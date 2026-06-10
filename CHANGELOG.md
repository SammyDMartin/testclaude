# Changelog — Ascent Universe Website

All notable changes to the Ascent Universe companion website.

---

## Session 13c (2026-06-10) — War of All Wars RTS & First Fleet Visual Polish

### New Game
- **War of All Wars** (`apathy-game.html`) — Playable RTS at relativistic scale: command 20 A-spheres and 3 D-spheres against the Apathy, an Earth-mass alien entity decelerating at 40,000 G.
  - 6,000 × 4,000 Mm battlespace (light-minute scale), 0.5s fixed timestep, time compression to 64×
  - A-spheres: 100G accel, frameshift drives (1000 Mm range), 12 Slasher torpedoes, 2 conversion bombs
  - D-spheres: 2G accel (5G burst), 800 HP + 100 armour, 220 X-ray lasers, 8 gamma cannons, 60 Slashers, 30 conversion bombs
  - Apathy: graver spikes (probabilistic), stellar-grade lasers, shearing gravity waves (AoE), anti-mind morale drain, anthropic trap
  - Morale system: anti-mind affects degrade fire rate; anthropic trap triggers dramatic "YOU ARE ALMOST CERTAINLY NOT REAL" overlay
  - Evacuation counter: 800k people/second through the interstice — hold long enough to save billions
  - Four scenarios: Scout (1000t), Standard/Heppolon (5.97e9t), Onslaught (5.97e11t), Extinction (5.97e13t)
  - Player abilities: Slashers [T], Gamma Cannons [G], Conversion Bombs [C], Frameshift [V], Reactor Overload [X]
  - Full SIM autoplay mode for observing AI fleet behaviour
  - Added to nav, simulations hub, home page card grid, and README

### Visual Improvements (threshold-game.html)
- Torpedo launch reticle FX: expanding ring + dashed vector line to target + diamond reticle + count badge
- Enhanced velocity vectors: thicker when accelerating, 60s tick marks, red during charge
- Torpedo projection lines (30s ahead while fuel remains)
- Selected ship waypoint/target visualisation
- SIM autoplay mode with Union fleet AI tactics
- Starting cordon increased from 17,000 → 25,000 km

---

## Session 13b (2026-06-10) — First Fleet v2: Real-Scale Physics & Commander AI

Major rework of `threshold-game.html` based on playtest feedback:

### Realism (true scale throughout)
- All quantities in real units: positions in km on a 90,000 × 60,000 km battlespace, velocities in km/s, accelerations in G (1 G = 0.00981 km/s²)
- Real performance figures: destroyers 10 G military / 30 G destruct; Incisors 12 G / 28 G burst; Annihilator 5 G combat / 20 G peak (per the MSD spec sheet — Δv 6,931 kps cruise); torpedoes 50 G with 250 kps Δv budgets; F-AM micromissiles 250 G; railgun muzzle 20 kps; duster stream 2,000 kps; lasers effectively instantaneous
- KSP-style time compression (1×/4×/16×/64×) on a fixed 0.2 s timestep — flip-and-burn arrival steering, ballistic drift when cold, segment-swept collision so 100+ kps closing speeds can't tunnel through trigger windows
- CIC-style tactical plot: constant-size icons, 2-minute velocity-projection vectors, 10,000 km grid, scale bar, toggleable weapon range rings
- Annihilator armed per its real MSD loadout: Neutraliser proton beam (1 TJ/shot), 4× 100 GW X-ray lasers, F-AM micromissile waves

### Enemy commander AI (deliberate, not reactive)
- Fleet-level commander designates a priority target (damage, isolation, threat, interstice proximity — herding the fleet off the wormhole, per canon)
- Standoff bombardment doctrine with coordinated multi-vector strike runs every few minutes; bombardment weapons leave the strike target to the strikers
- Railgun suppression response: ships under fire dodge (and a dodging ship cannot aim its spinal duster — Ngoni's "keep them dodging" is the literal mechanic), mass torpedo launches force squadron-wide evasive dispersal, wounded Incisors break off to long range
- Physics-honest counterplay: laser point-defence kills any torpedo tracked >150 s, so only fresh-geometry launches at inbound ships survive; a 30 G charge can only deviate ~1,500 km in 100 s, so the dived-on battlegroup is the one that can make the Isidore's choice

### New systems
- Four opposing-force scenarios (1 Incisor / 2 / historical 3+Annihilator / 4+Annihilator), persisted across restarts
- Railgun target designation [R] alongside torpedo volleys, with per-group fire-control state
- Enemy intel panel: click any contact for its real spec sheet, estimated hull, velocity/acceleration readout, and current behaviour state (STRIKE RUN — INBOUND, EVADING SUPPRESSION FIRE, BREAKING OFF…)
- Balance verified headless: passive play = annihilation with zero kills; scripted competent play reproduces history (1 kill with two more Incisors crippled); micro-tests confirm each kill path

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
