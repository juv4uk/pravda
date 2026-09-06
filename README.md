# PRAVDA (ПРАВДА)

**Дослідження 1000-річної української правової традиції, природи волі, зв'язаної влади та взаємності.**

Research into the thousand-year Ukrainian legal tradition of will, bound authority, and reciprocity.

---

## Почни звідси · Start here

**Найкоротший шлях:**

1. Прочитай [**GETTING-STARTED.md**](GETTING-STARTED.md) (рівні читання)
2. Або одразу [**VOLNOST.md**](VOLNOST.md) — п'ять речень, що є ліцензією

### ВОЛЬНІСТЬ (ядро)

```text
Цей твір дано тобі для вільного користування, вивчення, зміни й творення нового.

Користуйся своєю волею, пам'ятаючи про волю іншого.

Не перетворюй отриману свободу на владу над тим, хто прийде після тебе.

Твори так, щоб після тебе залишалося більше можливостей, а не більше залежності.

Автор стоїть перед цими словами так само, як і кожен інший.
```

Це не юридичний кодекс покарань. Це слово майстра до майстра.

---

## Про проєкт · About

**PRAVDA** — фундаментальний дослідницький репозиторій екосистеми.  
Він є колискою етики майстерні [PACTA](PACTA.md) та ліцензії [ВОЛЬНІСТЬ](VOLNOST.md), яка об'єднує всі власні твори екосистеми.

### Архітектура думки

```text
PRAVDA
  │
  ├── Історичне та семантичне дослідження
  │   (Руська Правда → Статути → Зборів → Гадяч → Орлик 1710)
  │         ↓
  ├── PACTA.md
  │   Етика майстерні: відношення, симетрія, зв'язана влада
  │         ↓
  └── VOLNOST.md
      П'ять простих речень — діюча ліцензія
```

### Що зібрано в репозиторії

1. **Корпус першоджерел** ([sources/](sources/)) — від XI ст. до Конституції Пилипа Орлика 1710
2. **Семантика понять** ([semantics/](semantics/), [dictionary/](dictionary/)) — *право*, *вольність*, *влада*, *свавілля*, *ряд*…
3. **Аналітичні тести** ([research/](research/))
   - [BOUND-AUTHORITY-TEST.md](research/BOUND-AUTHORITY-TEST.md) — 5 питань зв'язаної влади
   - [VOLIA-VOLNOST-SVAVILLIA.md](research/VOLIA-VOLNOST-SVAVILLIA.md) — каскад волі → влади
   - [NODES-OF-POWER.md](research/NODES-OF-POWER.md) — сучасні вузли залежності
4. **Анти-суддівський принцип** — ніхто (включно з автором) не є остаточним суддею власного спору
5. **Інструменти відчуття часу** ([scripts/](scripts/))

---

## Ключові документи

| Документ | Роль |
|----------|------|
| **[VOLNOST.md](VOLNOST.md)** | Канонічні 5 речень ліцензії |
| **[PACTA.md](PACTA.md)** | Етика майстерні |
| **[GETTING-STARTED.md](GETTING-STARTED.md)** | Рівні читання для новачка |
| [HISTORICAL-CLAIMS-REGISTER.md](HISTORICAL-CLAIMS-REGISTER.md) | Атомарні історичні свідчення |
| [BEGRIFFSGESCHICHTE-MATRIX.md](BEGRIFFSGESCHICHTE-MATRIX.md) | Поняттєва історія термінів |

---

## English overview

**PRAVDA** studies how freedom to create can coexist with the will of the other, drawing on a millennium of Ukrainian legal sources (Ruska Pravda, Lithuanian Statutes, Cossack treaties, Orlyk’s 1710 Constitution).

It is the cradle of:
- **PACTA** — workshop ethics (master speaking to master about relation, symmetry, and bound authority)
- **VOLNOST** — a five-sentence living license used across the ecosystem

Core stance: any attempt to turn received freedom into unilateral power over the next person is rejected. The author stands under the same words as everyone else. This is deliberately *not* a punitive legal code.

Start with [GETTING-STARTED.md](GETTING-STARTED.md) or go straight to [VOLNOST.md](VOLNOST.md).

---

## Архітектура репозиторію

```text
pravda/
├── README.md                  # Фасад і навігація
├── GETTING-STARTED.md         # Рівні читання (новий вхід)
├── VOLNOST.md                 # 5 речень ліцензії
├── PACTA.md                   # Етика майстерні
├── LICENSE                    # Той самий текст ВОЛЬНОСТІ
│
├── sources/                   # Першоджерела
├── research/                  # Аналітика і тести влади
├── semantics/ + dictionary/   # Поняттєвий апарат
├── license/                   # Архівні чернетки (superseded)
└── scripts/                   # Інструменти відчуття часу
```

---

## Еволюція: від HFL до ВОЛЬНОСТІ

На ранньому етапі розглядався *Human Freedom License* з фіксованими заборонами. Дослідження показало:

> Будь-яка спроба створити юридичний кодекс покарань неминуче робить автора «суворим дядьком» і верховним суддею, відтворюючи ту саму владу, яку ми прагнули зв'язати.

Тому юридичні чернетки в `license/` мають **архівний статус**. Актуальний результат — **[ВОЛЬНІСТЬ](VOLNOST.md)**.

---

## Інструменти відчуття часу

```bash
python3 scripts/repo-time-rhythm.py .
python3 scripts/swarm-comms-pulse.py /path/to/comms-log.md
python3 scripts/task-incubation-pulse.py /path/to/comms-log.md
python3 scripts/guard-inbox-latency.py /path/to/guard-inbox.mylog
```

---

## Ліцензія · License

Цей твір поширюється під [ВОЛЬНІСТЮ](LICENSE).

---

*Створено з любов'ю до правди, волі та людини. 2026.*
