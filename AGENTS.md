# Правила роботи агента / Agent working rules

Цей файл — локальний контракт репозиторію `pravda`. Він доповнює головний
[`ecosystem/AGENTS.md`](../../ecosystem/AGENTS.md); у разі конфлікту діє пряме
розпорядження власника та основний ecosystem-контракт.

## Українська — нормативна частина

- Власник формує ідею; агент будує малий перевірюваний експеримент, пояснює
  код до рівня представлення даних і ставить 3–5 питань на розуміння.
- Людські memory, policy, plan, architecture, research і README не можуть
  бути лише англійськими. Українська — основна; технічну англійську,
  identifiers, API, команди, цитати й код зберігати точно.
- Scope мовної політики — усі авторські репозиторії власника. Форки,
  дзеркала, vendored-залежності й upstream-код не стають авторськими через
  локальну присутність.
- Канонічний текст `LICENSE`/`VOLNOST.md` не змінювати без прямого рішення;
  пояснення меж ліцензії писати в README.
- Перед commit будь-якого `.my`/`.wsm` запускати `my-lisp --oracle-check`.
- Перед push завжди робити `git fetch`; commit/push виконувати лише після
  перевірки diff і тестів, доречних до зміни.
- Не переписувати Git history і не маскувати невідоме припущенням: джерело,
  provenance та межі доказу мають бути явними.

## English — normative mirror

This file is the local contract for `pravda`. It supplements the main
[`ecosystem/AGENTS.md`](../../ecosystem/AGENTS.md); direct owner instructions and
the ecosystem contract take precedence if they conflict.

- The owner forms the idea; the agent builds a small verifiable experiment,
  explains code down to data representation, and asks 3–5 understanding
  questions.
- Human-authored memory, policy, plan, architecture, research, and README
  documents must not be English-only. Ukrainian is primary; preserve technical
  English, identifiers, APIs, commands, quotations, and code exactly.
- The language-policy scope is all owner-authored repositories. Forks, mirrors,
  vendored dependencies, and upstream code do not become authored by presence.
- Do not alter canonical `LICENSE`/`VOLNOST.md` text without a direct owner
  decision; explain license boundaries in README.
- Before committing any `.my`/`.wsm`, run `my-lisp --oracle-check`.
- Always `git fetch` before push; inspect the diff and run relevant checks.
- Do not rewrite Git history or turn unknown provenance into an assumption.

## Repository boundary

`pravda` is an owner-authored research repository about Ukrainian legal
tradition, freedom, and bounded power. Preserve its historical quotations and
third-party source conditions; distinguish observation, interpretation, and
hypothesis.
