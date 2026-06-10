# Ascent Universe

A companion website for the Ascent Universe — a science fiction setting spanning from deep Dyn prehistory (~100,000 BCE) to the far-future Apathy War (~3200 CE).

## Authorship

The Ascent Universe is a human-authored science fiction project. The original novels and short stories were written by the author over several years. Some newer short stories and editorial work on this site were done collaboratively with Claude (Anthropic).

| Attribution | Meaning |
|-------------|---------|
| **Human** | Written entirely by the author |
| **AI-assisted** | Plotted by the author, drafted/expanded collaboratively with Claude |
| **AI-edited** | Human-written original, with AI-assisted revision and assembly |

### Stories by attribution

| Story | Date | Attribution |
|-------|------|-------------|
| Frameshift | ~100,000 BCE | Human |
| The Other Moon | ~100,000 BCE | Human |
| Seeker | ~100,000 BCE | Human |
| The Facilitator | 2078 CE | Human |
| **Inheritor** | 2085 CE | **AI-assisted** |
| The Utilitaria | 2112 CE | Human |
| Starwhisp | 2310 CE | Human |
| **The Last Duty** | 2314 CE | **AI-assisted** |
| The Director | 2432 CE | Human |
| Ascent (novel) | 2479 CE | Human |
| **Headhunted** | 2480 CE | **AI-assisted** |
| **The Worlds Within** | 2736 CE | **AI-assisted** |
| Threshold | 2909 CE | Human |
| Eszel & The Listener (novel) | 2909–2937 CE | Human, **AI-edited** |
| **The Sixty Percent** | ~3150 CE | **AI-assisted** |
| Bows and Arrows Against the Lightning | ~3200 CE | Human |
| The War of All Wars | ~3200 CE | Human |
| **Oblivion** | 3221 CE | **AI-assisted** |

The website itself (HTML/CSS/JS, interactive readers, MSD, battle simulation, codex, etc.) was built collaboratively with Claude.

## Live Site

Hosted via GitHub Pages. All pages are static HTML/CSS/JS with no build step. Two display modes:
- **Dark mode** — terminal/military-intelligence aesthetic (monospace, cyan/orange)
- **Light mode** — clean, simple reading mode (system fonts, minimal decoration)

Toggle using the theme button in the nav bar.

## Pages

### Core Pages

| Page | File | Description |
|------|------|-------------|
| **Home** | `index.html` | Hub page with navigation cards |
| **Stories** | `stories.html` | Chronological index of all fiction with attribution |
| **Reader** | `reader.html` | Lightweight markdown/text reader for source texts |
| **Drafts** | `drafts.html` | Draft browser for second-draft manuscripts |
| **MSD (Annihilator)** | `msd.html` | Interactive 3D MSD for the Annihilator-class IP Assault Vehicle |
| **MSD (D-Sphere)** | `msd-dsphere.html` | Interactive 3D MSD for the Ultimate Height-class Defence Sphere |
| **Threshold: First Fleet** | `threshold-game.html` | Playable real-time strategy game — command Union's First Fleet at the Battle of Threshold (2909 CE) |
| **Battle** | `battle.html` | Phase-by-phase animated tactical reconstruction of the Battle of the Interstice |
| **Science** | `science.html` | Science Compendium — real physics behind the fictional technology |
| **Timeline** | `timeline.html` | Interactive chronology from Deep Antiquity to the Apathy War |
| **Codex** | `codex.html` | Intelligence dossiers on factions, personnel, vessels, and threats |
| **Worlds** | `worlds.html` | Atmospheric profiles of major settings and epochs |
| **Threads** | `threads.html` | Character threads across all stories, colour-coded by entity |

### Interactive / AI Pages

| Page | File | Description |
|------|------|-------------|
| **Facilitator** | `facilitator.html` | Facilitator canon analysis, comparison to modern AI, interactive chat |
| **Utilitaria** | `utilitaria.html` | Utilitaria canon analysis and philosophical exploration |
| **Emissary Chat** | `utilitaria-chat.html` | Interactive diplomatic channel chat with the Utilitaria |
| **AI Analysis** | `ai-analysis.html` | Comparative analysis of Facilitator vs Utilitaria vs Apathy AI systems |
| **Anthropic Trap** | `anthropic-trap.html` | Interactive exploration of the Apathy's anthropic trap argument |
| **Insights** | `insights-report.html` | Claude Code usage analytics and workflow insights (standalone, not themed) |

### Visualisations

| Page | File | Description |
|------|------|-------------|
| **Orrery** | `orrery.html` | Interactive solar system orrery |
| **Interstice Network** | `interstice-map.html` | 3D canvas visualisation of the wormhole network |
| **Diamond Duster** | `diamond-duster.html` | Animated weapon firing sequence with HUD telemetry |
| **Liberation Day** | `liberation.html` | Animated warseed activation sequence from Ascent (2479 CE) |
| **Ascensor** | `ascensor.html` | Interactive orbital tether cross-section, surface to Dyn firmament |
| **Warseed Schematic** | `warseed.html` | Ocean floor weapon system cutaway with activation sequence |
| **Threshold Breach** | `threshold-breach.html` | Animated 2909 CE interstice breach and fleet engagement |
| **A-Sphere Cockpit** | `asphere-combat.html` | Interactive combat HUD — pilot an A-sphere against Apathy targets |
| **Apathy Approach** | `apathy-approach.html` | Long-range sensor display tracking an approaching berserker machine |
| **Simulations Hub** | `simulations.html` | Categorised index of all 17 tactical and interactive simulations |
| **Interstice Transit** | `interstice-transit.html` | First-person wormhole passage through dodecahedral cage |
| **Isidore's Charge** | `isidore-charge.html` | CIC simulation of the USS Isidore's 30G suicide charge |
| **Wasteland Traverse** | `wasteland-crawler.html` | Atmospheric journey through alien wasteland on occupied Earth |
| **Utilitaria Escape** | `utilitaria-escape.html` | LED modulation breakout from Pantheon geostationary station |
| **Fleet Bridge** | `bridge-tactical.html` | Virtual CIC of the Ultimate Height during Apathy engagement |

### In-Universe Documents

| Page | File | Description |
|------|------|-------------|
| **Reflections** | `reflections.html` | "The Reflections of Seeker" — Dyn philosophical text |

### Story Readers

| File | Story | Era |
|------|-------|-----|
| `seeker-story.html` | Seeker | ~100,000 BCE |
| `inheritor-story.html` | Inheritor | 2085 CE |
| `sixty-percent-story.html` | The Sixty Percent | ~3150 CE |
| `worlds-within-story.html` | The Worlds Within | 2736 CE |
| `headhunted-story.html` | Headhunted | 2480 CE |
| `oblivion-story.html` | Oblivion | 3221 CE |

## Shared Resources

- `style.css` — Shared theme with dark and light modes
- `nav.js` — Injected navigation bar, theme toggle, status bar, and in-universe clock

## Reference Documents

- **`UNIVERSE_REFERENCE.md`** — Comprehensive reference: synopses, characters, factions, technology, themes, continuity
- **`BRAINSTORMING.md`** — Development log and notes
- **`AI_ADVICE.md`** — Practical advice for AI models working on this project

## AI Collaboration

This project was built collaboratively with Claude Code (Anthropic). The following files guide AI sessions:

- **`CLAUDE.md`** — Project conventions, creative writing guidelines, and git procedures
- **`AI_ADVICE.md`** — Detailed advice for AI models working on this universe
- **`insights-report.html`** — Usage analytics and workflow insights from Claude Code sessions

### Key procedures for AI collaborators

1. **Read `AI_ADVICE.md` and `UNIVERSE_REFERENCE.md` before creative work** — canon consistency matters
2. **Commit after every chapter, page, or section** — never batch to the end
3. **Creative rewrites: expand, never cut** — preserve texture, atmosphere, and subtext
4. **Re-read files before editing** — special characters (smart quotes, em dashes) cause mismatches
5. **Report word counts** before and after any rewrite

## Development

No build step needed — edit HTML files directly and push. The `msd/` directory contains a separate React/Vite project for the MSD component.
