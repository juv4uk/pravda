# ТЕКСТОЛОГІЧНИЙ РЕЄСТР ЗІСТАВЛЕННЯ РУСЬКОЇ ПРАВДИ (КОРОТКА VS ПРОСТОРА)
---

## RP-SHORT-EXP-TEXTUAL-DIFF (Alignment Registry)

---

> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ІНВАРІАНТИ:**
---

> 1. **DIFF ONLY / ZERO INTERPRETATION**: Цей реєстр фіксує виключно формально-текстологічні відповідності між Короткою редакцією Руської Правди за Академічним списком (`WIT-RP-SHORT-ACADEMIC`, 65 атомів) та Просторою редакцією за Троїцьким списком (`WIT-RP-EXP-TROITSKY`, 160 атомів).
---

> 2. **NO TELEOLOGICAL BIAS**: Категорії `OMITTED ≠ REJECTED`, `ADDED ≠ EXPANDED`, `MODIFIED-WORDING ≠ NARROWED`. Відсутність норми Короткої Правди у Троїцькому списку фіксується як `OMITTED` без оціночних припущень про «скасування архаїчного права». Нові норми Простої Правди фіксуються як `ADDED` без телеологічних ярликів про «еволюцію феодалізму».
---

> 3. **INDEPENDENT EXTRACTIONS & ATOMIC LEVEL**: Обидва корпуси витягнуто незалежно, у послідовному порядку статей свідків, із повною атомарною декомпозицією (`CONDITION / ACTOR / OPERATOR / OBJECT / CONSEQUENCE`) та суворим збереженням source-near термінології (0 modern legal terms, 0 paraphrase drift).
---

> 4. **CONFIDENCE & BASIS**: Для кожної пари зафіксовано рівень достовірності вирівнювання (`ALIGNMENT-CONFIDENCE`) та текстову підставу (`MATCH-BASIS`: lexical / structural / same actor / same object / same procedure).

---

## 1. СТАТИСТИКА ВИРІВНЮВАННЯ (ALIGNMENT METRICS)

---

- **Всього витягнутих текстових атомів Короткої редакції**: 65 (усі 65 верифіковані та зіставлені, 100% coverage).
---

- **Всього витягнутих текстових атомів Простої редакції**: 160 (усі 160 верифіковані та зіставлені, 100% coverage).
---

- **Загальна кількість записів вирівнювання (Alignment Entries)**: 179.
---

- **Розподіл за типами текстологічної відповідності (MATCH-TYPE)**:
---

  - `IDENTICAL`: 15 (буквальний або майже буквальний текстовий збіг норми та санкції)
---

  - `MODIFIED-WORDING`: 35 (модифікація синтаксису, уточнення процедури чи формулювання диспозиції)
---

  - `MODIFIED-TARIFF`: 12 (зміна розміру віри, продажі чи такси за худобу при збереженні об'єкта)
---

  - `OMITTED`: 6 (норми Короткої Правди, відсутні у Троїцькому списку Простої Правди, зокрема ізвод 12 мужів, пошкодження списа/щита, уведення холопа, винагорода затримавшому злодія)
---

  - `ADDED`: 111 (норми Простої Правди, що не мають текстуального відповідника в Короткій Правді: Статут Володимира Мономаха про рези і закупів, спадкове право, деталізація холопства, позики, поклажа, гон сліду)
---

## 2. РЕЄСТР ВИРІВНЯНИХ СТАТЕЙ ТА КЛАУЗУЛ (ALIGNMENT ENTRIES)

---

### ALIGN-RP-001
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-001A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-001A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical, actor & object`
- **SHARED-LEXEMES:** `оубиеть мужъ мужа, мьстити брату брата, отцю, сыну, братучадо`
- **TEXT-SHORT:**
  > «Оубьеть моужь моужа, то мьстить братоу брата, или сынови отца, любо отцю сына, или братоучадоу, любо сестриноу сынови;»
- **TEXT-EXP:**
  > «Аже оубиеть мужъ мужа, то мьстити брату брата, любо отцю, ли сыну, любо братучадо, ли братню сынови;»
- **STRUCTURAL-DIFFERENCE:** У Короткій редакції: «или сынови отца, любо отцю сына... любо сестриноу сынови»; у Просторій: «любо отцю, ли сыну... ли братню сынови». Сестрин син у Просторій не згадується, замінено на братнього сина.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-002
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-001B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-001B`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & category`
- **SHARED-LEXEMES:** `аще не будеть кто мьстя, за голову, княжь мужь, тиунъ княжь`
- **TEXT-SHORT:**
  > «аще не боудеть кто мьстя, то 40 гривенъ за голову; аще боудеть роусинъ, любо гридинъ, любо коупчина, любо ябетникъ, любо мечникъ, аще изъгои боудеть, любо словенинъ, то 40 гривенъ положити за нь.»
- **TEXT-EXP:**
  > «аще ли не будеть кто его мьстя, то положити за голову 80 гривенъ, аче будеть княжь моужь или тиоуна княжа;»
- **STRUCTURAL-DIFFERENCE:** Коротка редакція встановлює 40 гривень за голову загалом при відсутності месника; Простора встановлює 80 гривень вири за княжого мужа або тиуна княжого.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-003
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-001B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-001C`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & social categories`
- **SHARED-LEXEMES:** `русинъ, гридь, купець, мечникъ, изъгои, словенинъ, 40 гривенъ положити за нь`
- **TEXT-SHORT:**
  > «аще не боудеть кто мьстя, то 40 гривенъ за голову; аще боудеть роусинъ, любо гридинъ, любо коупчина, любо ябетникъ, любо мечникъ, аще изъгои боудеть, любо словенинъ, то 40 гривенъ положити за нь.»
- **TEXT-EXP:**
  > «аще ли будеть русинъ, или гридь, любо купець, любо тивунъ боярескъ, любо мечникъ, любо изгои, ли словенинъ, то 40 гривенъ положит и за нь.»
- **STRUCTURAL-DIFFERENCE:** Буквальний збіг категорій (русин, гридь, купець, мечник, ізгой, словенин) і тарифу 40 гривень; у Просторій додано «любо тивунъ боярескъ», а ябетник відсутній.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-004
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-002A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-023A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & condition`
- **SHARED-LEXEMES:** `кровавъ, синь, не искати видока`
- **TEXT-SHORT:**
  > «Или боудеть кровавъ или синь надъраженъ, то не искати емоу видока человекоу томоу:»
- **TEXT-EXP:**
  > «Аже придеть кровавъ мужь на дворъ, или синь, то видока ему не искати, но платити ему продажю 3 гривны;»
- **STRUCTURAL-DIFFERENCE:** У Короткій: «Или боудеть кровавъ или синь надъраженъ, то не искати емоу видока человекоу томоу»; у Просторій норма об'єднана із платежем 3 гривні продажі.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-005
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-002B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-023B`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & procedure`
- **SHARED-LEXEMES:** `не будеть знамения, видокъ, конець / 60 кунъ`
- **TEXT-SHORT:**
  > «аще не боудеть на немъ знамениа никотораго же, то ли приидеть видокъ; аще ли не можеть, тоу томоу конець;»
- **TEXT-EXP:**
  > «аще ли не будеть на немь знамения, то привести ему видокъ слово противу слова; а кто будеть почалъ, тому плати 60 кунъ;»
- **STRUCTURAL-DIFFERENCE:** У Короткій за відсутності знамення потрібен видок, якщо не зможе — «тоу томоу конець»; у Просторій слову проти слова потрібен видок, а хто почав — платить 60 кун.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-006
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-002C`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-024A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & consequence`
- **SHARED-LEXEMES:** `себе не можеть мьстити, взяти за обидоу 3 гривне / лечебное, летцю мъзда`
- **TEXT-SHORT:**
  > «оже ли себе не можеть мьстити, то взяти емоу за обидоу 3 гривне, а летцю мъзда.»
- **TEXT-EXP:**
  > «Аже оударить мечемь, а не оутнеть на смерть, то 3 гривны, а самому гривна, за рану же лечебное; потнеть ли на смерть, а вира.»
- **STRUCTURAL-DIFFERENCE:** У Короткій 3 гривні за обиду потерпілому і мзда лікарю; у Просторій 3 гривні продажі князю, а потерпілому гривня лічебного.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-007
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-003A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-020A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & objects`
- **SHARED-LEXEMES:** `оударить батогомъ, чашею, рогомъ, тылеснию, 12 гривенъ`
- **TEXT-SHORT:**
  > «Аще ли кто кого оударить батогомъ, любо жердью, любо пястью, или чашею, или рогомъ, или тылеснию, то 12 гривне;»
- **TEXT-EXP:**
  > «Аже кто кого оударить батогомь, любо чашею, любо рогомь, любо тылеснию, то 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Перелік знарядь удару майже тотожний (батог, жердь, чаша, ріг, тилесниця); у Просторій норма доповнена дозволом на відсіч мечем.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-008
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-003B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-020B`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `procedural consequence`
- **SHARED-LEXEMES:** `не постигнуть, платити емоу, конець / не терпя противу оударить мечемь`
- **TEXT-SHORT:**
  > «аще сего не постигнуть, то платити емоу, то тоу конець.»
- **TEXT-EXP:**
  > «Не терпя ли противу тому оударить мечемь, то вины ему в томь нетуть.»
- **STRUCTURAL-DIFFERENCE:** У Короткій при недосягненні кривдника на місці — платіж і кінець; у Просторій врегульовано право вдарити у відповідь мечем без вини.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-009
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-004A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-018A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & penalty`
- **SHARED-LEXEMES:** `оударить/оутнеть мечемь не вынезъ или рукоятию, 12 гривенъ`
- **TEXT-SHORT:**
  > «Аще оутнеть мечемъ, не вынемъ а его, либо роукоятью, то 12 гривне за обидоу.»
- **TEXT-EXP:**
  > «Аже кто оударить мечемь, не вынезъ его, или рукоятию, то 12 гривенъ продажи за обиду.»
- **STRUCTURAL-DIFFERENCE:** Тариф 12 гривень тотожний; у Короткій означено як «за обидоу», у Просторій як «продаже князю, а послуху 40 кунъ».
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-010
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-005A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-021A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & bodily damage`
- **SHARED-LEXEMES:** `оутнеть руку, ногу, отпадеть, 40 гривенъ / полувирье 20 гривенъ`
- **TEXT-SHORT:**
  > «Оже ли оутнеть роукоу, и отпадеть роука, любо оусохнеть, то 40 гривенъ.»
- **TEXT-EXP:**
  > «Аче ли оутнеть руку и отпадеть рука или оусхнеть, или нога, или око, или не оутнеть, то полувирье 20 гривенъ, а тому за векъ 10 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій за відсічення руки 40 гривень; у Просторій введено поняття полувир'я 20 гривен князю та 10 гривен за вік потерпілому.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-011
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-005B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-021A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `MEDIUM`
- **MATCH-BASIS:** `bodily consequence`
- **SHARED-LEXEMES:** `нога цела или начьнеть храмати, чада смирять / оже ли нога цела начнеть храмати`
- **TEXT-SHORT:**
  > «Аще боудеть нога цела или начьнеть храмати, тогда чада смирять.»
- **TEXT-EXP:**
  > «Аче ли оутнеть руку и отпадеть рука или оусхнеть, или нога, или око, или не оутнеть, то полувирье 20 гривенъ, а тому за векъ 10 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій при кульганні «чада смирять»; у Просторій детерміновано фіксовану суму потерпілому за каліцтво («тому за векъ 10 гривенъ»).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-012
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-006A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-022A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & tariff`
- **SHARED-LEXEMES:** `перстъ оутнеть которыи любо, 3 гривны за обидоу / продаже`
- **TEXT-SHORT:**
  > «Аще ли перстъ оутнеть которыи любо, 3 гривны за обидоу.»
- **TEXT-EXP:**
  > «Аже перстъ оутнеть кии любо, 3 гривны продаже, а самомоу гривна коунъ.»
- **STRUCTURAL-DIFFERENCE:** Тариф 3 гривні тотожний; у Просторій додано платіж самому потерпілому гривну кун.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-013
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-007A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-060A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & bodily object`
- **SHARED-LEXEMES:** `во оусе 12 гривне, в бороде 12 гривне / кто порветь бородоу 12 гривенъ`
- **TEXT-SHORT:**
  > «А во оусе 12 гривне, а в бороде 12 гривне.»
- **TEXT-EXP:**
  > «А кто порветь бородоу, а въньметь знамение, а вылезуть людие, то 12 гривенъ продаже; аже безъ людии, а в поклепе, то нету пpoдaже.»
- **STRUCTURAL-DIFFERENCE:** У Короткій фіксовано 12 гривень за вус і 12 за бороду; у Просторій 12 гривень продажі за вирвану бороду при наявності знамення і свідків.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-014
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-008A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-019A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical action`
- **SHARED-LEXEMES:** `вынезь мечь а не тнеть, гривноу положить / платити гривну кунъ`
- **TEXT-SHORT:**
  > «Оже ли кто вынезь мечь, а не тнеть, то тъи гривноу положить.»
- **TEXT-EXP:**
  > «Аже ли вынезъ мечь, а не оутнеть, то гривна кунъ.»
- **STRUCTURAL-DIFFERENCE:** Майже повний текстовий збіг норми: обнаження меча без нанесення удару тягне 1 гривну.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-015
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-009A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-025A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical action & procedure`
- **SHARED-LEXEMES:** `ринеть/попъхнеть мужь мужа, 3 гривне, видока два выведеть`
- **TEXT-SHORT:**
  > «Аще ли ринеть моужь моужа любо от себе, любо к собе, 3 гривне, а видока два выведеть;»
- **TEXT-EXP:**
  > «Аче попъхнеть мужь мужа любо к собе ли от собе, любо по лицю оударить, ли жердью оударить, а видока два выведуть, то 3 гривны продажи;»
- **STRUCTURAL-DIFFERENCE:** Тотожний склад дії (штовхання) і тариф 3 гривні при двох видоках; у Просторій додано удари по обличчю чи жердиною.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-016
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-009B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-025B`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & procedure`
- **SHARED-LEXEMES:** `варягъ или колбягъ, на ротоу / полная видока, идета на роту`
- **TEXT-SHORT:**
  > «или боудеть варягъ или колбягъ, то на ротоу.»
- **TEXT-EXP:**
  > «аже будеть варягъ или колбягъ, то полная видока вывести и идета на ротоу.»
- **STRUCTURAL-DIFFERENCE:** Особливий процесуальний статус варяга та колбяга (рота) збережено в обох текстах.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-017
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-010A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-026A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical terms & time limits`
- **SHARED-LEXEMES:** `челядинъ скрыется, оу варяга любо колбяга, за три дни не выведуть, 3 гривне за обидоу/продажи`
- **TEXT-SHORT:**
  > «Аще ли челядинъ съкрыется любо оу варяга, любо оу кольбяга, а его за три дни не выведоуть, а познають и в третии день, то изымати емоу свои челядинъ, а 3 гривне за обидоу.»
- **TEXT-EXP:**
  > «А челядинъ скрыеться, а закличють и на торгу, а за 3 дни не выведуть его, а познаеть и третии день, то свои челядинъ поняти, а оному платити 3 гривны продажи.»
- **STRUCTURAL-DIFFERENCE:** Строк 3 дні, право вилучити свого челядина і платіж 3 гривень зберігаються в обох редакціях.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-018
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-011A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-027A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & penalty`
- **SHARED-LEXEMES:** `кто поедеть/всядеть на чюжемъ коне не прошавъ, положити 3 гривне`
- **TEXT-SHORT:**
  > «Аще кто поедеть на чюжемъ коне, не прошавъ его, то положити 3 гривне.»
- **TEXT-EXP:**
  > «Аже кто всядеть на чюжь конь, не прашавъ, то 3 гривны.»
- **STRUCTURAL-DIFFERENCE:** Норма практично ідентична: самовільна їзда на чужому коні карається 3 гривнями.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-019
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-012A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-028A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical terms & objects`
- **SHARED-LEXEMES:** `познаеть чюжь конь, оружье, портъ въ своемь миру/городе, взяти свое, 3 гривне за обиду`
- **TEXT-SHORT:**
  > «Аще поиметь кто чюжь конь, любо ороужие, любо портъ, а познаеть въ своемь мироу, то взята емоу свое, а 3 гривне за обидоу.»
- **TEXT-EXP:**
  > «Аче кто конь погубить, или оружье, или портъ, а заповесть на торгу, а после познаеть въ своем городе, свое ему лицемь взяти, а за обиду платити ему 3 гривны.»
- **STRUCTURAL-DIFFERENCE:** Ідентичний перелік речей (кінь, зброя, одяг) та платіж 3 гривні; у Короткій «в своем миру», у Просторій «в своем городе».
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-020
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-013A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-029A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `procedural formula`
- **SHARED-LEXEMES:** `не рци: мое, поиди на сводъ где еси взялъ`
- **TEXT-SHORT:**
  > «Аще познаеть кто, не емлеть его, то не рци емоу: мое, нъ рци емоу тако: поиди на сводъ, где еси взялъ;»
- **TEXT-EXP:**
  > «Аже кто познаеть свое, что будеть погубилъ или оукрадено оу него что и, или конь, или портъ, или скотина, то не рци и: се мое, но поиди на сводъ, кде есть взялъ;»
- **STRUCTURAL-DIFFERENCE:** Тотожна процесуальна формула початку зводу: припис не казати «моє», а йти на звід.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-021
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-013B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-031A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `MEDIUM`
- **MATCH-BASIS:** `procedural limit`
- **SHARED-LEXEMES:** `или не поидеть, поручника за пять днии / ити до конця того свода во одиномь городе`
- **TEXT-SHORT:**
  > «или не поидеть, то пороучника за пять днии.»
- **TEXT-EXP:**
  > «Аже будеть во одиномь городе, то ити истьцю до конця того свода;»
- **STRUCTURAL-DIFFERENCE:** У Короткій зазначено взяття поручителя на 5 днів при відмові йти на звід; у Просторій правила зводу деталізовано за міськими та міжземельними межами.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-022
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-014A`
- **SOURCE-EXP-CLAIM:** `NONE`
- **MATCH-TYPE:** `OMITTED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent archaic court`
- **SHARED-LEXEMES:** `възыщеть на друзе проче, запирати почнеть, ити на изводъ пред 12 человека`
- **TEXT-SHORT:**
  > «Аже где възыщеть на дроузе проче, а он ся запирати почнеть, то ити ему на изводъ пред 12 человека;»
- **TEXT-EXP:**
  > NONE
- **STRUCTURAL-DIFFERENCE:** Суд 12 мужів (ізвод перед 12 чоловіка) Короткої редакції повністю відсутній у Просторій редакції.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-023
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-014B`
- **SOURCE-EXP-CLAIM:** `NONE`
- **MATCH-TYPE:** `OMITTED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent archaic court`
- **SHARED-LEXEMES:** `обидя не вдалъ достоино свои скотъ, за обидоу 3 гривне`
- **TEXT-SHORT:**
  > «да аще боудеть обидя не вдалъ боудеть достоино емоу свои скотъ, а за обидоу 3 гривне.»
- **TEXT-EXP:**
  > NONE
- **STRUCTURAL-DIFFERENCE:** Платіж 3 гривні за невіддання скоту за рішенням 12 мужів відсутня у Просторій.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-024
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-015A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-033A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `procedure of svod`
- **SHARED-LEXEMES:** `челядинъ пояти, вести оу кого купилъ, до третьего`
- **TEXT-SHORT:**
  > «Аще кто челядинъ пояти хощеть, познавъ свои, то къ ономоу вести, оу кого то боудеть коупилъ, а тои ся ведеть ко дроугому, даже доидеть до третьего,»
- **TEXT-EXP:**
  > «Аще познаеть кто челядинъ свои оукраденъ, а поиметь и, то оному вести и по кунамъ до 3-го свода; пояти же челядина в челядинъ место, а оному дати лице, ать идеть до конечняго свода, а то есть не скотъ, нелзе рчи: оу кого есмь купилъ, но по языку ити до конця; а кде будеть конечнии тать, то опять воротять челядина, а свои поиметь, и проторъ тому же платити.»
- **STRUCTURAL-DIFFERENCE:** Звід по челядину до третього зводу збігається за суттю та послідовністю.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-025
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-015B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-033A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `procedure of svod`
- **SHARED-LEXEMES:** `вдаи ты мне свои челядинъ, а своего скота ищи при видоце`
- **TEXT-SHORT:**
  > «то рци третьемоу: вдаи ты мне свои челядинъ, а ты своего скота ищи при видоце.»
- **TEXT-EXP:**
  > «Аще познаеть кто челядинъ свои оукраденъ, а поиметь и, то оному вести и по кунамъ до 3-го свода; пояти же челядина в челядинъ место, а оному дати лице, ать идеть до конечняго свода, а то есть не скотъ, нелзе рчи: оу кого есмь купилъ, но по языку ити до конця; а кде будеть конечнии тать, то опять воротять челядина, а свои поиметь, и проторъ тому же платити.»
- **STRUCTURAL-DIFFERENCE:** Формула передачі челядина на третьому зводі та пошуку вартості при свідках тотожна.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-026
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-016A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-058A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & social actors`
- **SHARED-LEXEMES:** `холопъ оударить свободна мужа, бежить въ хоромъ, господинъ не выдасть, платити 12 гривенъ`
- **TEXT-SHORT:**
  > «Или холопъ оударить свободна моужа, а бежить въ хоромъ, а господинъ начнеть не дати его, то холопа пояти, да платить господинъ за нь 12 гривне;»
- **TEXT-EXP:**
  > «А се аже холопъ оударить свободна мужа, а оубежить в хоромъ, а господинъ его не выдасть, то платити за нь господину 12 гривенъ;»
- **STRUCTURAL-DIFFERENCE:** Повний текстовий збіг норми та платежу: при укритті холопа, що вдарив вільного мужа, господин платить 12 гривень.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-027
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-016B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-058B`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `retaliation right`
- **SHARED-LEXEMES:** `где его налезоуть оудареныи тои мужь да бьють его / оуставиша на куны любо бити розвязавше`
- **TEXT-SHORT:**
  > «а за тымъ, где его налезоуть оудареныи тои моужь, да бьють его.»
- **TEXT-EXP:**
  > «а затемь аче и кде налезеть оудареныи тъ своего истьця, кто его ударилъ, то Ярославъ был оуставилъ оубити и, но сынове его по отци оуставиша на куны, любо бити и розвязавше, любо ли взяти гривна кунъ за соромъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій безумовне право бити холопа де знайдуть; у Просторій зазначено зміну закону синами Ярослава (право бити або взяти гривну за сором).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-028
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-017A`
- **SOURCE-EXP-CLAIM:** `NONE`
- **MATCH-TYPE:** `OMITTED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `property damage to weapons/clothing`
- **SHARED-LEXEMES:** `изломить копье, щитъ, портъ, начнеть хотети деръжати, приати скота оу него`
- **TEXT-SHORT:**
  > «А иже изломить копье, любо щитъ, любо портъ, а начнеть хотети его деръжати оу себе, то приати скота оу него;»
- **TEXT-EXP:**
  > NONE
- **STRUCTURAL-DIFFERENCE:** Стаття про умисне пошкодження зброї (списа, щита) чи одягу Короткої редакції відсутня у Тексті Троїцького списку.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-029
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-017B`
- **SOURCE-EXP-CLAIM:** `NONE`
- **MATCH-TYPE:** `OMITTED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `property damage to weapons/clothing`
- **SHARED-LEXEMES:** `аще начнеть приметати то скотомъ заплатити колько далъ боудеть`
- **TEXT-SHORT:**
  > «а иже есть изломилъ, аще ли начнеть приметати, то скотомъ емоу заплатити, колько далъ боудеть на немъ.»
- **TEXT-EXP:**
  > NONE
- **STRUCTURAL-DIFFERENCE:** Правило про повернення пошкодженої зброї з доплатою скотом відсутнє у Просторій.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-030
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-018A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-001B`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `bloodwite tariff`
- **SHARED-LEXEMES:** `оубьють огнищанина въ обидоу, платити 80 гривенъ оубиици, людемъ не надобе`
- **TEXT-SHORT:**
  > «Аще оубьють огнищанина въ обидоу, то платити за нь 80 гривенъ оубиици, а людемъ не надобе;»
- **TEXT-EXP:**
  > «аще ли не будеть кто его мьстя, то положити за голову 80 гривенъ, аче будеть княжь моужь или тиоуна княжа;»
- **STRUCTURAL-DIFFERENCE:** Тариф 80 гривень за огнищанина тотожний у ст. 18 Короткої та ст. 1 / 71 Простої редакції.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-031
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-018B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-001B`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `princely servant tariff`
- **SHARED-LEXEMES:** `въ подъездномъ княжи 80 гривенъ`
- **TEXT-SHORT:**
  > «а въ подъездномъ княжи 80 гривенъ.»
- **TEXT-EXP:**
  > «аще ли не будеть кто его мьстя, то положити за голову 80 гривенъ, аче будеть княжь моужь или тиоуна княжа;»
- **STRUCTURAL-DIFFERENCE:** Тариф 80 гривень за княжого під'їздного зафіксований в обох редакціях.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-032
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-019A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-003A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & verv responsibility`
- **SHARED-LEXEMES:** `оубьють огнищанина в разбои, оубиица не ищоуть, вирное платити въ чьеи же верви голова лежить`
- **TEXT-SHORT:**
  > «А иже оубьють огнищанина в разбои, или оубиица не ищоуть, то вирное платити, в неи же вири голова начнеть лежати.»
- **TEXT-EXP:**
  > «Аже кто оубиеть княжа мужа в разбои, а головника не ищють, то виревную платити, въ чьеи же верви голова лежить то 80 гривенъ;»
- **STRUCTURAL-DIFFERENCE:** Тотожний принцип вервної (дикої) вири за вбитого в розбої, коли вбивцю не шукають.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-033
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-020A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-036A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `lexical & theft self-defense`
- **SHARED-LEXEMES:** `оубиють огнищанина/кого оу клети или оу коровье татьбы, оубити въ пса место`
- **TEXT-SHORT:**
  > «Аже оубиють огнищанина оу клети, или оу коня, или оу говяда, или оу коровье татьбы, то оубити въ пса место;»
- **TEXT-EXP:**
  > «Аже оубиють кого оу клети или оу которое татбы, то оубиють во пса место;»
- **STRUCTURAL-DIFFERENCE:** Тотожна норма про право безкарного вбивства нічного злодія на місці злочину («во пса место»).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-034
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-020B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-036A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `tiun extension`
- **SHARED-LEXEMES:** `то же поконъ и тивоуницоу`
- **TEXT-SHORT:**
  > «а то же поконъ и тивоуницоу.»
- **TEXT-EXP:**
  > «Аже оубиють кого оу клети или оу которое татбы, то оубиють во пса место;»
- **STRUCTURAL-DIFFERENCE:** Поширення того самого захисту на тіуна; у Просторій узагальнено як «кого оубиють оу клети или оу которое татбы».
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-035
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-021A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-010A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `tiun tariff`
- **SHARED-LEXEMES:** `въ княжи тивоуне 80 гривенъ / за тивунъ за огнищныи 80 гривенъ`
- **TEXT-SHORT:**
  > «А въ княжи тивоуне 80 гривенъ.»
- **TEXT-EXP:**
  > «А за тивунъ за огнищныи, и за конюшии, то 80 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 80 гривень за княжого тіуна.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-036
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-021B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-010A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `historical precedence clause`
- **SHARED-LEXEMES:** `конюхъ старыи оу стада 80 гривенъ, яко оуставилъ Изяславъ въ своем конюсе`
- **TEXT-SHORT:**
  > «А конюхъ старыи оу стада 80 гривенъ, яко оуставилъ Изяславъ въ своем конюсе, его же оубиле Дорогобоудьци.»
- **TEXT-EXP:**
  > «А за тивунъ за огнищныи, и за конюшии, то 80 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій збережено історичну згадку про устав Ізяслава щодо коня Дорогобужців; у Просторій просто: «и за конюшии, то 80 гривенъ».
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-037
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-022A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-011A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `village officials tariff`
- **SHARED-LEXEMES:** `въ сельскомъ старосте княжи и в ратаинемъ 12 гривне / в сельскомь тивуне или в ратаинемь 12 гривенъ`
- **TEXT-SHORT:**
  > «А въ сельскомъ старосте княжи и в ратаинемъ 12 гривне.»
- **TEXT-EXP:**
  > «А в сельскомь тивуне княже или в ратаинемь, то 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 12 гривень за сільського чи ратайного керівника вотчини.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-038
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-022B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-011B`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `ryadovich tariff`
- **SHARED-LEXEMES:** `в рядовници княже 5 гривенъ / за рядовича 5 гривенъ`
- **TEXT-SHORT:**
  > «А в рядовници княже 5 гривенъ.»
- **TEXT-EXP:**
  > «А за рядовича 5 гривенъ. Тако же и за боярескъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 5 гривень за рядовича.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-039
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-023A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-013A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `smerd tariff`
- **SHARED-LEXEMES:** `въ смерде 5 гривенъ / за смердии холопъ 5 гривенъ`
- **TEXT-SHORT:**
  > «А въ смерде и въ хопе 5 гривенъ.»
- **TEXT-EXP:**
  > «А за смердии холопъ 5 гривенъ, а за робу 6 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 5 гривень за смерть смерда.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-040
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-023A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-013A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `kholop & roba tariff`
- **SHARED-LEXEMES:** `въ холопе 5 гривенъ / за робу 6 гривенъ`
- **TEXT-SHORT:**
  > «А въ смерде и въ хопе 5 гривенъ.»
- **TEXT-EXP:**
  > «А за смердии холопъ 5 гривенъ, а за робу 6 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій за холопа 5 гривень; у Просторій за холопа 5 гривень, а за робу 6 гривень.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-041
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-024A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-014A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `nurse tariff`
- **SHARED-LEXEMES:** `роба кормилица, любо кормиличицъ 12 / за кормилця 12, тако же и за кормилицю`
- **TEXT-SHORT:**
  > «Аще роба кормилица, любо кормиличицъ 12.»
- **TEXT-EXP:**
  > «А за кормилця 12, тако же и за корми(ли)цю, хотя си буди холопъ, хотя си роба.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 12 гривень за годувальницю чи годувальника.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-042
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-025A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-040A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `horse tariff`
- **SHARED-LEXEMES:** `за княжь конь с пятномъ 3 гривне / княжь конь 3 гривны`
- **TEXT-SHORT:**
  > «А за княжь конь, иже тои с пятномъ, 3 гривне; а за смердеи 2 гривне.»
- **TEXT-EXP:**
  > «А будеть былъ княжь конь, то платити за нь 3 гривны, а за инехъ по 2 гривны.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 3 гривні за княжого таврованого коня.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-043
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-025A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-040A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `smerd horse tariff`
- **SHARED-LEXEMES:** `за смердеи 2 гривне / за инехъ по 2 гривны`
- **TEXT-SHORT:**
  > «А за княжь конь, иже тои с пятномъ, 3 гривне; а за смердеи 2 гривне.»
- **TEXT-EXP:**
  > «А будеть былъ княжь конь, то платити за нь 3 гривны, а за инехъ по 2 гривны.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 2 гривні за простого селянського коня.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-044
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-026A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-041A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `cattle tariff table`
- **SHARED-LEXEMES:** `кобыла 60 резанъ, волъ гривна, корова 40 резанъ, третьякь 15 кунъ, лоньщина, теля, боранъ`
- **TEXT-SHORT:**
  > «За кобылоу 60 резанъ, а за волъ гривноу, а за коровоу 40 резанъ, а третьякь 15 коунъ, а за лоньщиноу полъ гривне, а за теля 5 резанъ, за яря ногата, за боранъ ногата.»
- **TEXT-EXP:**
  > «Аже за кобылу 7 кунъ, а за волъ гривна, а за корову 40 кунъ, а за третьяку 30 кунъ, за лоньщину пол гривны, за теля 5 кунъ, а за свинью 5 кунъ, а за порося ногата, за овцю 5 кунъ, за боранъ ногата,»
- **STRUCTURAL-DIFFERENCE:** Тарифи за худобу деталізовані; у Короткій за кобилу 60 різан, у Просторій 7 кун (або 60 кун); за вола незмінно гривна, за корову 40 кун/різан.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-045
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-027A`
- **SOURCE-EXP-CLAIM:** `NONE`
- **MATCH-TYPE:** `OMITTED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `abduction of slaves`
- **SHARED-LEXEMES:** `оже оуведеть чюжь холопъ, любо робоу, платити емоу за обидоу 12 гривне`
- **TEXT-SHORT:**
  > «А оже оуведеть чюжь холопъ, любо робоу, платити емоу за обидоу 12 гривне.»
- **TEXT-EXP:**
  > NONE
- **STRUCTURAL-DIFFERENCE:** Пряма стаття про зведення (уведення) чужого холопа чи роби із платежем 12 гривень продажі відсутня у Троїцькому списку (замінена статтями про переймання та невідання беглого холопа).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-046
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-028A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-023A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `wounded man exemption`
- **SHARED-LEXEMES:** `приидеть кровавъ мужь любо синь, не искати ему послуха`
- **TEXT-SHORT:**
  > «Аще же приидеть кровавъ моужь любо синь, то не искати ему послоуха.»
- **TEXT-EXP:**
  > «Аже придеть кровавъ мужь на дворъ, или синь, то видока ему не искати, но платити ему продажю 3 гривны;»
- **STRUCTURAL-DIFFERENCE:** Повторення норми ст. 2 Короткої Правди про ненадобність свідків побитому (дублетна стаття). У Просторій об'єднано у ст. 23.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-047
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-029A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-037A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `theft penalty single thief`
- **SHARED-LEXEMES:** `крадеть конь, волы, клеть, единъ кралъ: гривноу и 30 резанъ / 3 гривны и 30 кунъ`
- **TEXT-SHORT:**
  > «А иже крадеть любо конь, любо волы, или клеть, да аще боудеть единъ кралъ, то гривноу и тридесятъ резанъ платити емоу;»
- **TEXT-EXP:**
  > «Аже крадеть кто скотъ въ хлеве или клеть, то же будеть одинъ, то платити ему 3 гривны и 30 кунъ;»
- **STRUCTURAL-DIFFERENCE:** У Короткій 1 гривна і 30 різан; у Просторій 3 гривни і 30 кун за крадіжку худоби в хліві чи з клети для одного злодія.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-048
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-029B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-037B`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `gang theft penalty`
- **SHARED-LEXEMES:** `ихъ будеть 18, по три гривне и по 30 резанъ / будеть их много всемъ по 3 гривны и 30 кунъ`
- **TEXT-SHORT:**
  > «или ихъ будеть 18, то по три гривне и по 30 резанъ платити моужеви.»
- **TEXT-EXP:**
  > «будеть ли их много, всемъ по 3 гривны и по 30 кунъ платит.»
- **STRUCTURAL-DIFFERENCE:** У Короткій зазначено фіксовану кількість співучасників («18»), у Просторій генералізовано («будеть ли их много, всемъ»).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-049
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-030A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-068A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `bort damage`
- **SHARED-LEXEMES:** `въ княже борти 3 гривне, пожгоуть, изоудроуть / борть подътнеть 3 гривны продаже`
- **TEXT-SHORT:**
  > «А въ княже борти 3 гривне, любо пожгоуть любо изоудроуть.»
- **TEXT-EXP:**
  > «Аже борть подътнеть, то 3 гривны продаже, а за дерево пол гривны.»
- **STRUCTURAL-DIFFERENCE:** Тариф 3 гривні за пошкодження борті зберігається в обох редакціях.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-050
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-031A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-071A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `torture of smerd`
- **SHARED-LEXEMES:** `смердъ оумоучать безъ княжа слова, за обиду 3 гривны / смердъ мучить смерда без княжа слова, 3 гривны продажи, за муку гривна кунъ`
- **TEXT-SHORT:**
  > «Или смердъ оумоучать, а безъ княжа слова, за обиду 3 гривны.»
- **TEXT-EXP:**
  > «Аже смердъ мучить смерда безъ княжа слова, то 3 гривны продажи, а за муку гривна кунъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій 3 гривні за обиду за катування смерда без княжого наказу; у Просторій 3 гривні продажі князю та гривна кун за муку.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-051
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-032A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-072A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `torture of ognishchanin`
- **SHARED-LEXEMES:** `въ огнищанине, въ тивоунице, въ мечници 12 гривъне / аже огнищанина мучить, 12 гривенъ продаже, за муку гривна`
- **TEXT-SHORT:**
  > «А въ гнищанине, и в тивоунице, и въ мечници 12 гривъне.»
- **TEXT-EXP:**
  > «Аже огнищанина мучить, то 12 гривенъ продаже, а за муку гривна.»
- **STRUCTURAL-DIFFERENCE:** У Короткій 12 гривень за образу/катування вогнищанина, тіуна чи мечника; у Просторій деталізовано як 12 гривень продажі та гривна за муку.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-052
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-033A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-065A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `boundary violation penalty`
- **SHARED-LEXEMES:** `межоу переореть либо перетесъ, за обидоу 12 гривне / межю перетнеть, разореть, 12 гривенъ продажи`
- **TEXT-SHORT:**
  > «А иже межоу переореть либо перетесъ, то за обидоу 12 гривне.»
- **TEXT-EXP:**
  > «Аже межю перетнеть бортьную, или ролеиную разореть, или дворную тыномь перегородить межю, то 12 гривенъ продажи.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 12 гривень за пошкодження межі (ролейної, бортної чи двірної).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-053
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-034A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-073A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `boat theft penalty`
- **SHARED-LEXEMES:** `лодью оукрадеть, за лодью платити 30 резанъ, а продажи 60 резанъ / 60 кунъ продаже, лодию лицемь воротити, морьскую 3 гривны`
- **TEXT-SHORT:**
  > «А оже лодью оукрадеть, то за лодью платити 30 резанъ, а продажи 60 резанъ.»
- **TEXT-EXP:**
  > «Аже лодью оукрадеть, то 60 кунъ продаже, а лодию лицемь воротити; а морьскую лодью 3 гривны, а за набоиную лодью 2 гривны, за челнъ 20 кунъ, а за стругъ гривна.»
- **STRUCTURAL-DIFFERENCE:** У Короткій 30 різан за лодь і 60 різан продажі; у Просторій 60 кун продажі князю, повернення лоді обличчям та градація (морська 3 гривни, набійна 2 гривни, човен 20 кун, струг гривна).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-054
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-035A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-076A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `bird theft tariff`
- **SHARED-LEXEMES:** `въ голоубе и въ коуряти 9 коунъ / за голубь 9 кунъ, за куря 9 кунъ`
- **TEXT-SHORT:**
  > «А въ голоубе и въ коуряти 9 коунъ.»
- **TEXT-EXP:**
  > «А за голубь 9 кунъ, а за куря 9 кунъ, а за оутовь 30 кунъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 9 кун за голуба і курку.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-055
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-036A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-077A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `waterfowl theft tariff`
- **SHARED-LEXEMES:** `въ оутке, въ гоусе, въ жераве, въ лебеди 30 резанъ, продажи 60 резанъ / за гусь 30 кунъ, за лебедь 30 кунъ, за жеравль 30 кунъ`
- **TEXT-SHORT:**
  > «А въ оутке, и въ гоусе, и въ жераве, и въ лебеди 30 резанъ; а продажи 60 резанъ.»
- **TEXT-EXP:**
  > «А за гусь 30 кунъ, а за лебедь 30 кунъ, а за жеравль 30 кунъ.»
- **STRUCTURAL-DIFFERENCE:** Платіж 30 кун/різан за птицю зберігається.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-056
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-037A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-075A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `hunting dog/bird theft`
- **SHARED-LEXEMES:** `чюжь песъ, ястребъ, соколъ, за обидоу 3 гривны / ястрябъ или соколъ продаже 3 гривны, а господину гривна`
- **TEXT-SHORT:**
  > «А оже оукрадоуть чюжь песъ, любо ястребъ, любо соколъ, то за обидоу 3 гривны.»
- **TEXT-EXP:**
  > «Аже кто оукрадеть въ чьемь перевесе ястрябъ или соколъ, то продаже 3 гривны, а господину гривна.»
- **STRUCTURAL-DIFFERENCE:** У Короткій 3 гривні за обиду за пса, яструба чи сокола; у Просторій 3 гривні продажі та гривна господину.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-057
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-038A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-036A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `killing thief at night`
- **SHARED-LEXEMES:** `оубьють татя на своемъ дворе, оу клети, оу хлева то тои оубитъ / оубиють во пса место`
- **TEXT-SHORT:**
  > «Аще оубьють татя на своемъ дворе, любо оу клети, или оу хлева, то тои оубитъ;»
- **TEXT-EXP:**
  > «Аже оубиють кого оу клети или оу которое татбы, то оубиють во пса место;»
- **STRUCTURAL-DIFFERENCE:** Тотожне визнання законним убивства нічного злодія на місці вчинення злочину.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-058
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-038B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-036B`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `bringing thief at dawn`
- **SHARED-LEXEMES:** `до света держать, то вести его на княжь дворъ / додержать света, вести на княжь дворъ`
- **TEXT-SHORT:**
  > «аще ли до света держать, то вести его на княжь двор;»
- **TEXT-EXP:**
  > «аже ли и додержать света, то вести на княжь дворъ; оже ли оубиють и, а оуже боудуть людие связана видели, то платити в томь 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний припис вести злодія на княжий двір, якщо затримано живим до світанку.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-059
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-038C`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-036B`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `killing tied thief`
- **SHARED-LEXEMES:** `оже оубьють а люди боудоуть видели связанъ то платити в немь / платити в томь 12 гривенъ`
- **TEXT-SHORT:**
  > «а оже ли оубьють, а люди боудоуть видели связанъ, то платити в немь.»
- **TEXT-EXP:**
  > «аже ли и додержать света, то вести на княжь дворъ; оже ли оубиють и, а оуже боудуть людие связана видели, то платити в томь 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** У Короткій «платити в немь» (за голову); у Просторій зафіксовано точний платіж 12 гривень.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-060
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-039A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-078A`
- **MATCH-TYPE:** `IDENTICAL`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `hay/wood theft`
- **SHARED-LEXEMES:** `сено крадоуть 9 коунъ, въ дровехъ 9 коунъ / въ сене и въ дровехъ 9 кунъ`
- **TEXT-SHORT:**
  > «Оже сено крадоуть, то 9 коунъ; а въ дровехъ 9 коунъ.»
- **TEXT-EXP:**
  > «А въ сене и въ дровехъ 9 кунъ, а господину колико боудеть возъ оукрадено, то имати ему за возъ по 2 ногате.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 9 кун за крадіжку сіна чи дров; у Просторій додано плату по 2 ногати за віз господину.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-061
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-040A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-038A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `small livestock theft`
- **SHARED-LEXEMES:** `оукрадоуть овъцоу, козоу, свинью, 10 оукрале по 60 резанъ продажи / скотъ на поли овце козы свиньи 60 кунъ, будеть их много то всемъ по 60`
- **TEXT-SHORT:**
  > «Аже оукрадоуть овъцоу или козоу, или свинью, а ихъ боудеть 10 одиноу овьцоу оукрале, да положать по 60 резанъ продажи;»
- **TEXT-EXP:**
  > «Аже крадеть скотъ на поли, или овце, или козы, ли свиньи, 60 кунъ; будеть ли ихъ много, то всемъ по 60 кунъ.»
- **STRUCTURAL-DIFFERENCE:** Тотожний тариф 60 різан/кун продажі з кожного співучасника крадіжки дрібної худоби.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-062
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-040B`
- **SOURCE-EXP-CLAIM:** `NONE`
- **MATCH-TYPE:** `OMITTED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `thief catcher reward`
- **SHARED-LEXEMES:** `а хто изималъ, томоу 10 резанъ`
- **TEXT-SHORT:**
  > «а хто изималъ, томоу 10 резанъ.»
- **TEXT-EXP:**
  > NONE
- **STRUCTURAL-DIFFERENCE:** Платіж тому, хто затримав злодія (10 різан), відсутня у відповідній статті Простої редакції.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-063
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-041A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-082A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `MEDIUM`
- **MATCH-BASIS:** `court fee distribution`
- **SHARED-LEXEMES:** `от гривни мечникоу коуна, в десятиноу 15 коунъ, князю 3 гривны / железного платити 40 кунъ, мечнику 5 кунъ`
- **TEXT-SHORT:**
  > «А от гривни мечникоу коуна, а в десятиноу 15 коунъ, а князю 3 гривны;»
- **TEXT-EXP:**
  > «А железного платити 40 кунъ, а мечнику 5 кунъ, а пол гривны детьскому; то ти железныи оурокъ, кто си в чемь емлеть.»
- **STRUCTURAL-DIFFERENCE:** Розподіл судових зборів між князем, мечником та десятиною; у Просторій перероблено на залізний урок та наклади.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-064
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-041B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-067A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `MEDIUM`
- **MATCH-BASIS:** `court fee from 12 grivnas`
- **SHARED-LEXEMES:** `от 12 гривноу емъцю 70 коунъ, в десятину 2 гривне, князю 10 гривенъ / наклады 12 гривенъ, отроку 2 гривны и 20 кунъ, писцю 10 кунъ`
- **TEXT-SHORT:**
  > «а от 12 гривноу емъцю 70 коунъ, а в десятину 2 гривне, а князю 10 гривенъ.»
- **TEXT-EXP:**
  > «А се наклады: 12 гривенъ, отроку 2 гривны и 20 кунъ, а самому ехати со отрокомь на дву коню; сути же на ротъ овесъ, а мясо дати овенъ любо полоть, а инемь кормомь, что има черево возметь, писцю 10 кунъ, перекладнаго 5 кунъ, на мехъ две ногате.»
- **STRUCTURAL-DIFFERENCE:** Розподіл збору від 12 гривень продажі перероблено в Просторій у систему накладів (ст. 67).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-065
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-042A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-007A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `virnik rations table`
- **SHARED-LEXEMES:** `вирникоу взяти 7 ведоръ солодоу, овенъ, полотъ, две ногате, сыры, куры, 4 коне овесъ / вирнику взяти 7 ведеръ солоду, овенъ, куна же сыръ, куръ по двою`
- **TEXT-SHORT:**
  > «А се поклонъ вирныи: вирникоу взяти 7 ведоръ солодоу на неделю, тъже овенъ любо полотъ, или две ногате; а въ средоу резаноу, въже сыры, в пятницоу тако же; а хлеба по колькоу моугоуть ясти, и пшена; а куръ по двое на день; коне 4 поставити и соути имъ на ротъ, колько могоуть зобати;»
- **TEXT-EXP:**
  > «А се покони вирнии были при Ярославе: вирнику взяти 7 ведеръ солоду на неделю, же овенъ, любо полоть, любо 2 ногате; а в середу куна же сыръ, а в пятницю тако же; а куръ по двою ему на день; а хлебовъ 7 на неделю; а пшена 7 оуборковъ, а гороху 7 оуборковъ, а соли 7 голважень; то то вирнику со отрокомь; а кони 4, конемъ на ротъ сути овесъ; вирнику 8 гривенъ, а 10 кунъ перекладная, а метелнику 12 векшии, а съсадная гривна.»
- **STRUCTURAL-DIFFERENCE:** Майже дослівний збіг раціону утримання вірника (поклон вірний при Ярославі).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-066
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-042B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-007A`
- **MATCH-TYPE:** `MODIFIED-TARIFF`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `virnik money fee`
- **SHARED-LEXEMES:** `вирникоу 60 гривенъ и 10 резанъ и 12 веверици, переде гривна, в говение за рыбы 7 резанъ / вирнику 8 гривенъ а 10 кунъ перекладная, съсадная гривна`
- **TEXT-SHORT:**
  > «а вирникоу 60 гривенъ и 10 резанъ и 12 веверици; а переде гривна; или ся пригоди в говение рьбами, то взяти за рыбы 7 резанъ; тъ всехъ коунъ 15 коунъ на неделю, а борошна колько могоуть изъясти; до недели же вироу сбероуть вирници; то ти оурокъ Ярославль.»
- **TEXT-EXP:**
  > «А се покони вирнии были при Ярославе: вирнику взяти 7 ведеръ солоду на неделю, же овенъ, любо полоть, любо 2 ногате; а в середу куна же сыръ, а в пятницю тако же; а куръ по двою ему на день; а хлебовъ 7 на неделю; а пшена 7 оуборковъ, а гороху 7 оуборковъ, а соли 7 голважень; то то вирнику со отрокомь; а кони 4, конемъ на ротъ сути овесъ; вирнику 8 гривенъ, а 10 кунъ перекладная, а метелнику 12 векшии, а съсадная гривна.»
- **STRUCTURAL-DIFFERENCE:** Грошовий збір вірника: у Короткій зафіксовано сукупний обсяг («60 гривенъ и 10 резанъ и 12 веверици»), у Просторій реформовано на 8 гривень (при 40-гривневій вирі) та 16 гривень (при 80-гривневій).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-067
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-043A`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-091A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `bridge master fee`
- **SHARED-LEXEMES:** `урокъ мостьниковъ, помостивше мостъ взяти от дела ногата, от городници ногата / мостнику оуроци: помостивше мостъ взяти от 10 локотъ по ногате`
- **TEXT-SHORT:**
  > «А се оурокъ мостьниковъ: аще помостивше мостъ, взяти от дела ногата, а от городници ногата;»
- **TEXT-EXP:**
  > «А се мостнику оуроци: помостивше мостъ, взяти oò 10 локотъ по ногате; аже починить моста ветхаго, то колико городне починить, то взяти ему по куне от городне; а мостнику самому ехати со отрокомь на дву коню, 4 лукна овса на неделю, а есть, что можеть.»
- **STRUCTURAL-DIFFERENCE:** Оплата праці мостників за будівництво нового мосту: заміна обліку від городниці на облік від 10 ліктів мосту.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-068
- **SOURCE-SHORT-CLAIM:** `HC-RP-SHORT-043B`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-091A`
- **MATCH-TYPE:** `MODIFIED-WORDING`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `bridge master repair fee`
- **SHARED-LEXEMES:** `ветхаго моста подтвердити неколико доскъ 3, 4 или 5 то тое же / починивше мостъ колико городниць, то взяти по ногате`
- **TEXT-SHORT:**
  > «аще же боудеть ветхаго моста подтвердити неколико доскъ, или 3, или 4, или 5, то тое же.»
- **TEXT-EXP:**
  > «А се мостнику оуроци: помостивше мостъ, взяти oò 10 локотъ по ногате; аже починить моста ветхаго, то колико городне починить, то взяти ему по куне от городне; а мостнику самому ехати со отрокомь на дву коню, 4 лукна овса на неделю, а есть, что можеть.»
- **STRUCTURAL-DIFFERENCE:** Оплата за ремонт старого моста збережена в обох редакціях.
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-069
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-002A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «По Ярославе же паки совкупившеся сынове его: Изяславъ, Святославъ, Всеволодъ и мужи ихъ: Коснячько, Перенегъ, Никифоръ, и отложиша оубиение за голову, но кунами ся выкупати;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 2).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-070
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-002B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «а ино все якоже Ярославъ судилъ, такоже и сынове его оуставиша.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 2).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-071
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-003B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «паки ли людинъ, то 40 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 3).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-072
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-004A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Которая ли вервь начнеть платити дикую веру, колико летъ заплатить ту виру, зане же безъ головника имъ платити.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 4).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-073
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-004B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Будеть ли головникъ ихъ въ верви, то зань к нимъ прикладываеть, того же деля имъ помагати головникоу, любо си дикую веру; но сплати имъ во обчи 40 гривенъ, а головничьство самому головнику; а въ 40 гривенъ ему заплатити ис дружины свою часть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 4).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-074
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-004C`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Но оже будеть оубилъ или въ сваде или в пиру явлено, то тако ему платити по верви ныне, иже ся прикладывають вирою.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 4).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-075
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-005A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Будеть ли сталъ на разбои безъ всякоя свады, то за разбоиника люди не платять, но выдадять и всего съ женою и с детми на потокъ и на разграбление.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 5).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-076
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-006A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто не вложиться в дикую веру, тому людье не помогають, но самъ платить.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 6).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-077
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-008A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будеть вира во 80 гривенъ, то вирнику 16 гривенъ и 10 кунъ и 12 векши, а переди съсадная гривна, а за голову 3 гривны.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 8).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-078
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-009A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже въ княжи отроци, или в конюсе, или в поваре, то 40 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 9).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-079
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-012A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А за ремественика и за ремественицю, то 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 12).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-080
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-015A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аще будеть на кого поклепная вира, то же будеть послухов 7, то ти выведуть виру; паки ли варягъ или кто инъ, тогда.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 15).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-081
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-015B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А по костехъ и по мертвеци не платить верви, аже имене не ведають, ни знають его.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 15).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-082
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-016A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А иже свержеть виру, то гривна кунъ сметная отроку; а кто и клепалъ, а тому дати другую гривну; а от виры помечнаго 9.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 16).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-083
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-017A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Искавше ли послуха, не налезуть, а истьця начнеть головою клепати, то имъ правду железо.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 17).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-084
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-017B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Тако же и во всех тяжахъ, в татбе и в поклепе; оже не будеть лиця, то тогда дати ему железо из неволи до полугривны золота; аже ли мне то на воду, оли то до дву гривенъ; аже мене, то роте ему ити по свое куны.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 17).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-085
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-023C`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «аче же и кровавъ придеть, или будеть самъ почалъ, а вылезуть послуси, то то ему за платежь, оже и били.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 23).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-086
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-029B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «сведитеся, кто будеть виноватъ, на того татба снидеть, тогда онъ свое возметь, а что погибло боудеть с нимь, то же ему начнеть платити.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 29).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-087
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-030A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аще будеть коневыи тать, выдати князю на потокъ;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 30).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-088
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-030B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «паки ли боудеть клетныи тать, то 3 гривны платити емоу.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 30).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-089
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-031B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «будеть ли сводъ по землямъ, то ити ему до третьяго свода; а что будеть лице, то тому платити третьему кунами за лице; а с лицемь ити до конця своду, а истьцю ждати прока; а кде снидеть на конечняго, то тому все платити и продажю.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 31).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-090
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-032A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Паки ли будеть что татебно купилъ в торгу, или конь, или портъ, или скотину, то выведеть свободна мужа два или мытника; аже начнеть не знати, оу кого купилъ, то ити по немь темъ видокомъ на роту, а истьцю свое лице взяти; а что с нимь погибло, а того ему желети, а оному желети своихъ кунъ, зане не знаеть оу кого купивъ;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 32).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-091
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-032B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «познаеть ли на долзе оу кого то купилъ, то свое куны возметь, и сему платити, что оу него будеть погибло, а князю продажю.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 32).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-092
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-034A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А князю продаже 12 гривенъ в челядине или оукрадше.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 34).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-093
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-035A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А и своего города в чюжю землю свода нетуть, но тако же вывести ему послухи, любо мытника, передъ кимь же купивше, то истьцю лице взяти, а прока ему желети, что с нимь погибло, а оному своих кунъ желети.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 35).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-094
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-039A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже крадеть гумно или жито въ яме, то колико ихъ будеть крало, то всемъ по 3 гривны и по 30 кунъ;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 39).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-095
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-039B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «а оу него же погибло, то оже будеть лице, лице поиметь; а за лето возметь по полугривне, паки ли лиця не будетъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 39).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-096
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-041B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «а за жеребець, аже не вседано на нь, гривна кунъ, за жеребя 6 ногатъ, а за коровие молоко 6 ногатъ; то ти оуроци смердомъ, оже платять князю продажю.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 41).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-097
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-042A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будуть холопи татие любо княжи, любо боярьстии, любо чернечь, их же князь продажею не казнить, зане суть несвободни, то двоиче платить ко истьцю за обидоу.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 42).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-098
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-043A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто взищеть кунъ на друзе, а онъ ся начнеть запирати, то оже на нь выведеть послуси, то ти поидуть на роту, а онъ возметь свое куны; зане же не далъ ему кунъ за много летъ, то платити ему за обиду 3 гривны.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 43).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-099
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-044A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто купець купцю дасть куплю в куны или в гостьбу, то купцю пред послухи кунъ не имати, послуси ему не надобе, но ити ему самому роте, аже ся почнеть запирати.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 44).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-100
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-045A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто поклажаи кладеть оу кого любо, то ту послуха нетуть; но оже начнеть большимь клепати, тому ити роте оу кого то лежалъ товаръ: а толко еси оу мене положилъ зане же ему въ бологоделъ и хоронилъ товаръ того.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 45).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-101
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-046A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто даеть куны в резъ, или наставъ в медъ, или жито во просопъ, то послухи ему ставити, како ся будеть рядилъ, тако же ему имати.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 46).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-102
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-047A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «О месячныи резъ, оже за мало, то имати ему; заидуть ли ся куны до того же года, то дадять ему куны въ треть, а месячныи резъ погренути. Послуховъ ли не будеть, а будеть кунъ 3 гривны, то ити ему про свое куны роте; будеть ли боле кунъ, то речи ему тако: промиловался еси, оже еси не ставил послуховъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 47).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-103
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-048A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Володимерь Всеволодичь, по Святополце, созва дружину свою на Берестовемь: Ратибора Киевьского тысячьского, Прокопью Белогородьского тысячьского, Станислава Переяславьского тысячьского, Нажира, Мирослава, Иванка Чюдиновича Олгова мужа, и оуставили до третьяго реза, оже емлеть въ треть куны; аже кто возметь два реза, то то ему исто; паки ли возметь три резы, то иста ему не взяти.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 48).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-104
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-049A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто емлеть по 10 кунъ от лета на гривну, то того не отметати.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 49).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-105
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-049B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто емлеть по 10 кунъ от лета на гривну, то того не отметати.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 49).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-106
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-050A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже которыи купець, кде любо шедъ съ чюжими кунами, истопиться любо рать возметь, ли огнь, то не насилити ему, ни продати его; но како начнеть от лета платити, тако же платить, зане же пагуба от бога есть, а не виноватъ есть;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 50).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-107
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-050B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «аже ли пропиеться или пробиеться, а в безумьи чюжь товаръ испортить, то како любо темъ, чии то товаръ, ждуть ли ему, а своя имъ воля, продадять ли, а своя имъ воля.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 50).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-108
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-051A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто многимъ долженъ будеть, а пришедъ господь изъ иного города или чюжеземець, а не ведая запустить за нь товаръ, а опять начнеть не дати гости кунъ, а первии должебити начнуть ему запинати, не дадуче ему кунъ, то вести и на торгъ, продати же и отдати же первое гостины коуны, а домашнимъ, что ся останеть кунъ, тем же ся поделять;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 51).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-109
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-051B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «паки ли будуть княжи куны, то княжи куны первое взяти, а прокъ в делъ; аже кто много реза ималъ, не имати тому.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 51).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-110
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-052A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже закупъ бежить от господы, то обель;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 52).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-111
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-052B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «идеть ли искатъ кунъ, а явлено ходить, или ко князю или къ судиямъ бежить обиды деля своего господина, то про то не робять его, но дати емоу правдоу.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 52).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-112
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-053A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже оу господина ролеиныи закупъ, а погубить воискии конь, то не платити ему; но еже далъ ему господинъ плугъ и борону, от него же купу емлеть, то то погубивше платити;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 53).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-113
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-053B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «аже ли господинъ его отслеть на свое орудье, а погибнеть без него, то того ему не платити.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 53).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-114
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-054A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже изъ хлева выведуть, то закупу того не платити; но оже погубить на поли, и въ дворъ не вженеть и не затворить, кде ему господинъ велить, или орудья своя дея, а того погубить, то то ему платити.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 54).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-115
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-055A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже господинъ переобидить закоупа, а оувидить купу его или отарицю, то то ему все воротити, а за обиду платити ему 60 кунъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 55).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-116
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-055B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Паки ли прииметь на немь кунъ, то опять ему воротити куны, что будеть принялъ, а за обиду платити ему 3 гривны продажи.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 55).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-117
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-055C`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Продасть ли господинъ закупа обель, то наимиту свобода во всехъ кунахъ, а господину за обиду платити 12 гривенъ продаже.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 55).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-118
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-055D`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже господинъ бьеть закупа про дело, то без вины есть; биеть ли не смысля пьянъ, а без вины, то яко же въ свободнемь платежь, такоже и в закупе.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 55).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-119
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-056A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже холопъ обелныи выведеть конь чии любо, то платити за нь 2 гривны.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 56).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-120
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-057A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже закупъ выведеть что, то господинъ в немь; но оже кде и налезуть, то преди заплатить господинъ его конь или что будеть ино взялъ, ему холопъ обелныи;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 57).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-121
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-057B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «и паки ли господинъ не хотети начнеть платити за нь, а продасть и, отдасть же переди или за конь, или за волъ или за товаръ, что будеть чюжего взялъ, а прокъ ему самому взяти собе.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 57).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-122
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-059A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А послушьства на холопа не складають, но оже не будеть свободнаго, но по нужи сложити на боярьска тивуна, а на инехъ не складывати. А в мале тяже по нужи възложити на закупа.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 59).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-123
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-061A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже выбьють зубъ, а кровь видять оу него во рте, а людье вылезуть, то 12 гривенъ продаже, а за зубъ гривна.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 61).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-124
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-062A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже оукрадеть кто бобръ, то 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 62).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-125
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-063A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будеть росечена земля или знамение, им же ловлено, или сеть, то по верви искати татя ли платити продажю.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 63).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-126
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-064A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже разнаменаеть борть, то 12 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 64).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-127
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-066A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже дубъ подотнеть знаменьныи или межьныи, то 12 гривенъ продаже.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 66).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-128
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-069A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже пчелы выдереть, то 3 гривны продаже, а за медъ, аже будеть пчелы не лажены, то 10 кунъ; будеть ли олекъ, то 5 кунъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 69).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-129
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-070A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Не будеть ли татя, то по следу женуть, аже не боудеть следа ли к селу или к товару, а не отсочать от собе следа, ни едуть на следъ или отбьются, то темь платати татбу и продажю; а следъ гнати с чюжими людми, а с послухи;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 70).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-130
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-070B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «аже погубять следъ на гостиньце на велице, а села не будеть, или на пусте, кде же не будеть ни села, ни людии, то не платити ни продажи, ни татбы.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 70).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-131
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-074A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто подотнеть вервь в перевесе, то 3 гривны продажи, а господину за вервь гривна кунъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 74).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-132
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-079A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже зажгуть гумно, то на потокъ, на грабежь домъ его, переди пагубу исплатившю, а въ проце князю поточити и; тако же, аже кто дворъ зажьжеть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 79).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-133
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-080A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А кто пакощами конь порежеть или скотину, продаже 12 гривенъ, а пагубу господину оурокъ платити.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 80).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-134
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-081A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Ты тяже все судять послухи свободными, будеть ли послухъ холопъ, то холопу на правду не вылазити;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 81).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-135
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-081B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «но оже хощеть истець, или иметь и, а река тако: по сего речи емлю тя, но азъ емлю тя, а не холопъ, и емети и на железо; аже обинити и, то емлеть на немь свое; не обинить ли его, платити ему гривна за муку, зане по холопьи речи ялъ и.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 81).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-136
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-082B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже иметь на железо по свободныхъ людии речи, либо ли запа на нь будеть, любо прохожение нощное, или кимь любо образомь аже не ожьжеться, то про муки не платити ему, но одино железное, кто и будеть ялъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 82).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-137
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-083A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто оубиеть жену, то темь же судомь судити, яко же и мужа аже будеть виноватъ (а), то пол виры 20 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 83).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-138
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-084A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А в холопе и в робе виры нетуть; но оже будеть безъ вины оубиенъ, то за холопъ оукоръ (а) платити или за робу, а князю 12 гривен продаже.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 84).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-139
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-085A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже смердъ оумреть, то задницю князю; аже будуть дщери оу него дома, то даяти часть на не; аже будуть за мужемь, то не даяти части имъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 85).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-140
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-086A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже в боярехъ любо въ дружине, то за князя задниця не идеть; но оже не будеть сыновъ, а дчери возмуть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 86).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-141
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-087A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто оумирая разделить домъ свои детемъ, на том же стояти; паки ли безъ ряду оумреть, то всемъ детемъ, а на самого часть дати души.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 87).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-142
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-088A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже жена сядеть по мужи, то на ню часть дати; а что на ню мужь възложить, тому же есть госпожа, а задниця еи мужня не надобе.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 88).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-143
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-088B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Будуть ли дети, то что первое жены, то то возмуть дети матере своея; любо си на женоу будеть възложилъ, обаче матери своеи возмуть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 88).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-144
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-089A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будеть сестра в домоу, то тои заднице не имати, но отдадять ю за мужь братия, како си могуть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 89).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-145
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-090A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А се оуроци городнику: закладаюче городню, куну взяти, а кончавше ногата; а за кормъ, и за вологу, и за мяса, и за рыбы 7 кунъ на неделю, 7 хлебовъ, 7 оуборковъ пшена, 7 луконъ овса на 4 кони: имати же ему, донеле городъ срубять, а солоду одину дадять 10 луконъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 90).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-146
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-092A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будуть робьи дети оу мужа, то задници имъ не имати, но свобода имъ смертию.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 92).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-147
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-093A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будуть в дому дети мали, а не джи ся будуть сами собою печаловати, а мати имъ поидеть за мужь, то кто имъ ближии будеть, тому же дати на руце и с добыткомь и с домомь, донеле же возмогуть; а товаръ дати перед людми;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 93).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-148
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-093B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «а что срезить товаромь темь ли пригостить, то то ему собе, а истыи товаръ воротить имъ, а прикупъ ему собе, зане кормилъ и печаловалъся ими; яже от челяди плод или от скота, то то все поимати лицемь; что ли будеть ростерялъ, то то все ему платити детемъ тем.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 93).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-149
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-094A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аче же и отчимъ прииметь дети cú задницею, то тако же есть рядъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 94).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-150
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-094B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А дворъ без дела отень всякъ меншему сынови.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 94).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-151
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-095A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже жена ворчеться седети по мужи, а ростеряеть добыток и поидеть за мужь, то платити еи все детемъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 95).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-152
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-095B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Не хотети ли начнуть дети еи ни на дворе, а она начнеть всяко хотети и седети, то творити всяко волю, а детемъ не дати воли; но что еи далъ мужь, с тем же еи седети, или, свою часть вземше, седети же.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 95).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-153
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-096A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А матерня часть не надобе детемъ, но кому мати дасть, тому же взяти; дасть ли всемъ, а вси розделять;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 96).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-154
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-096B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «безъ языка ли оумреть, то оу кого будеть на дворе была и кто ю кормилъ, то тому взяти.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 96).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-155
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-097A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже будуть двою мужю дети, а одиное матери, то онемъ своего отця задниця, а онемъ своего.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 97).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-156
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-097B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Будеть ли потерялъ своего иночима что, а онех отця, а оумреть, то възворотить брату, на не же и людье вылезуть, что будеть отець его истерялъ иночимля; а что ему своего отця, то держить.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 97).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-157
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-098A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А матери которыи сынъ добръ, перваго ли, другаго ли, тому же дасть свое; аче и вси сынове еи будуть лиси, а дчери можеть дати, кто ю кормить.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 98).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-158
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-099A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А се оуроци судебнии: от виры 9 кунъ, а метелнику 9 векошь, а от бортное земли 30 кунъ, а о инехъ о всехъ тяжь, кому помогуть, по 4 куны, а метелнику 6 векошь.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 99).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-159
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-100A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже братья ростяжються передъ княземь о задницю, которыи детьскии идеть их делитъ, то тому взяти гривна коунъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 100).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-160
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-101A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А се оуроци ротнии: от головы 30 кунъ, а отъ бортьное земли 30 кунъ бес трии кунъ, тако же и отъ ролеиное земли, а от свободы 9 кунъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 101).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-161
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-102A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Холопьство обелное трое: оже кто хотя купить до полу гривны, а послухи поставить, а ногату дасть перед самемъ холопомь.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 102).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-162
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-103A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А второе холопьство: поиметь робу без ряду, поиметь ли с рядомь, то како ся будеть рядилъ, на том же стоить.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 103).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-163
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-104A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А се третьее холопьство: тивуньство без ряду или привяжеть ключь к собе без ряду, с рядомь ли, то како ся будеть рядилъ, на том же стоить.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 104).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-164
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-105A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «А въ даче не холопъ, ни по хлебе роботять, ни по придатъце; но оже не доходять года, то ворочати ему милость; отходить ли, то не виноватъ есть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 105).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-165
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-106A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже холопъ бежить, а заповесть господинъ, аже слышавъ кто или зная и ведая, оже есть холопъ, а дасть ему хлеба или оукажеть ему путь, то платити ему за холопъ 5 гривенъ, а за робу 6 гривенъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 106).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-166
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-107A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто переиметь чюжъ холопъ и дасть весть господину его, то имати ему переемъ гривна; не оублюдеть ли, то платити ему 4 гривны, а пятая переемная ему;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 107).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-167
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-107B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «а будеть роба, то 5 гривенъ, а шестая на переемъ отходить.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 107).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-168
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-108A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто своего холопа самъ досочиться въ чьемь любо городe, а будеть посадникъ не ведалъ его, то, поведавше ему, пояти же ему отрокъ от него и шедше оувязати и, и дати ему вязебную 10 кунъ, а переима нетуть;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 108).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-169
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-108B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «аче оупустить и гоня, а собе ему пагуба, а платить в то никто же, тем же и переима нетуть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 108).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-170
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-109A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто не ведая чюжь холопъ оусрячеть и, или повесть дееть, любо держить и оу собе, а идеть от него, то ити ему роте, яко не ведалъ есмь, оже есть холопъ, а платежа в томь нетуть.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 109).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-171
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-110A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аче же холопъ кде куны вложить , а онъ будеть не ведая вдалъ, то господину выкупати али лишитися его;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 110).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-172
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-110B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «ведая ли будеть далъ, а кунъ ему лишитися.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 110).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-173
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-111A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже пустить холопъ в торгъ, а одолжаеть, то выкупати его господину и не лишитися его.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 111).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-174
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-112A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто кренеть чюжь холопъ не ведая, то первому господину холопъ поняти, а оному куны имати роте ходивше, яко не ведая есмь купилъ,»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 112).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-175
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-112B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «ведая ли будет купилъ, то кунъ ему лиху быти.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 112).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-176
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-113A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже холопъ бегая будеть добудеть товара, то господину долгъ, господину же и товаръ, а не лишатися его.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 113).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-177
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-114A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже кто бежа, а поиметь суседне что или товаръ, то господину платити за нь оурокъ, что будеть взялъ.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 114).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-178
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-115A`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «Аже холопъ крадеть кого любо, то господину выкупати и любо выдати и, с кимь будеть кралъ, а жене и детемъ не надобе, но оже будуть с нимь крали и хоронили, то всехъ выдати, паки ли а выкупаеть господинъ;»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 115).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`

---

### ALIGN-RP-179
- **SOURCE-SHORT-CLAIM:** `NONE`
- **SOURCE-EXP-CLAIM:** `HC-RP-EXP-115B`
- **MATCH-TYPE:** `ADDED`
- **ALIGNMENT-CONFIDENCE:** `HIGH`
- **MATCH-BASIS:** `independent article in Expanded recension`
- **SHARED-LEXEMES:** `NONE`
- **TEXT-SHORT:**
  > NONE
- **TEXT-EXP:**
  > «аже будуть свободнии с нимь крали или хоронили, то князю въ продаже.»
- **STRUCTURAL-DIFFERENCE:** Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції (Артикул 115).
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **HISTORICAL-INTERPRETATION:** `EMPTY`
