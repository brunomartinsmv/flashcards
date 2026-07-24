# Flashcards (language study)

Personal workshop for creating Anki flashcards that support Bruno's path to fluency in languages he is learning.

## Language

**Flashcards (repo)**:
The personal workshop that produces language-learning cards for Anki toward fluency.
_Avoid_: general study repo, banking/example prompts as current scope

**Language**:
A target language Bruno is learning toward fluency (today: Spanish, English; others later).
_Avoid_: subject, topic (when meaning a whole language)

**Fluency**:
The learning goal for each **Language** — usable, active command, not passive recognition alone.
_Avoid_: “finishing the deck”, “knowing the cards”

**Production**:
The primary training mode: actively retrieving and using the linguistic target.
_Avoid_: recognition-only practice as the default

**Recognition**:
Understanding or completing a target with lower retrieval demand; allowed in the mix, not the default emphasis.
_Avoid_: treating easy recognition cards as evidence of **Fluency**

**Support**:
The clarifying side of a card (Extra/notes): how the target is explained to Bruno.
_Avoid_: always-PT translation as a universal rule; “answer” when meaning the support field

**L1 Support**:
**Support** written in Portuguese, used when the target is still new or fragile.
_Avoid_: forcing Portuguese forever on strong languages

**In-context Support**:
**Support** that explains what the target means *in that sentence* (gloss/sense), not a full parallel translation — the preferred direction for English as it advances.
_Avoid_: word-list definitions detached from the sentence; mandatory full PT rendering

**Target**:
The linguistic unit the card forces Bruno to retrieve — a word-in-context, chunk, collocation, or structure, chosen by **Language** and level.
_Avoid_: “vocabulary” as a vague catch-all; treating every card as a bare word list item

**Card**:
One study item in a **Lote** or **Deck**: a single **Cloze** (or legacy) note with one **Target** and its **Support**.
_Avoid_: using “flashcard” for the repo, the **Lote**, and the item interchangeably

**Generation Queue**:
The ordering policy for creating new material across **Languages** — Spanish and English proceed in parallel (smaller batches), not one language blocking the other.
_Avoid_: “Spanish-only until backlog is zero” as a hard rule; abandoning the weaker language to “finish” English

**Lote**:
One weekly generation unit for a single **Language** (~10–20 **Cards** normally; smaller when the **Deck** New backlog is high), stored as its own dated file under that language’s folder and imported promptly.
_Avoid_: monthly mega-batches as the default; one file mixing multiple languages; parking unimported **Lotes** “for later”

**Deck**:
The live Anki collection for one **Language**. External Anki names stay `idioms__spanish` / `idioms__english` (legacy labels, not a content restriction).
_Avoid_: treating the repo alone as the studied collection; renaming Decks just to drop “idioms”

**Inventory**:
The dedupe universe for a **Language**: a fresh **Deck Export** plus any **Lotes** in the repo not yet reflected in that export.
_Avoid_: generating against a stale export; ignoring unimported **Lotes**

**Inventory Gate**:
Hard stop before generation when the **Deck** export is missing or older than **Export Freshness** — the cycle must not invent **Cards** against a blind **Inventory**.
_Avoid_: best-effort generation on whatever file happens to be around

**Export Freshness**:
Maximum age of a **Deck** export for the **Inventory Gate** to pass: **7 days**.
_Avoid_: same-calendar-day only; multi-week stale exports

**Deck Export**:
The Anki text export of a **Deck**, kept outside the repo (e.g. `/Users/bruno/Documents/idioms__spanish.txt`); path recorded in the **Language Profile**.
_Avoid_: committing live exports into git as the source of truth

**Prompt Import**:
The policy of importing a **Lote** into its **Deck** soon after **Review Gate** — sized to what Bruno will actually study — rather than stockpiling files in the repo.
_Avoid_: “generate now, import whenever”; forgotten pending **Lotes**

**Cloze**:
The default Anki note type for new **Lotes** in every **Language**: one `{{c1::Target}}` lacuna per **Card**, with **Support** in Extra/notes.
_Avoid_: Basic/`_____` as the default for new material; reversed cards

**Legacy Backlog**:
Existing notes already in a **Deck** (including easy New cards); kept and studied as-is without mass suspend/rewrite — quality bar applies to new **Lotes** only.
_Avoid_: blocking new generation until the old pile is cleaned; mass deletion as the default plan

**Input**:
Real language material Bruno supplies for a cycle (series lines, Discord, work email, weekly doubts); when present, it outranks theme defaults for that **Lote**.
_Avoid_: requiring **Input** every week or the automation stalls

**Theme Defaults**:
The skill’s priority themes and distributions used when no **Input** is available for that **Language**’s weekly **Lote**.
_Avoid_: inventing forever from themes while ignoring available **Input**

**Review Gate**:
Bruno’s manual check of a generated **Lote** (edit/reject **Cards**) after automated validation and before import into the **Deck**.
_Avoid_: fully automatic import; trusting script validation alone for naturalness

**Process Skill**:
The shared generation rules (pipeline, **Lote**, **Cloze**, **Inventory**, **Review Gate**, **Prompt Import**) that apply to every **Language**.
_Avoid_: copying the full pipeline into each language folder

**Language Profile**:
The short per-**Language** overlay (level, **Target** bias, **Support** style, **Theme Defaults**, deck/export paths).
_Avoid_: a single monolithic multi-language skill with no profiles; fully separate duplicated skills

**Language Folder**:
Per-**Language** directory under `flashcards/` (e.g. `flashcards/spanish/`, `flashcards/english/`) that holds that language’s **Lotes**.
_Avoid_: a flat mixed `flashcards/` dump; elaborate current/archive splits while **Prompt Import** is the norm

## Relationships

- This **Flashcards (repo)** exists only for **Languages** — not for arbitrary school/work subjects.
- **Cards** aim at **Fluency**, with **Production** as the default emphasis and **Recognition** as secondary.
- **Support** depends on **Language** and novelty: new/fragile material may use **L1 Support**; stronger material (especially English) prefers **In-context Support**.
- Each **Card** has exactly one **Target**; the **Target** kind (word-in-context vs chunk/structure) depends on **Language** and level.
- The **Generation Queue** runs **Languages** in parallel; each cycle produces one **Lote** per active **Language**.
- When a **Deck** already has a high New backlog, the weekly **Lote** is reduced (e.g. ~5), not skipped and not stockpiled.
- **Prompt Import** means: after **Review Gate**, import soon at a studyable size — do not stockpile.
- Before generating a **Lote**, the **Inventory Gate** must pass (fresh **Deck Export** + pending **Lotes**).
- New **Lotes** use **Cloze**; legacy Basic notes in a **Deck** may remain but are not the template for generation.
- **Legacy Backlog** stays; improvement is forward-only via new **Lotes**.
- A weekly **Lote** prefers **Input** when available; otherwise it falls back to **Theme Defaults**.
- Pipeline per **Lote**: **Inventory Gate** → generate → validate → **Review Gate** → import into **Deck**.
- Agents follow the **Process Skill** plus the relevant **Language Profile**.
- Each **Language** owns a **Language Folder** for its **Lotes**.
- Anki **Deck** display names may stay `idioms__*`; domain language still says **Deck** of that **Language**.

## Example dialogue

> **Dev:** "Should we bring back the banking example as an active workflow?"
> **Domain expert:** "No — this **Flashcards (repo)** is only for **Languages**."
>
> **Dev:** "The Spanish deck has ~12% difficulty and ~1.5s/card — is that success?"
> **Domain expert:** "No. **Fluency** needs **Production**. Easy **Recognition** does not count as progress by itself."
>
> **Dev:** "For English, should Extra always be a full Portuguese translation?"
> **Domain expert:** "Only if it's still new. Otherwise I want **In-context Support** — what that word means in that sentence."
>
> **Dev:** "Is every **Target** a single word?"
> **Domain expert:** "No. In Spanish I mostly want chunks and structures. In English, word-in-context is fine as I level up."
>
> **Dev:** "Spanish has thousands of New cards — should we pause English generation?"
> **Domain expert:** "No. Keep the **Generation Queue** parallel; just don't dump huge imports into a deck that's already backed up."
>
> **Dev:** "Should automation produce one big monthly file with ES and EN together?"
> **Domain expert:** "No. One weekly **Lote** per **Language**, about 10–20 **Cards** each."
>
> **Dev:** "The Spanish export has ~300 lines but stats show thousands of cards — can we generate anyway?"
> **Domain expert:** "No. **Inventory Gate** fails. Re-export the **Deck** first."
>
> **Dev:** "New backlog is huge — generate 20 and leave them in the repo?"
> **Domain expert:** "No. Make a reduced **Lote** and use **Prompt Import**. If it sits in the repo I'll forget it."
>
> **Dev:** "Should English use Basic with 'what does this word mean in the sentence'?"
> **Domain expert:** "No. Still **Cloze**; put the in-context sense in **Support**."
>
> **Dev:** "Should we suspend the thousands of easy Spanish New cards?"
> **Domain expert:** "No. That's too much work. Leave the **Legacy Backlog**; just add better **Cards** going forward."
>
> **Dev:** "No notes from me this week — skip generation?"
> **Domain expert:** "No. Use **Theme Defaults**. If I pasted Discord lines, those **Input** items win."
>
> **Dev:** "Can automation import straight into Anki after the validator passes?"
> **Domain expert:** "No. There is a **Review Gate**. Bad **Cards** become permanent **Legacy Backlog**."
>
> **Dev:** "Should we clone the whole Spanish skill for English?"
> **Domain expert:** "No. One **Process Skill**, plus a short English **Language Profile**."
>
> **Dev:** "Keep dumping English and Spanish TSVs in one flat folder?"
> **Domain expert:** "No. Each **Language** gets a **Language Folder**."
>
> **Dev:** "Rename `idioms__spanish` because it's not only idioms?"
> **Domain expert:** "Not worth it. Keep the Anki name; in the repo we still say the Spanish **Deck**."
>
> **Dev:** "Export is two weeks old — generate with best effort?"
> **Domain expert:** "No. **Inventory Gate** blocks until there is a fresh export."

## Flagged ambiguities

- "flashcards" resolved (2026-07-24): **Flashcards (repo)** vs **Card** (item); avoid bare “flashcard” when either could apply.
- Scope resolved (2026-07-24): languages only, not general subjects.
- Training mode resolved (2026-07-24): mix with emphasis on **Production**.
- Support policy resolved (2026-07-24): per-language; **L1 Support** for new material; **In-context Support** as English matures.
- **Target** shape resolved (2026-07-24): both word-in-context and chunk/structure, by language and level.
- **Generation Queue** resolved (2026-07-24): parallel across languages; periodic automation desired.
- **Lote** cadence resolved (2026-07-24): weekly per language; shrink when New is high; **Prompt Import** after **Review Gate**.
- **Inventory** resolved (2026-07-24): fresh **Deck** export + unimported **Lotes**; **Inventory Gate** blocks if export missing/stale.
- **Export Freshness** resolved (2026-07-24): ≤ 7 days.
- Note type resolved (2026-07-24): **Cloze** default for all new **Lotes**.
- **Legacy Backlog** policy resolved (2026-07-24): keep as-is; improve only via new **Lotes**.
- Material source resolved (2026-07-24): **Input** overrides **Theme Defaults**.
- Import safety resolved (2026-07-24): **Review Gate** before import.
- Skill shape resolved (2026-07-24): **Process Skill** + **Language Profiles**.
- Repo layout resolved (2026-07-24): **Language Folders** under `flashcards/`.
- **Deck** naming resolved (2026-07-24): keep external `idioms__*` labels.
- **Deck Export** location resolved (2026-07-24): outside the repo; paths in **Language Profiles**.
- ADRs recorded (2026-07-24): `docs/adr/0001`–`0003` (profiles, Cloze, gates/import).
- Grill session closed (2026-07-24): domain vocabulary accepted; lote filename convention left flexible for implementation.
