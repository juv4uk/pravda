# ДОСЬЄ 08a: ЕМПІРИЧНА ДЕКОМПОЗИЦІЯ СУЧАСНИХ ЛІЦЕНЗІЙ НА СПОСТЕРЕЖУВАНІ ОПЕРАТОРИ
## Рівень спостереження: без нормативних або історичних інтерпретацій

> **Методологічне правило:** Рівень спостереження (observational layer) не повинен містити слів `libertas`, `confirmatio`, `pactum`, `reciprocity`, `вольність` тощо. Кожна операція фіксується як формальна зв'язка параметрів:
> ```text
> OPERATOR
> ├── ACTOR        (Хто діє)
> ├── ACTION       (Що робить)
> ├── OBJECT       (Щодо якого матеріалу)
> ├── TRIGGER      (Яка подія запускає дію або обов'язок)
> ├── RECIPIENT    (Кому спрямована дія)
> ├── CONDITION    (Які умови чинності)
> ├── PROHIBITION  (Що прямо заборонено)
> ├── CONSEQUENCE  (Що відбувається при виході за межі)
> └── EXACT CLAUSE (Точна автентична цитата з офіційного тексту)
> ```

---

### 1. ДОКУМЕНТАЛЬНІ СВІДКИ (WITNESS CORPUS)

1. **MIT License** (Open Source Initiative text, 1988/current).
2. **Apache License, Version 2.0** (Apache Software Foundation, January 2004).
3. **Mozilla Public License, Version 2.0** (Mozilla Foundation, 2012).
4. **GNU General Public License, Version 3** (Free Software Foundation, 29 June 2007).
5. **GNU Affero General Public License, Version 3** (Free Software Foundation, 19 November 2007).
6. **Контрольний свідок (Proprietary EULA):**  
   **Microsoft Software License Terms: Windows Operating System** (Версія від травня 2021 р., pre-installed / retail Windows 10/11).

---

### 2. КАТАЛОГ СПОСТЕРЕЖУВАНИХ ОПЕРАТОРІВ (OBSERVED OPERATORS)

```text
A. НАДАННЯ ТА ДОЗВОЛИ
   ├── OP-PERMIT                   (дозвіл діяти в межах монополії копірайту)
   ├── OP-GRANT                    (явне наділення вичерпним переліком прав)
   └── OP-PATENT-GRANT             (наділення патентною ліцензією)

B. УМОВИ ТА ЗБЕРЕЖЕННЯ ІДЕНТИЧНОСТІ
   ├── OP-CONDITION                (загальна залежність прав від дотримання вимог)
   └── OP-NOTICE                   (вимога збереження авторських та ліцензійних повідомлень)

C. ПЕРЕДАЧА, ВИХІДНИЙ КОД ТА ЗВ'ЯЗАНІСТЬ НАСТУПНИКІВ
   ├── OP-SOURCE-PROVISION         (вимога надати або відкрити вихідний код)
   ├── OP-SAME-TERMS               (вимога поширювати похідні/модифіковані форми під тією самою ліцензією)
   ├── OP-DIRECT-GRANT             (пряме виникнення ліцензійного зв'язку між автором і кінцевим реципієнтом)
   └── OP-NO-FURTHER-RESTRICTIONS  (заборона для посередника додавати обтяження чи звужувати права реципієнта)

D. ПАТЕНТНИЙ ЗАХИСТ ТА КОНФЛІКТ
   └── OP-PATENT-RETALIATION       (скасування патентних/копірайтних прав при ініціюванні патентного позову)

E. ПРИПИНЕННЯ ТА ВІДНОВЛЕННЯ
   ├── OP-TERMINATE                (автоматичне або одностороннє припинення дії ліцензії)
   ├── OP-CURE                     (пільговий строк на усунення порушення)
   └── OP-REINSTATE                (відновлення чинності прав після усунення порушення)

F. ВІДМОВА ВІД ГАРАНТІЙ ТА ВІДПОВІДАЛЬНОСТІ
   ├── OP-DISCLAIM                 (повне заперечення наявності гарантій якості)
   └── OP-LIMIT-LIABILITY          (обмеження або виключення цивільної відповідальності за збитки)
```

---

### 3. ПООПЕРАТОРНИЙ РОЗБІР СВІДКІВ (WITH EXACT CLAUSES)

#### 3.1. OP-PERMIT & OP-GRANT (Надання правомочностей)

- **MIT:**
  - `ACTOR`: Any person obtaining a copy.
  - `ACTION`: deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies.
  - `OBJECT`: Software and associated documentation files.
  - `TRIGGER`: Obtaining a copy of the Software.
  - `EXACT CLAUSE`: *«Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files... to deal in the Software without restriction...»*

- **Apache-2.0 (§2):**
  - `ACTOR`: Each Contributor.
  - `ACTION`: grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.
  - `OBJECT`: The Work and Derivative Works.
  - `EXACT CLAUSE`: *«Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license...»*

- **MPL-2.0 (§2.1):**
  - `ACTOR`: Each Contributor.
  - `ACTION`: grants You a world-wide, royalty-free, non-exclusive license to use, reproduce, make available, modify, display, perform, distribute Covered Software.
  - `EXACT CLAUSE`: *«Each Contributor hereby grants You a world-wide, royalty-free, non-exclusive license under such Contributor's Intellectual Property Rights... to use, reproduce, make available, modify, display, perform, distribute...»*

- **GPLv3 (§2, §4, §9):**
  - `ACTOR`: Recipient / Licensee.
  - `ACTION`: run, propagate, convey.
  - `OBJECT`: Program / Covered Works.
  - `EXACT CLAUSE`: §9: *«Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work.»*; §2: *«The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §2.a, §2.c):**
  - `ACTOR`: Device user.
  - `ACTION`: run one instance on one device.
  - `PROHIBITION`: no ownership transfer; not sold, only licensed.
  - `EXACT CLAUSE`: §2.a: *«The software is licensed, not sold. Under this agreement, we grant you the right to install and run one instance of the software on your device (the licensed device), for use by one person at a time...»*; §2.c: *«Restrictions. The manufacturer or installer and Microsoft reserve all rights (such as rights under intellectual property laws) not expressly granted in this agreement. For example, this license does not give you any right to, and you may not: (i) use or virtualize features of the software separately; (ii) publish, copy (other than the permitted backup copy), rent, lease, or lend the software...»*

---

#### 3.2. OP-NOTICE (Збереження авторських та ліцензійних написів)

- **MIT:**
  - `ACTOR`: Anyone distributing copies or substantial portions.
  - `ACTION`: include the copyright notice and permission notice.
  - `EXACT CLAUSE`: *«The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.»*

- **Apache-2.0 (§4.a, §4.d):**
  - `ACTOR`: You (distributor).
  - `ACTION`: give recipients a copy of this License; retain all copyright, patent, trademark, and attribution notices; include readable copy of NOTICE file.
  - `EXACT CLAUSE`: §4.d: *«If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file...»*

- **MPL-2.0 (§3.1):**
  - `ACTOR`: You (distributor).
  - `ACTION`: inform recipients that Source Code Form is governed by this License and how it can be obtained.
  - `EXACT CLAUSE`: *«You must inform recipients of the Executable Form how they can obtain a copy of the Source Code Form by reasonable means in a timely manner through a medium customarily used for software exchange.»*

- **GPLv3 (§4, §5.a):**
  - `ACTOR`: You (conveyor).
  - `ACTION`: keep intact all notices; display prominent notices stating that work is modified.
  - `EXACT CLAUSE`: §4: *«You may convey verbatim copies... provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply...»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §2.c.v):**
  - `PROHIBITION`: *«You may not... remove, minimize, block, or modify any notices of Microsoft or its suppliers in the software.»*

---

#### 3.3. OP-SOURCE-PROVISION (Обов'язок надання вихідного коду)

- **MIT:**
  - `STATUS`: **Відсутній** (Zero requirement).

- **Apache-2.0:**
  - `STATUS`: **Відсутній** (Можна поширювати виключно в Object form без розкриття source, §4).

- **MPL-2.0 (§3.1, §3.2):**
  - `ACTOR`: You.
  - `TRIGGER`: Distribution of Covered Software in Executable Form or Source Code Form.
  - `OBJECT`: Source Code Form of the Covered Software (лише MPL-файли).
  - `ACTION`: must make Source Code Form available under MPL-2.0.
  - `EXACT CLAUSE`: §3.1: *«All distribution of Covered Software in Source Code Form, including any Modifications that You create or to which You contribute, must be under the terms of this License.»*; §3.2: *«If You distribute Covered Software in Executable Form then... such Source Code Form must be made available by reasonable means...»*

- **GPLv3 (§6):**
  - `ACTOR`: Conveyor of covered work in object code form.
  - `ACTION`: convey machine-readable Corresponding Source.
  - `OBJECT`: All source code, interfaces, build scripts.
  - `EXACT CLAUSE`: §6: *«You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways...»*

- **AGPLv3 (§13):**
  - `ACTOR`: Operator modifying the Program and interacting remotely through computer network.
  - `ACTION`: provide Corresponding Source to all users remotely interacting with it.
  - `EXACT CLAUSE`: §13: *«if you modify the Program, your modified version must prominently offer all users interacting with it remotely through a computer network... an opportunity to receive the Corresponding Source of your version...»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §2.c.vi):**
  - `STATUS`: **Сувора пряма заборона декомпіляції**.
  - `EXACT CLAUSE`: *«You may not... reverse engineer, decompile, or disassemble the software, or attempt to do so, except and only to the extent that the licensing terms governing use of open-source components that may be included with the software provide otherwise...»*

---

#### 3.4. OP-SAME-TERMS (Вимога поширення під тими самими умовами)

- **MIT:**
  - `STATUS`: **Відсутній**. Дозволено субліцензувати та переліцензувати («to sublicense, and/or sell copies»).

- **Apache-2.0:**
  - `STATUS`: **Відсутній** для похідного твору (Derivative Works can be distributed under different terms, provided §4 conditions are met).

- **MPL-2.0 (§3.1):**
  - `SCOPE`: File-level.
  - `OBJECT`: Covered Software (файли під MPL та зміни до них).
  - `ACTION`: All distribution of Covered Software in Source Code Form must be under the terms of this License. Larger Works may combine MPL files with proprietary files (§3.3).
  - `EXACT CLAUSE`: §3.1: *«All distribution of Covered Software in Source Code Form, including any Modifications that You create or to which You contribute, must be under the terms of this License.»*

- **GPLv3 (§5.c):**
  - `SCOPE`: Work-level / Entirety.
  - `OBJECT`: The entire work, as a whole.
  - `ACTION`: You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy.
  - `EXACT CLAUSE`: §5.c: *«You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged.»*

- **Microsoft Windows 11 EULA (Контроль — May 2021):**
  - `STATUS`: **N/A** (Поширення заборонено в принципі; дозволено лише разову повну передачу всього пристрою разом із ліцензійною наклейкою, §4.b).

---

#### 3.5. OP-DIRECT-GRANT (Пряме виникнення зв'язку з першоджерелом)

- **MIT:**
  - `МЕХАНІЗМ`: Грант надається будь-кому, хто одержує копію («to any person obtaining a copy»).

- **Apache-2.0 (§2):**
  - `МЕХАНІЗМ`: Кожен контриб'ютор безпосередньо надає ліцензію реципієнту («each Contributor hereby grants to You...»).

- **MPL-2.0 (§2.1):**
  - `МЕХАНІЗМ`: Прямий грант від кожного контриб'ютора кожному одержувачу («Each Contributor hereby grants You...»).

- **GPLv3 (§10):**
  - `МЕХАНІЗМ`: Автоматична пряма ліцензія downstream-реципієнту від усіх попередніх ліцензіарів; проміжна ланка не діє як субліцензіар.
  - `EXACT CLAUSE`: §10: *«Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §1.a):**
  - `МЕХАНІЗМ`: Прямий контракт кінцевого споживача з корпорацією Microsoft (або виробником пристрою).
  - `EXACT CLAUSE`: *«Depending on how you obtained the Windows software, this is a license agreement between (i) you and the device manufacturer or software installer that distributes the software with your device; or (ii) you and Microsoft Corporation...»*

---

#### 3.6. OP-NO-FURTHER-RESTRICTIONS (Заборона додаткових обтяжень посередником)

- **MIT:**
  - `STATUS`: **Відсутній**. Посередник може додати будь-які обмеження до власного дистрибутиву.

- **Apache-2.0:**
  - `STATUS`: **Обмежений**. Заборонено змінювати саму ліцензію на вихідний код Work, але дозволено додавати комерційні умови до Derivative Works.

- **MPL-2.0 (§3.1):**
  - `ACTOR`: You (distributor).
  - `PROHIBITION`: You may not attempt to alter or restrict the recipients' rights in the Source Code Form.
  - `EXACT CLAUSE`: §3.1: *«You may not attempt to alter or restrict the recipients' rights in the Source Code Form.»*

- **GPLv3 (§10):**
  - `ACTOR`: Anyone conveying covered work.
  - `PROHIBITION`: You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License.
  - `EXACT CLAUSE`: §10: *«You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License...»*

- **Microsoft Windows 11 EULA (Контроль — May 2021):**
  - `STATUS`: **N/A** (Будь-які додаткові дії користувача вже за замовчуванням заблоковані положенням §2.c: *«reserve all rights not expressly granted»*).

---

#### 3.7. OP-PATENT-GRANT & OP-PATENT-RETALIATION (Патентний блок)

- **MIT:**
  - `STATUS`: **Мовчить** (Патентний грант явно не згадується; існує судова невизначеність щодо implied patent license).

- **Apache-2.0 (§3):**
  - `PATENT GRANT`: Each Contributor grants perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent license.
  - `RETALIATION TRIGGER`: If You institute patent litigation against any entity alleging that the Work or a Contribution constitutes patent infringement.
  - `CONSEQUENCE`: Any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.
  - `EXACT CLAUSE`: §3: *«If You institute patent litigation against any entity... alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.»*

- **MPL-2.0 (§2.1.b, §5.2):**
  - `PATENT GRANT`: Express patent license for Contributor Version.
  - `RETALIATION TRIGGER`: If You initiate litigation against any entity by alleging that the Covered Software directly or indirectly infringes any patent.
  - `CONSEQUENCE`: Rights granted to You by any and all Contributors under Section 2.1 of this License shall terminate.
  - `EXACT CLAUSE`: §5.2: *«If You initiate litigation against any entity... alleging that the Contributor Version or Covered Software directly or indirectly infringes any patent, then the rights granted to You by any and all Contributors for the Covered Software under Section 2.1 of this License shall terminate.»*

- **GPLv3 (§11):**
  - `PATENT GRANT`: Express patent grant from each contributor.
  - `PROHIBITION`: Prohibition of discriminatory patent deals (anti-Novell clause: cannot convey if shielded by patent license not available to everyone).
  - `EXACT CLAUSE`: §11: *«Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims... You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work...»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §2.c):**
  - `STATUS`: Жодні патентні права не надаються. Будь-яке використання запатентованих технологій за межами виконання одного інстальованого бінарного коду є прямим порушенням.

---

#### 3.8. OP-TERMINATE, OP-CURE, OP-REINSTATE (Припинення, пільговий період, відновлення)

- **MIT:**
  - `STATUS`: **Мовчить про процедуру**. За загальним правом (common law bare license): невиконання умови збереження копірайту автоматично робить особу порушником копірайту (*naked infringement*).

- **Apache-2.0 (§3, §8):**
  - `TRIGGER`: Патентний позов припиняє патентні права (§3). Загальне порушення ліцензії робить особу відповідальною за copyright infringement. Процедура cure period відсутня.

- **MPL-2.0 (§5.1):**
  - `TRIGGER`: Failure to comply with terms.
  - `CONSEQUENCE`: Automatic termination.
  - `CURE / REINSTATEMENT`:
    - (a) Automatic reinstatement if failure is cured within 30 days of becoming aware.
    - (b) Provisional reinstatement if cured, unless copyright holder explicitly terminates within 60 days of receiving notice.
  - `EXACT CLAUSE`: §5.1: *«If You fail to comply with any of the terms of this License, then Your rights under this License terminate automatically. However, if You become compliant, then the rights granted under this License from a particular Contributor are reinstated (a) provisionally, unless and until such Contributor explicitly and finally terminates Your grants, and (b) on an ongoing basis, if such Contributor fails to notify You of the non-compliance by some reasonable means prior to 60 days after You have come back into compliance.»*

- **GPLv3 (§8):**
  - `TRIGGER`: Any propagation or modification not in accordance with this License.
  - `CONSEQUENCE`: Automatic termination of all rights.
  - `CURE / REINSTATEMENT`:
    - (a) If all violations cease, rights are provisionally reinstated unless copyright holder explicitly and finally terminates within 60 days after cessation.
    - (b) First-time violation cure: rights are permanently reinstated if copyright holder notifies you within 60 days and you cure within 30 days of receipt.
  - `EXACT CLAUSE`: §8: *«All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met... However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally... and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation... Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation... and you cure the violation prior to 30 days after your receipt of the notice.»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §2.d):**
  - `TRIGGER`: Failure to comply with any terms of the agreement.
  - `CONSEQUENCE`: Immediate termination by Microsoft without cure period or reinstatement.
  - `EXACT CLAUSE`: *«If you fail to comply with any terms of this agreement, Microsoft or the device manufacturer may terminate this agreement and your right to use the software. In that case, you must immediately uninstall and destroy all copies of the software.»*

---

#### 3.9. OP-DISCLAIM & OP-LIMIT-LIABILITY (Відмова від гарантій та обмеження відповідальності)

- **MIT:**
  - `EXACT CLAUSE`: *«THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND... IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY...»*

- **Apache-2.0 (§7, §8):**
  - `EXACT CLAUSE`: §7: *«Work is provided on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND...»*; §8: *«In no event and under no legal theory... shall any Contributor be liable to You for damages...»*

- **MPL-2.0 (§6, §7):**
  - `EXACT CLAUSE`: §6: *«Covered Software is provided under this License on an "as is" basis, without warranty of any kind...»*; §7: *«Under no circumstances and under no legal theory... shall any Contributor... be liable to You for any direct, indirect, special, incidental, or consequential damages...»*

- **GPLv3 (§15, §16):**
  - `EXACT CLAUSE`: §15: *«THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW...»*; §16: *«IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW... WILL ANY COPYRIGHT HOLDER... BE LIABLE TO YOU FOR DAMAGES...»*

- **Microsoft Windows 11 EULA (Контроль — May 2021, §10, §11):**
  - `EXACT CLAUSE`: §10: *«Limited Warranty. Microsoft warrants that properly licensed software will perform substantially as described...»* (на відміну від open source, є обмежена комерційна гарантія на 90 днів або 1 рік); §11: *«Exclusion of Other Damages. You can recover from Microsoft and its suppliers only direct damages up to the amount you actually paid for the software (or up to $50.00 if you acquired the software for no charge)... You cannot recover any other damages, including consequential, lost profits, special, indirect, or incidental damages.»*

---

### 4. ЗВЕДЕНА ТАБЛИЦЯ СПОСТЕРЕЖУВАНИХ ОПЕРАТОРІВ

| Спостережуваний оператор | MIT | Apache-2.0 | MPL-2.0 | GPLv3 | AGPLv3 | MS Windows 11 EULA (May 2021) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OP-PERMIT** | ТАК | ТАК | ТАК | ТАК | ТАК | ТАК (суворо звужений) |
| **OP-GRANT** | ТАК | ТАК | ТАК | ТАК | ТАК | ТАК (обмежене право запуску) |
| **OP-PATENT-GRANT** | НІ | ТАК | ТАК | ТАК | ТАК | НІ |
| **OP-CONDITION** | ТАК | ТАК | ТАК | ТАК | ТАК | ТАК |
| **OP-NOTICE** | ТАК | ТАК | ТАК | ТАК | ТАК | ТАК (заборона приховувати) |
| **OP-SOURCE-PROVISION** | НІ | НІ | ТАК (file-level) | ТАК (full) | ТАК (full + network) | **ПРОТИЛЕЖНИЙ** (заборона reverse engineering) |
| **OP-SAME-TERMS** | НІ | НІ | ТАК (file-level) | ТАК (work-level) | ТАК (work-level) | N/A |
| **OP-DIRECT-GRANT** | ТАК | ТАК | ТАК | ТАК | ТАК | ТАК (контракт прямо з MS) |
| **OP-NO-FURTHER-RESTRICTIONS** | НІ | НІ | ТАК (source form) | ТАК (all rights) | ТАК (all rights) | **ПРОТИЛЕЖНИЙ** (all rights reserved) |
| **OP-PATENT-RETALIATION** | НІ | ТАК | ТАК | ТАК | ТАК | N/A |
| **OP-TERMINATE** | Мовчить | ТАК (патент) | ТАК (auto) | ТАК (auto) | ТАК (auto) | ТАК (одностороннє право MS) |
| **OP-CURE** | НІ | НІ | ТАК (30 днів) | ТАК (30 днів) | ТАК (30 днів) | НІ |
| **OP-REINSTATE** | НІ | НІ | ТАК (auto/prov) | ТАК (auto/prov) | ТАК (auto/prov) | НІ |
| **OP-DISCLAIM** | ТАК | ТАК | ТАК | ТАК | ТАК | ЧАСТКОВО (є 90-денна limited warranty) |
| **OP-LIMIT-LIABILITY** | ТАК | ТАК | ТАК | ТАК | ТАК | ТАК (ліміт сумою оплати або $50) |

---

### 5. МЕТОДОЛОГІЧНИЙ ВИСНОВОК: ПІДГОТОВКА ДО BLIND HISTORICAL SEARCH

1. **Сучасна «ліцензія» не є атомом:**  
   Це конгломерат із щонайменше **14 незалежних юридичних операторів**.
2. **Оператори не виникають у праві одночасно:**  
   - `OP-PERMIT` і `OP-GRANT` мають іншу генеалогію, ніж `OP-SAME-TERMS` або `OP-NO-FURTHER-RESTRICTIONS`.
   - `OP-CURE` та `OP-REINSTATE` (пільговий строк виправлення порушення) мають власну процедурну історію, автономну від копірайту.
3. **Правило для наступного кроку (Blind Historical Search):**  
   Ми беремо не назви правових пам'яток, а окремі операторні структури (`ACTOR / ACTION / OBJECT / TRIGGER / CONDITION / CONSEQUENCE`) і шукаємо їхнє незалежне документальне виникнення у джерелах XI–XVIII ст. без упередженої прив'язки до слів *licence*, *libertas* чи *pactum*.
