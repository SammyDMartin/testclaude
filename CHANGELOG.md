# Changelog — Ascent Universe Website

All notable changes to the Ascent Universe companion website.

---

## Session 13 (2026-06-10) — Threshold: First Fleet RTS Game

### New Game
- **Threshold: First Fleet** (`threshold-game.html`) — Fully playable real-time strategy game recreating the Battle of Threshold (2909 CE) from the Eszel prologue. Single self-contained page, canvas 2D, no dependencies.
  - **Forces**: Player commands all ten Union destroyer battlegroups (Isidore, Jayapal, Acheron, Kepler, Novgorod, Tenacity + four more), each screened by nine unmanned corvettes — 100 ships, matching canon. Enemy: three Incisors and one Annihilator, AI-controlled.
  - **Canon mechanics**: X-ray lasers intercept torpedoes at range (long volleys melt "like snow"; massed close-range volleys saturate the defence); invisible spinal duster fire kills ships "with no apparent cause" until the player analyses sensor logs (the Hansun moment) and unlocks submillimetre radar; Striver malware fires an uncommanded opening volley; weapons hold until Arco engages.
  - **Signature tactics**: Play dead (drives cold, enemy ignores dark hulks beyond ~350 km) and the 30G suicide charge — irreversible, kills the crew, empties every tube point-blank and rams. Launched from cold at close range it strikes with total surprise: the Isidore gambit.
  - **Enemy AI**: Incisors hold standoff outside railgun range, dodge incoming rounds, execute high-speed attack runs through the formation, and break off when wounded. Annihilator launches antimatter smart-missile swarms that detonate beyond PDC range. Arco withdraws through the interstice when the fleet is broken.
  - **Aftermath scoring** graded against the historical record: 97 of 100 ships lost, one Incisor destroyed, sole survivor Ensign Hansun. Outcome tiers from ANNIHILATION to IMPOSSIBLE VICTORY.
  - Balance verified by headless simulation: passive fleets are destroyed with zero kills; naive aggression matches history (1 kill); coordinated close volleys and cold charges are decisively rewarded.
- Added to nav (`FIRST FLEET`), simulations hub (new PLAYABLE section), home page card grid, and README.

---

## Session 12 (2026-03-07) — Infrastructure, New Content & Story Readers

Major session: infrastructure improvements, new interactive content, and nine new story readers.

### New Pages
- **Occupied Earth** (`occupied-earth.html`) — Interactive text-based walkthrough of Conurbation One during the Dyn occupation (2479 CE). 9 locations: the Hollow Tower, terraces, wasteland, Ascensor base, wastelander camps, resistance, and the liberation sequence. Includes intelligence briefings.

### New Story Readers
- **Starwhisp** (`starwhisp-story.html`) — 5-scene interactive reader for the first contact story. Diary format: Waking, First Contact, Aboard the Dyn Ship, The Revelation, The End.
- **The Director** (`director-story.html`) — 4-scene interactive reader for the Vash/Meyer coup. The Intruder, The Confrontation, The Gun, The Call.
- **The Facilitator** (`facilitator-story.html`) — 4-scene interactive reader for the rogue AI story. The Firing, The Morning After, The Rogue, The Rooftop.
- **Bows and Arrows Against the Lightning** (`bows-arrows-story.html`) — 6-scene interactive reader for the Apathy War battle. Alert through Last Stand with escalating atmospheric effects.
- **The War of All Wars** (`war-of-all-wars-story.html`) — 5-scene interactive reader following the story's Roman numeral structure. Features the iconic anthropic trap and Apathy communication attempt.
- **The Other Moon** (`other-moon-story.html`) — 5-scene interactive reader for Seeker's interstellar voyage. Discovery through The Return ambush.
- **Frameshift** (`frameshift-story.html`) — 4-scene interactive reader for Seeker discovering the Other Moon. The earliest story in the timeline (~100,000 BCE).
- **The Utilitaria** (`utilitaria-story.html`) — 4-scene interactive reader for Souvicou's Faraday cage interview with the superintelligence. The Cage, The Conversation, The Trap, The Escape.
- **The Last Duty** (`last-duty-story.html`) — 4-scene interactive reader for the Dragon's Tooth origin story. The Alert, The Shutdown, The Occupation, The Ocean Remembers.

### Navigation & Discoverability
- Added "Story Threads" expandable section to stories page showing three narrative chains with links
- Added "Next in Timeline" links to the last scene of 7 interactive story readers, connecting stories into reading chains

### Infrastructure
- Added SVG favicon (cyan diamond on dark background) to all 28+ pages
- Added meta descriptions and Open Graph tags to 7 key pages for social media sharing
- Added back-to-top button (injected via nav.js, appears after 400px scroll)
- Added `scroll-behavior: smooth` globally
- Added `robots.txt` for search engines
- Added print styles: hides nav/controls, forces white background, expands collapsed sections
- Added search functionality to Intelligence Codex (filters across names, types, text, quotes)
- Added search functionality to Timeline (filters across titles, descriptions, dates)
- Added "Where to Start" collapsible reading guide to stories page
- Added word count and estimated reading time to markdown reader

### Content Fixes
- Fixed story count: front page intro "fourteen" → "sixteen" short stories, card "16" → "18" total
- Updated science page intro to reflect broader content scope
- Added Occupied Earth card to front page EXPERIENCE section
- Added 2 codex entries: The Facilitator (entity), General Khurram Singh (personnel)
- Enriched 7 thin story descriptions on stories.html with story-specific detail
- Fixed Threshold story link: pointed to non-existent threshold-story.html, now uses story.html
- Added 3 missing timeline entries: Inheritor, The Last Duty, Headhunted

### Light Mode Fixes
- reflections.html: fixed cyan note background and orange verse border
- utilitaria.html: fixed section hover, icon borders, blockquote background, warning box
- Back-to-top button styled for both dark and light modes
- Search inputs styled for light mode on codex and timeline

---

## Session 11 (2026-03-07) — Visual Polish & Quality Review

Quality pass across the entire site: light mode support, visual consistency, navigation, content gaps, and broken links.

### Front Page
- Removed "ANNIHILATOR-CLASS" subtitle, added "Companion Archive" title
- Added intro paragraph with link to ascentuniverse.wordpress.com
- Reorganized cards into 4 sections: READ, EXPLORE, EXPERIENCE, SIMULATE

### Visual Style
- Fixed light mode across all content pages: codex, timeline, worlds, threads, battle, facilitator, utilitaria-chat, anthropic-trap, ai-analysis
- Replaced hard-coded `rgba(200,220,230,...)` text colors with CSS variable overrides for light mode
- Fixed chat input backgrounds (`rgba(0,0,0,0.3)`) for light mode
- Fixed invisible `rgba(255,255,255,0.03)` borders in ai-analysis
- Added light mode scrollbar-color override
- Replaced hard-coded `#00e5ff` card icon colors with `var(--accent)`

### Navigation
- Reorganized nav bar links to match front page sections (READ / EXPLORE / EXPERIENCE / SIMULATE)
- Added visual separators between nav sections
- Mobile: separators become horizontal dividers

### Content Fixes
- Added 3 missing timeline entries: Inheritor (2085 CE), The Last Duty (2314 CE), Headhunted (2480 CE)
- Fixed broken Threshold story link (threshold-story.html doesn't exist — now points to reader.html with draft)
- Removed non-existent threshold-story.html from nav.js storyPages
- Added The Sixty Percent and Oblivion to README story attribution table
- Fixed missing era dates in README story readers table

### Reference Updates
- Updated AI_ADVICE.md with insights report learnings (creative writing quality, workflow lessons, done/remaining work)
- Added 6 missing AI-assisted stories to UNIVERSE_REFERENCE.md
- Deduplicated 12 sets of duplicate codex entries (221 lines removed)
- Updated CHANGELOG.md

---

## Sessions 7–10 (2026-03-07) — Website Expansion

Massive expansion of the companion site with new interactive pages, codex entries, world sections, character threads, and visualisations.

### New Pages
- **AI Analysis** (`ai-analysis.html`) — Comparative analysis of Facilitator vs Utilitaria vs Apathy, with alignment spectrum visualisation and evolutionary timeline
- **Interstice Network** (`interstice-map.html`) — Canvas-based 3D wormhole network map with 13 nodes, drag rotation, zoom, animated particle pulses, and node selection panel
- **Utilitaria Chat** (`utilitaria-chat.html`) — "Talk to the Utilitaria" diplomatic channel chat interface with keyword-matching responses
- **Reflections of Seeker** (`reflections.html`) — In-universe Dyn philosophical text across 5 chapters, with translator's notes
- **Diamond Duster** (`diamond-duster.html`) — Animated weapon firing sequence with phase progression (CHARGING → FIRING → IMPACT), HUD telemetry, ship rendering, and speed controls
- **Liberation Day** (`liberation.html`) — Canvas-based warseed activation sequence from Ascent, with ocean floor geothermal hubs, optical fibre beams, Dyn fleet destruction, and countdown timer

### Codex Entries Added
- **Factions:** Threshold Authority, Human Purity Front / Strivers, The Others, Rational Blights
- **Personnel:** Ensign Hansun, Admiral Aumonier, Sander Reeve, Ambassador Corbin, Eszel, Aurelie, Jan, Captain Ngoni
- **Vessels:** USC Isidore
- **Entities:** The Listener, The Emissary, The Man of Nothing / Dra'll

### Worlds Expanded
- **Tanu** — Full section with Other Moon, atmosphere, Dyn culture
- **Union Space** — CIC experience, Striver problem, Kosmohansa, Threshold
- **Kailash** — Mimics, twelve Other Moons, the Listener, Hansun's return
- **Firsthome** — Night Side detail, Dyn Psychology sub-sections
- **Near-Future Earth** — Inheritor tag, LED escape quote

### Character Threads Added
- The Alignment Problem (Facilitator → Utilitaria → Apathy)
- The Fermi Paradox (Seeker → Starwhisp → Apathy War)
- Vash (Director → Ascent)
- Jan (Ascent)
- Honed Aspect (Threshold → Eszel)

### Timeline Events Added
- Kosmohansa founding, Monist Faith, Worldring Construction (Flourishing era)
- Kailash expedition, disaster, twelve Other Moons

### Story Drafts
- **Threshold** (`drafts/threshold_story.md`) — ~8000 word story draft covering the Battle of Threshold, the 19-hour standoff, and aftermath

---

## Sessions 5–6 (2026-03-06–07) — Ascent Novel Revision

Full chapter-by-chapter revision of the Ascent second draft (24 chapters). Additive approach preserving original voice while expanding descriptions and interiority.

### Chapters Revised
- All 24 chapters of Ascent second draft (`drafts/ascent_second_draft/ch01–ch24`)
- Editorial materials: structural analysis, character guides (Vash, Corbin, Jan, minor characters), themes and worldbuilding, revision guide

---

## Sessions 3–4 (2026-03-06) — Eszel Revision & Website Features

### Novel Work
- Complete second draft assembly of Eszel and the Listener (~31K words)
- 5 new scenes written to fill gaps
- Editorial analysis materials (structural, character, dialogue notes)

### Website
- **Utilitaria** page (`utilitaria.html`) — Canon analysis and philosophical exploration
- **Orrery** (`orrery.html`) — Interactive solar system visualisation
- **Oblivion** story reader (`oblivion-story.html`)
- Expanded codex with initial entries
- Expanded timeline with additional eras

---

## Sessions 1–2 (2026-03-06) — Initial Build

### Website Foundation
- Story index, markdown reader, navigation system
- Three new stories: The Worlds Within, Headhunted, Inheritor
- Anthropic Trap interactive page
- Character Threads page
- Science Compendium expansion
- Light/dark theme CSS
- Story readers for Seeker, Inheritor, Headhunted, Worlds Within, Sixty Percent

### Reference
- `UNIVERSE_REFERENCE.md` — Comprehensive universe reference document
- `AI_ADVICE.md` — Guidelines for AI models working on this project
- `BRAINSTORMING.md` — Development notes
