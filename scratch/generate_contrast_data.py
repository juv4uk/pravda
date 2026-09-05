import re
import json

with open('scratch/svobod_dump.txt', 'r', encoding='utf-8') as f:
    s_blocks = f.read().split('\n\n')

with open('scratch/voln_noun_dump.txt', 'r', encoding='utf-8') as f:
    v_blocks = f.read().split('\n\n')

def parse_blocks(blocks):
    records = []
    for b in blocks:
        if not b.strip(): continue
        lines = b.strip().split('\n')
        m = re.match(r'\[([^\]]+)\]\s*\[([^\]]+)\]\s*(.*)', lines[0])
        if m:
            rec_id, src, loc = m.group(1), m.group(2), m.group(3)
            form_m = re.search(r'FORM:\s*(\S+)\s*\(([^)]+)\)', lines[1])
            form = form_m.group(1) if form_m else ""
            pos = form_m.group(2) if form_m else ""
            ctx = lines[2].replace('CTX:', '').strip()
            records.append({
                'id': rec_id,
                'src': src,
                'loc': loc,
                'form': form,
                'pos': pos,
                'ctx': ctx
            })
    return records

svob = parse_blocks(s_blocks)
voln = parse_blocks(v_blocks)

print(f"SVOB: {len(svob)}, VOLN: {len(voln)}")

# Detailed morphological categorization for VOLNOST
def analyze_voln(r):
    form = r['form']
    form_l = form.lower()
    src = r['src']
    ctx = r['ctx']
    ctx_l = ctx.lower()
    
    # Language
    if src in ['SRC-HADIACH-1658', 'SRC-HADIACH-1659']:
        lang = "Early Modern Polish" if not any('\u0400' <= c <= '\u04FF' for c in form) else "Early Modern Ruthenian"
    elif src in ['SRC-LS-1566', 'SRC-LS-1588']:
        lang = "Chancery Ruthenian (Grand Duchy of Lithuania)"
    elif src == 'SRC-MARCH-1654':
        lang = "Early Modern Russian / Ruthenian exchange"
    elif src == 'SRC-ORLYK-1710':
        lang = "Old Ukrainian (Hetmanate chancery standard)"
    else:
        lang = "Old Rus"
        
    # Case & Number
    # Default tags
    num = "PL"
    case = "GEN"
    prep = ""
    gov_verb = "UNKNOWN"
    modifier = ""
    holder = ""
    coord = []
    
    # Polish forms
    if lang == "Early Modern Polish":
        if form_l in ['wolnościami']:
            case = "INS"
            num = "PL"
        elif form_l in ['wolnościom']:
            case = "DAT"
            num = "PL"
        elif form_l in ['wolnościach']:
            case = "LOC"
            num = "PL"
        elif form_l in ['wolności']:
            # Could be GEN.SG, DAT.SG, LOC.SG, or NOM.PL, ACC.PL, GEN.PL
            # Inspect preposition or verb
            if 'przy ' in ctx_l:
                case = "LOC"
                num = "SG/PL"
            elif 'zażywać' in ctx_l or 'zażywa' in ctx_l:
                case = "GEN"
                num = "PL"
            elif 'do ' in ctx_l:
                case = "GEN"
                num = "SG"
            elif 'ujmę' in ctx_l or 'uymę' in ctx_l:
                case = "GEN"
                num = "PL"
            else:
                case = "GEN/ACC"
                num = "PL"
    else:
        # Cyrillic forms
        if form_l in ['вольность']:
            case = "NOM/ACC"
            num = "SG"
        elif form_l in ['вольностью']:
            case = "INS"
            num = "SG"
        elif form_l in ['вольностей', 'вольностеи']:
            case = "GEN"
            num = "PL"
        elif form_l in ['вольностяхъ', 'вольностях', 'вольностехъ']:
            case = "LOC"
            num = "PL"
        elif form_l in ['вольностям']:
            case = "DAT"
            num = "PL"
        elif form_l in ['вольности', 'вольносьти', 'вольності']:
            if 'при ' in ctx_l or 'въ ' in ctx_l:
                case = "LOC"
                num = "SG/PL"
            elif 'на ' in ctx_l:
                case = "ACC"
                num = "PL"
            elif 'сторожы' in ctx_l:
                case = "GEN"
                num = "SG"
            else:
                case = "GEN/ACC/NOM"
                num = "PL"
                
    # Detect governing verb / preposition
    for p in ['при ', 'въ ', 'на ', 'межы ', 'до ', 'зъ ', 'од ', 'проти ']:
        if p in ctx_l:
            prep = p.strip()
            break
            
    vbs = ['заховати', 'заховуючи', 'заживати', 'уживати', 'ужывати', 'порушити', 'порушати', 
           'потвердити', 'потвержаемъ', 'отбирати', 'отводити', 'обваровали', 'привлащати', 
           'конфирмуе', 'поламати', 'піднявся', 'домогтися', 'змогла', 'розширенью', 'примноженыя',
           'gaudere', 'przypuszczamy', 'zostawuią', 'zostawały']
    for v in vbs:
        if v in ctx_l:
            gov_verb = v
            break
            
    # Modifiers
    mods = ['шляхец', 'хрестіян', 'посполит', 'давн', 'стародавн', 'войсков', 'військ', 'руськ', 'козац', 'szlacheck', 'spólny', 'koronn']
    for m in mods:
        if m in ctx_l:
            modifier = m
            break
            
    # Coordinated terms
    if 'прав' in ctx_l or 'praw' in ctx_l:
        coord.append('PRAVA')
    if 'свобод' in ctx_l or 'swobod' in ctx_l:
        coord.append('SVOBODY')
    if 'привил' in ctx_l or 'przywilei' in ctx_l:
        coord.append('PRIVILEGE')
    if 'звыча' in ctx_l or 'zwyczaj' in ctx_l:
        coord.append('ZVYCHAY')
    if 'порядок' in ctx_l:
        coord.append('PORYADOK')
        
    # Holder / Referent
    if 'шлях' in ctx_l or 'rycer' in ctx_l or 'szlach' in ctx_l:
        holder = "Шляхта / рицерство"
    elif 'войск' in ctx_l or 'woysk' in ctx_l or 'козац' in ctx_l:
        holder = "Військо Запорозьке / козацтво"
    elif 'народ' in ctx_l:
        holder = "Народ руський / народи"
    elif 'религ' in ctx_l or 'cerkiew' in ctx_l:
        holder = "Релігія / духовенство"
    elif 'академи' in ctx_l or 'akadem' in ctx_l:
        holder = "Академія / колегія"
    else:
        holder = "Корпорація / стан / міщани"
        
    return {
        'id': r['id'],
        'src': src,
        'loc': r['loc'],
        'lang': lang,
        'form': form,
        'case': case,
        'num': num,
        'prep': prep,
        'gov_verb': gov_verb,
        'modifier': modifier,
        'coord': coord,
        'holder': holder,
        'ctx': ctx
    }

analyzed_voln = [analyze_voln(r) for r in voln]
print(f"Analyzed {len(analyzed_voln)} VOLN records.")

# Detailed analysis for SVOBODA
def analyze_svob(r):
    form = r['form']
    form_l = form.lower()
    src = r['src']
    ctx = r['ctx']
    ctx_l = ctx.lower()
    
    if src in ['SRC-HADIACH-1658', 'SRC-HADIACH-1659']:
        lang = "Early Modern Polish" if not any('\u0400' <= c <= '\u04FF' for c in form) else "Early Modern Ruthenian"
    elif src in ['SRC-LS-1566', 'SRC-LS-1588']:
        lang = "Chancery Ruthenian (Grand Duchy of Lithuania)"
    elif src in ['SRC-RP-SHORT', 'SRC-RP-EXP']:
        lang = "Old Rus / Church Slavonic recension"
    elif src == 'SRC-ORLYK-1710':
        lang = "Old Ukrainian (Hetmanate chancery standard)"
    else:
        lang = "Unknown"
        
    # POS, Case, Number, Role
    pos = r['pos']
    case = ""
    num = ""
    role = ""
    referent = ""
    
    if pos == 'ADJ':
        if form_l in ['свободна', 'свободнаго']:
            case = "ACC/GEN.SG.M"
            num = "SG"
            role = "ATTRIBUTIVE (мужа)"
            referent = "Вільна людина (не-холоп)"
        elif form_l in ['свободнемь']:
            case = "LOC.SG.M"
            num = "SG"
            role = "SUBSTANTIVIZED / ATTRIBUTIVE"
            referent = "Вільна людина"
        elif form_l in ['свободными']:
            case = "INS.PL"
            num = "PL"
            role = "ATTRIBUTIVE (послухи)"
            referent = "Вільні свідки на суді"
        elif form_l in ['свободныхъ', 'свободных']:
            case = "GEN.PL"
            num = "PL"
            role = "ATTRIBUTIVE (людии / полонених)"
            referent = "Вільні люди / звільнені бранці"
        elif form_l in ['свободнии']:
            case = "NOM.PL"
            num = "PL"
            role = "SUBSTANTIVIZED"
            referent = "Вільні співучасники злочину"
        elif form_l in ['swobodnie']:
            pos = "ADV"
            role = "ADVERBIAL MANNER"
            referent = "Безперешкодне відправлення обряду/наук"
        elif form_l in ['свободити']:
            pos = "VERB"
            role = "INFINITIVE OBJECT"
            referent = "Акт визволення отчизни"
        elif form_l in ['свободахъ', 'свободъ', 'свободами']:
            # Correction of inventory POS
            pos = "NOUN"
            case = "LOC/GEN/INS.PL"
            num = "PL"
            role = "OBJECT OF PREPOSITION"
            referent = "Шляхетські/християнські привілеї"
    elif pos == 'NOUN':
        if form_l in ['свобода']:
            case = "NOM.SG"
            num = "SG"
            role = "PREDICATIVE NOUN"
            referent = "Акт/стан набуття волі (закуп, діти рабині)"
        elif form_l in ['свободы']:
            if src == 'SRC-RP-EXP':
                case = "GEN.SG"
                num = "SG"
                role = "OBJECT OF PREPOSITION (від поселення)"
                referent = "Поселення-слобода"
            else:
                case = "GEN.SG/ACC.PL"
                num = "SG/PL"
                role = "OBJECT"
                referent = "Бажана свобода війська / права"
        elif form_l in ['свободу']:
            case = "ACC.SG"
            num = "SG"
            role = "OBJECT OF PREPOSITION"
            referent = "Первісний стан свободи народу"
        elif form_l in ['swobodach']:
            case = "LOC.PL"
            num = "PL"
            role = "OBJECT OF PREPOSITION (przy)"
            referent = "Права й свободи народів"
            
    return {
        'id': r['id'],
        'src': src,
        'loc': r['loc'],
        'lang': lang,
        'form': form,
        'pos': pos,
        'case': case,
        'num': num,
        'role': role,
        'referent': referent,
        'ctx': ctx
    }

analyzed_svob = [analyze_svob(r) for r in svob]
print(f"Analyzed {len(analyzed_svob)} SVOB records.")

with open('scratch/analyzed_voln.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_voln, f, ensure_ascii=False, indent=2)

with open('scratch/analyzed_svob.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_svob, f, ensure_ascii=False, indent=2)

print("Data saved to scratch/*.json")
