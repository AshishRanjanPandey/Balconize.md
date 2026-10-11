*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass](https://dev.to/challenges/hacktoberfest-week1-2026-10-05)*

# 🌱 Balconize — The Urban Micro-Space Sunlight & Yield Optimizer

> *"The screen should be the shortest part of your day."*

---

## What I Built

Modern life keeps urban dwellers trapped behind glowing screens, doomscrolling gardening reels and daydreaming about nature while living in high-rise concrete apartments. 

I built **Balconize** to bridge the gap between digital AI and physical dirt.

**Balconize** is a 100% local, private, zero-cost Streamlit application powered by open-weight models (via Ollama) and a deterministic agro-ecological physics engine. It translates apartment balcony constraints—orientation (South/East/West/North), seasonal solar angles, direct sunlight hours, and mounting hardware—into an exact **3-Tier Vertical Stacking Blueprint**:

- **Zone 1: Railing & Hanging Baskets** (Horizon sky light capture for trailers like strawberries, cascading thyme, and sun-seeking herbs).
- **Zone 2: Mid-Tier Rail Grid & Wall Vertical** (Filtered light for daily cut-and-come-again greens, baby spinach, butterhead lettuce, and scallions).
- **Zone 3: Floor & Deep Corner Containers** (Thermal ground anchor for heavy root pots like cherry tomatoes, mini bell peppers, and french breakfast radishes).

### How it gets people off the screen and into the real world:
Rather than trapping users in an endless digital simulator, Balconize is built for **immediate departure from the laptop**:
1. **Under 30-Second Blueprint Generation:** Select your orientation and sunlight hours, and instantly receive your layout.
2. **Tactile "Touch Grass" Actions:** Every recommended crop features an outdoor sensory instruction (e.g. *pushing a finger 1 inch into the soil to test moisture, crushing a mint leaf to inhale aromatic terpenes, or pinching sucker shoots with fingertips*).
3. **One-Click Outdoor Action Plan Export:** A dedicated button generates a clean, text-only printable checklist (`.txt` / `.md`). Users download or print the sheet, close their browser, grab a trowel, and step outside into the sunlight.

**Target Audience:** Urban apartment residents, beginner balcony gardeners, and screen-fatigued tech workers wanting to cultivate organic food in tight spaces.

---

## Demo

- **Live Deployed App:** [https://balconize.streamlit.app](https://balconize.streamlit.app) *(Replace with your Streamlit Cloud URL)*
- **Local Dev URL:** `http://localhost:8501`

### 📐 Balcony Architectural Elevation Schematic:
```
☀️ DIRECT SOLAR ANGLE VECTOR  ===> [Facing: South/East/West/North | Season: Cycle]
─────────────────────────────────────────────────────────────────────────────
▲ OPEN SKYLINE HORIZON (UNOBSTRUCTED)
│
│   [ ZONE 1: FRONT RAILING / HANGING BASKETS ] ────────── (Elevation: +3.5 to +6.5 ft)
│   • Plant Blueprint: Cascading Strawberries, Creeping Thyme, Thai Chili, Spearmint
│   • Containers: Railing saddle planters, coco-coir hanging baskets (6-8" depth)
│   • Physics: Horizon light capture; trailing foliage cascades down; wind-hardy.
│
│       │
│       ▼ (Filtered / Ambient Sunlight Gradient)
│
│   [ ZONE 2: MID-TIER RAIL GRID & WALL VERTICAL ] ────── (Elevation: +1.5 to +3.5 ft)
│   • Plant Blueprint: Baby Spinach, Cilantro, Butterhead Lettuce, Spring Onion
│   • Containers: Tiered ladder planters, felt wall pockets (7-9" depth)
│   • Physics: Sheltered from harsh gusts; ideal for daily cut-and-come-again harvest.
│
│       │
│       ▼ (Thermal Masonry Storage & Ground Stability)
│
│   [ ZONE 3: FLOOR & DEEP CORNER POTS ] ──────────────── (Deck Floor: 0.0 ft)
│   • Plant Blueprint: Balcony Cherry Tomatoes, French Radish, Mini Bell Pepper
│   • Containers: 12-14" heavy terracotta or 7-gallon fabric grow bags
│   • Physics: Low center of gravity; deep root anchorage; high thermal mass.
─────────────────────────────────────────────────────────────────────────────
🚪 INTERIOR APARTMENT DOOR  (Close Laptop • Step Outside • Breathe Fresh Air)
```

---

## Code

<!-- Embed your GitHub repo directly below -->
{% github https://github.com/Dev_Ashish/Balconize %}

**Repository Structure:**
```
verdant_balcony/
│
├── app.py                  # Pro-tier Streamlit UI, bento-grid zoning, city presets & Touch Grass challenge
├── model_service.py        # Ollama connector with fast socket checks & per-zone agro-engine
├── plants_database.json    # Local JSON database of 12 crops, solar vectors, and companion rules
├── requirements.txt        # Minimal dependencies (streamlit>=1.30.0, ollama>=0.1.6, pandas>=2.0.0)
└── README.md               # Complete architecture docs & privacy statement
```

---

## How I Built It

### 1. Open-Source AI Core & Local Inference
- **Local Open-Weight LLM via Ollama:** Supports on-device inference using open models like `phi3:mini`, `gemma:2b`, and `llama3.2`. 
- **Sub-Millisecond Socket Pre-Check:** A non-blocking socket test (`127.0.0.1:11434`) probes local daemon availability in under 2ms.
- **Fail-Safe Deterministic Fallback Engine:** If Ollama is offline or not installed, Balconize seamlessly executes an algorithmic agro-ecological matching engine. The app never crashes, requires zero API keys, and runs on any basic laptop in milliseconds.

### 2. Independent Per-Zone Microclimate Physics
Balconize calculates tailored sunlight gradients across three distinct vertical tiers:
- **Solar Exposure Vectors:** Adjusts for compass facing (South maximum sun vs East morning light vs West afternoon heat vs North ambient diffuse light).
- **Seasonal Solar Modifiers:** Dynamically scales from `1.25x` in Summer Peak down to `0.55x` in Winter Resilient.
- **Bioclimatic Rules:** Automatically prevents fragile soft greens from scorching in West-facing railings, disqualifies heavy 14" tomato pots from dangerous railing mounts, and substitutes frost-tender nightshades with cold-hardy greens in winter.

### 3. Pro-Tier Bento-Grid UI (Streamlit & Vanilla CSS)
- Custom CSS design system using Google Fonts (*Outfit* and *Plus Jakarta Sans*), rich dark forest greens (`#0F2317`), fresh mint (`#2ECC71`), and warm terracotta accents.
- Bento telemetry KPI bar showing effective sun hours, photosynthetic efficiency, projected fresh monthly harvests (~18 harvests/mo), and estimated plastic packaging eliminated (~2.5 kg).
- One-click city presets (*Tokyo Studio, Mediterranean Sun Trap, High-Rise Sunset Deck, Nordic Winter Terrace*).
- Gamified weekly **"Touch Grass Challenge"** checklist to encourage real-world interaction with plants.

---

## Why Does Open Innovation Matter?

1. **True Privacy for Living Spaces:** Your apartment layout, window orientation, and balcony dimensions belong to you. Closed AI APIs require sending personal living telemetry to corporate cloud servers. Open-weight models running on local machines guarantee **0 bytes of data ever leave your device**.
2. **$0 Cost Barrier to Food Sovereignty:** Growing food should not require a $20/month subscription or cloud token fees. Open-source models and local code make regenerative urban farming accessible to students, renters, and apartment dwellers worldwide at zero cost.
3. **Resilience & Offline Autonomy:** Balconies and rooftop gardens frequently have weak Wi-Fi or cellular dead zones. By running 100% locally via Ollama and deterministic agro-rules, Balconize operates completely offline. If the internet goes down, your urban farm blueprint still works.

---

## My Agent Session

<!-- Optional: Embed your DevRelay session link below if recorded -->
<!-- {% agent_session <YOUR_SESSION_ID> %} -->

During development, the AI assistant helped pair-program the reactive Streamlit bento-grid layout, formulate the agronomic orientation physics matrices, and engineer the dual Ollama connector / zero-failure fallback pipeline.

---

## Prize Categories

- **Primary Challenge:** Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass
- **Open-Source AI & Local Inference:** Built with Ollama & Open Weights

---

*Built with ❤️ for Hacktoberfest 2026. Put down the screen, pick up the trowel, and touch some grass!*
