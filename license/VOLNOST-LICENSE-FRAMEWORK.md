# КОНЦЕПТУАЛЬНИЙ ФРЕЙМВОРК ЛІЦЕНЗІЇ ПРАВ І ВОЛЬНОСТЕЙ (VOLNOST-BASED LICENSE FRAMEWORK)

> [!WARNING]
> **STATUS: EXPERIMENTAL / NON-AUTHORITATIVE DRAFT — NOT ADOPTED**
> This document represents an exploratory research draft and has **NOT** been approved, ratified, or adopted by the Project Owner as policy or licensing for any repository in the ecosystem.
> **DO NOT PROPAGATE. DO NOT ENFORCE. LINTER SHALL NOT DEFINE NORMATIVE CONTENT.**
> Methodology in effect: `SOURCE → EXTRACTION → RESEARCH → NORMATIVE`. We are currently at .

## Від історичного синтезу до точних юридичних формулювань

**Status:** DRAFT / PROPOSED FRAMEWORK (PHASE 5)  
**Repository:** `pravda` (`/home/agents/GitHub/pravda`)  
**Parent Methodology:** `HISTORICAL-SYNTHESIS.md` · `WSM-LICENSE-MANIFESTO.md`  
**Epistemic Goal:** Трансформація 4 історичних аксіом у строгі юридичні положення ліцензії, яка поєднує технологічну свободу з категоричною забороною агресії, репресій та цифрового закріпачення.

---

## 1. Архітектурна демаркація та подолання відкритих юридичних дилем

На підставі інструкції для юридичного радника ([`WSM-LICENSE-MANIFESTO.md`](file:///home/agents/GitHub/pravda/license/drafts/WSM-LICENSE-MANIFESTO.md)) та історичного синтезу ([`HISTORICAL-SYNTHESIS.md`](file:///home/agents/GitHub/pravda/HISTORICAL-SYNTHESIS.md)), ліцензія базується на наступних розмежуваннях:

### 1.1. OSI Open Source vs Ethical Source / Source-Available
- **Реальність Open Source Definition (OSD):** Пункт 5 (No Discrimination Against Persons or Groups) та Пункт 6 (No Discrimination Against Fields of Endeavor) критеріїв OSI суворо забороняють обмеження на сфери використання (включно з військовою діяльністю чи агресією). Тому будь-яка ліцензія з етичними/правозахисними обмеженнями формально класифікується не як OSI-approved «Open Source», а як **`Ethical Source`** або **`Source-Available with Invariant Ethical Covenants`**.
- **Архітектурний орієнтир: Модель MPL-2.0 та принцип «не захоплювати сусідів»:** Детально розроблено в [`VOLNOST-COMPATIBILITY-SPEC.md`](file:///home/agents/GitHub/pravda/license/VOLNOST-COMPATIBILITY-SPEC.md). Щоб забезпечити композиційну сумісність із MIT, Apache-2.0, MPL-2.0 та сімейством GPL:
  - Copyleft-вимоги діють суворо на рівні окремих файлів/модулів (`Covered Code`), не інфікуючи сусідній незалежний код у збірці (`Larger Work`).
  - Передбачено шлях до сумісності з GPLv3 через інститут вторинних ліцензій (`Secondary Licenses`).
  - Нормативний Пакт (`PACTA`) не створює несумісних обтяжень для звичайного компілювання чи лінкування коду.

### 1.2. Об'єктивні міжнародні стандарти замість розмитих моральних декларацій
Щоб уникнути суб'єктивного трактування понять «агресія», «репресії» та «права людини», ліцензія спирається виключно на кодифіковані норми міжнародного публічного права:
1. **Злочин агресії (Crime of Aggression):** Стаття 8 bis Римського статуту Міжнародного кримінального суду та Резолюція ГА ООН 3314 (XXIX).
2. **Воєнні злочини та злочини проти людяності:** Статті 7 та 8 Римського статуту МКС; Женевські конвенції 1949 року та Додаткові протоколи до них.
3. **Фундаментальні права людини:** Загальна декларація прав людини (УДПЛ 1948), Міжнародний пакт про громадянські і політичні права (МПГПП 1966), Конвенція проти катувань (CAT 1984).

---

## 2. Структура Ліцензійної угоди (Draft License Structure)

Ліцензія будується за модульним принципом із 6 розділів:

```text
┌─────────────────────────────────────────────────────────────────────────┐
│              VOLNOST ETHICAL PUBLIC LICENSE (ВЕПЛ)                      │
├─────────────────────────────────────────────────────────────────────────┤
│ РОЗДІЛ 1. ВИЗНАЧЕННЯ ТЕРМІНІВ (DEFINITIONS)                             │
│   - Програмне забезпечення, Похідний твір, Користувач, Розповсюдження   │
│   - Нормативні джерела: Римський статут, УДПЛ, МПГПП, Женевські конвенції│
├─────────────────────────────────────────────────────────────────────────┤
│ РОЗДІЛ 2. НАДАННЯ ПРАВ І ВОЛЬНОСТЕЙ (GRANT OF RIGHTS)                   │
│   - Безвідкличне, безоплатне право на виконання, модифікацію, вивчення  │
│   - Повна технологічна симетрія: застосовується однаково до всіх суб'єктів│
├─────────────────────────────────────────────────────────────────────────┤
│ РОЗДІЛ 3. ПАКТ ВОЛЬНОСТЕЙ ТА ОБМЕЖЕННЯ (COVENANT OF LIBERTIES)          │
│   - 3.1. Захист від агресії (Prohibition of Aggressive Warfare)         │
│   - 3.2. Захист від репресій і катувань (Human Rights Covenants)        │
│   - 3.3. Захист від цифрового закріпачення (Anti-Enclosure / Copyleft)   │
│   - 3.4. Захист від ламання прав (Prohibition of Arbitrary Intrusion)   │
├─────────────────────────────────────────────────────────────────────────┤
│ РОЗДІЛ 4. ЛІЦЕНЗІЙНИЙ ІМУНІТЕТ ТА ОБОРОНА (LEGITIMATE SELF-DEFENSE)     │
│   - Право на збройний захист суверенітету, території та цивільного      │
│     населення згідно зі статтею 51 Статуту ООН                          │
├─────────────────────────────────────────────────────────────────────────┤
│ РОЗДІЛ 5. МЕХАНІЗМ ПРИПИНЕННЯ ДІЇ (TERMINATION & DUE PROCESS)           │
│   - Автоматичне припинення ліцензії у разі порушення Розділу 3          │
│   - Механізм виправлення (Cure Period) та незалежний арбітраж           │
├─────────────────────────────────────────────────────────────────────────┤
│ РОЗДІЛ 6. ВІДМОВА ВІД ГАРАНТІЙ ТА ОБМЕЖЕННЯ ВІДПОВІДАЛЬНОСТІ (DISCLAIMER)│
│   - Стандартний захист розробників AS-IS без фінансових зобов'язань     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Точні формулювання ключових статей

### 3.1. Стаття про надання вольностей (Grant of Liberties)
> **2.1. Grant of License.** Author hereby grants to You a perpetual, worldwide, non-exclusive, royalty-free license to use, reproduce, modify, display, perform, sublicense, and distribute the Software, subject to the conditions and limitations of Section 3.  
> **2.2. Universal Symmetry.** The rights granted herein apply equally to natural persons, corporations, non-governmental entities, sovereign states, and armed forces, without discrimination based on nationality, place of origin, or legal form.

### 3.2. Стаття про категоричні заборони (Prohibited Uses)
> **3.1. Prohibition of Unlawful Aggression.** The Software shall not be used, directly or indirectly, to initiate, facilitate, conduct, or support any act or war of aggression as defined under Article 8 bis of the Rome Statute of the International Criminal Court and United Nations General Assembly Resolution 3314 (XXIX).  
> **3.2. Prohibition of Human Rights Violations.** The Software shall not be used to commit, facilitate, or support:  
> (a) War crimes or crimes against humanity (Articles 7 and 8 of the Rome Statute);  
> (b) Extrajudicial killings, enforced disappearances, or torture (UN Convention Against Torture);  
> (c) Systematic, arbitrary surveillance or discrimination violating Articles 12, 18, 19, or 21 of the Universal Declaration of Human Rights.  
> **3.3. Prohibition of Digital Enclosure (Anti-Enclosure Clause).** Recipients of the Software or derivative works shall not restrict the exercise of the liberties granted herein through technological protection measures (DRM), proprietary compilation obscuration, or unconscionable contractual lock-ins.

### 3.3. Стаття про законну оборону (Legitimate Defense Safe Harbor)
> **4.1. Inherent Right of Individual and Collective Self-Defense.** Nothing in Section 3 shall be construed to prohibit, restrict, or impair the use of the Software for the legitimate defense of sovereign territory, critical civilian infrastructure, public health, cybersecurity, or civilian life against unlawful military invasion or armed attack, in full compliance with Article 51 of the Charter of the United Nations and the customary laws of armed conflict.

### 3.4. Стаття про припинення дії та арбітраж (Due Process Termination)
> **5.1. Automatic Suspension.** Any use of the Software in violation of Section 3 immediately and automatically suspends all licenses and rights granted to the breaching party.  
> **5.2. Opportunity to Cure and Determination.** A license suspended under Section 5.1 shall be permanently terminated unless the breaching party cures the violation within 30 days of receipt of formal notice, or establishes through competent international judicial determination (ICJ, ICC, or recognised arbitration tribunal) that no violation of Section 3 occurred.

---

## 4. Відповіді на юридичні питання з Маніфесту

1. **Як юридично визначити агресію та воєнні злочини?**
   - Через пряму ліцензійну інкорпорацію Римського статуту МКС (Articles 7, 8, 8 bis) та Резолюцій ООН. Це усуває суб'єктивізм: діяння оцінюється за конвенційним критерієм міжнародного права.
2. **Як бути зі старими MIT-ліцензіями в історії репозиторіїв?**
   - Історичні коміти під MIT залишаються під MIT (неможливо відкликати вже видану ліцензію на минулі версії). Проте нові релізи, мажорні оновлення, нова кодова база чи форки легітимно переходять на нову ліцензію автора з моменту її оголошення.
3. **Як реалізувати модель Dual Licensing?**
   - Відкрита версія поширюється за цією ліцензією (Volnost Ethical License). Для комерційних корпорацій чи урядів, які вимагають специфічних гарантій або аудиту сумісності, пропонується комерційна угода (Commercial Proprietary License), умови якої, однак, не можуть скасовувати базових антиагресивних ковенантів.

---

## 5. Дорожня карта фіналізації ліцензії

1. **Обговорення проєкту:** Узгодження формулювань ліцензії з власником екосистеми.
2. **Юридична верифікація:** Підготовка тексту для зовнішньої правової експертизи (право інтелектуальної власності + міжнародне публічне право).
3. **Публікація офіційного драфту:** Розміщення тексту у `license/VOLNOST-LICENSE-1.0.md` та синхронізація з екосистемою.
