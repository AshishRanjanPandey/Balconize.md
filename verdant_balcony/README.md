# 🌱 Balconize (Pro-Tier Edition)
### *Turn Any Apartment Balcony Into a High-Yield Vertical Micro-Farm*

> **Hackathon Theme:** *"Touch Grass"* — Open-source AI that gets people off their screens and out into the physical world, making the screen the shortest part of the daily experience.

---

## 🌟 1. Project Overview & Core Value Proposition

**Balconize** is a lightning-fast, 100% local, private, zero-cost Streamlit application running on open-weight models (via [Ollama](https://ollama.ai)) paired with an independent per-zone agro-ecological rule engine. It translates apartment balcony parameters, sunlight hours, and seasonal angles into an exact, professional vertical-stacking and container arrangement blueprint.

- **Zero Cloud Costs ($0.00):** No external API keys (OpenAI, Anthropic, or Google) required.
- **100% Private On-Device Inference:** Balcony dimensions, geolocation hints, and household data never leave your computer.
- **Fail-Safe Deterministic Fallback:** If Ollama is offline or uninstalled, Balconize automatically transitions to an instant, structured agronomic matching engine using `plants_database.json`. The demo never fails.
- **Touch Grass Ethos:** Rather than keeping users glued to infinite digital dashboards, Balconize generates a high-contrast, physical outdoor action plan designed to be exported in seconds so users can step outside, touch soil, and cultivate real food.

---

## 🏗️ 2. Architectural Blueprint & File Tree

```
verdant_balcony/
│
├── app.py                  # Pro-tier Balconize UI, bento-grid zoning, city presets & Touch Grass challenge
├── model_service.py        # Ollama connector with fast socket checks & per-zone agro-engine
├── plants_database.json    # Local JSON database of 12 crops, solar vectors, and companion rules
├── requirements.txt        # Python dependencies (streamlit, ollama, pandas)
└── README.md               # Documentation highlighting open-source privacy and local utility
```

### Component Breakdown

| Component | Responsibility |
| :--- | :--- |
| **`app.py`** | Bento-grid UI, one-click city presets, telemetry KPI cards, interactive 2D architectural schematic, gamified weekly Touch Grass challenges, and export module. |
| **`model_service.py`** | Hybrid AI connector supporting local open weights (`phi3`, `gemma:2b`, `llama3.2`, `mistral`) with sub-millisecond socket health-checks and an independent per-zone agro-engine. |
| **`plants_database.json`** | 12 urban-optimized balcony crops (Mint, Coriander, Spinach, Radish, Cherry Tomatoes, Thai Chili, Lettuce, Thyme, Basil, Spring Onion, Strawberries, Dwarf Bell Pepper), sunlight exposure matrices, and companion guilds. |
| **`requirements.txt`** | Minimal, modern Python dependency specification. |

---

## 📐 3. The 3-Tier Vertical Zoning Framework

Balconize arranges crops across three distinct spatial zones to optimize sunlight capture, prevent container shading, and anchor heavy wind loads:

```
☀️ DIRECT SOLAR ANGLE VECTOR  ===> [Facing: South/East/West/North | Season: Cycle]
─────────────────────────────────────────────────────────────────────────────
▲ OPEN SKYLINE HORIZON (UNOBSTRUCTED)
│
│   [ ZONE 1: FRONT RAILING / HANGING BASKETS ] ────────── (Elevation: +3.5 to +6.5 ft)
│   • Plant Blueprint: Cascading Strawberries, Creeping Thyme, Thai Chili, Spearmint
│   • Containers: Railing saddle planters, coco-coir hanging baskets (6-8" depth)
│   • Role: Horizon light capture; trailing foliage cascades down; wind-hardy.
│
│       │
│       ▼ (Filtered / Ambient Sunlight Gradient)
│
│   [ ZONE 2: MID-TIER RAIL GRID & WALL VERTICAL ] ────── (Elevation: +1.5 to +3.5 ft)
│   • Plant Blueprint: Baby Spinach, Cilantro, Butterhead Lettuce, Spring Onion
│   • Containers: Tiered ladder planters, felt wall pockets (7-9" depth)
│   • Role: Sheltered from harsh gusts; ideal for daily cut-and-come-again harvest.
│
│       │
│       ▼ (Thermal Masonry Storage & Ground Stability)
│
│   [ ZONE 3: FLOOR & DEEP CORNER POTS ] ──────────────── (Deck Floor: 0.0 ft)
│   • Plant Blueprint: Balcony Cherry Tomatoes, French Radish, Mini Bell Pepper
│   • Containers: 12-14" heavy terracotta or 7-gallon fabric grow bags
│   • Role: Low center of gravity; deep root anchorage; high thermal mass.
─────────────────────────────────────────────────────────────────────────────
🚪 INTERIOR APARTMENT DOOR  (Close Laptop • Step Outside • Breathe Fresh Air)
```

---

## ⚡ 4. Quickstart & Installation

### Prerequisites
- Python 3.10+
- *(Optional, for LLM mode)* [Ollama](https://ollama.ai) installed with `phi3` or `gemma:2b`:
  ```bash
  ollama run phi3
  # or
  ollama run gemma:2b
  ```

### Step 1: Run the App
```bash
# From workspace root:
python run.py

# Or via streamlit:
streamlit run verdant_balcony/app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🏙️ 5. One-Click City Balcony Presets

Balconize includes built-in one-click presets for rapid testing and demonstrations:
- ☀️ **Mediterranean Sun Trap:** South-facing, 8.5h sun, heavy summer nightshades.
- 🌅 **Tokyo Morning Studio:** East-facing, 4.5h sun, compact spring leafy greens.
- 🔥 **High-Rise Sunset Deck:** West-facing, 6.5h sun, heat-resilient Mediterranean herbs.
- ❄️ **Nordic Winter Terrace:** North-facing, 2.5h sun, cold-hardy winter greens and roots.

---

## 🔒 6. Open-Source Privacy Guarantee

| Dimension | Balconize Standard | Typical Cloud AI Apps |
| :--- | :--- | :--- |
| **Cloud Telemetry** | **0 Bytes (100% Offline)** | Continuous tracking |
| **API Costs** | **$0.00 Lifetime** | Recurring subscription / tokens |
| **Privacy** | **100% Local Device** | Data stored on remote servers |
| **Network Reliance** | **Works without internet** | Fails without connectivity |

---

*Built with ❤️ for Hacktoberfest & the Touch Grass Hackathon.*
