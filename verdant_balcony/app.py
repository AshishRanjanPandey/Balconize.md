"""
Balconize — The Urban Micro-Space Sunlight & Yield Optimizer
Pro-Tier Streamlit Application with Bento-Grid Design System & Local AI/Algorithmic Engine
"""

import streamlit as st
import json
import time
import pandas as pd
import importlib

import model_service
importlib.reload(model_service)

# ==============================================================================
# 1. PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Balconize — Urban Sunlight & Yield Optimizer",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. PRO-TIER DESIGN SYSTEM & CUSTOM CSS
# ==============================================================================
CUSTOM_CSS = """
<style>
/* -------------------------------------------------------------
   Typography & Global Design Variables
   ------------------------------------------------------------- */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg-dark: #0A140D;
    --forest-deep: #0F2317;
    --forest-card: #142E1F;
    --mint-vibrant: #2ECC71;
    --mint-glow: #10B981;
    --mint-soft: rgba(46, 204, 113, 0.12);
    --amber-warm: #F59E0B;
    --terracotta-warm: #E07A5F;
    --text-primary: #0F172A;
    --text-muted: #64748B;
    --card-radius: 16px;
    --transition-smooth: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

h1, h2, h3, h4, .brand-font {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800;
}

/* Hide streamlit clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Container layout */
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 1320px !important;
}

/* -------------------------------------------------------------
   Pro Hero Banner
   ------------------------------------------------------------- */
.hero-wrapper {
    background: linear-gradient(135deg, #0D2315 0%, #153822 50%, #09190E 100%);
    border: 1px solid rgba(46, 204, 113, 0.3);
    border-radius: 22px;
    padding: 2.2rem 2.6rem;
    color: #FFFFFF;
    margin-bottom: 1.6rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 16px 40px rgba(10, 26, 15, 0.28);
}

.hero-wrapper::after {
    content: "🌱";
    font-size: 14rem;
    position: absolute;
    right: -2.5rem;
    bottom: -4.5rem;
    opacity: 0.07;
    pointer-events: none;
}

.hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(46, 204, 113, 0.16);
    border: 1px solid rgba(46, 204, 113, 0.4);
    color: #34D399;
    font-size: 0.76rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    padding: 5px 13px;
    border-radius: 999px;
    margin-bottom: 0.8rem;
}

.hero-title {
    font-size: 2.65rem;
    font-weight: 900;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin: 0 0 0.5rem 0;
    background: linear-gradient(110deg, #FFFFFF 35%, #A7F3D0 80%, #34D399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: #CBD5E1;
    max-width: 760px;
    line-height: 1.55;
    margin-bottom: 1.3rem;
}

/* Pulsing Status Badges */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border-radius: 10px;
    font-size: 0.83rem;
    font-weight: 700;
    backdrop-filter: blur(8px);
}

.status-active {
    background: rgba(16, 185, 129, 0.2);
    border: 1px solid rgba(16, 185, 129, 0.6);
    color: #A7F3D0;
}

.status-fallback {
    background: rgba(245, 158, 11, 0.2);
    border: 1px solid rgba(245, 158, 11, 0.6);
    color: #FDE68A;
}

/* -------------------------------------------------------------
   Preset Selector Bar
   ------------------------------------------------------------- */
.preset-card-box {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 10px 16px;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
}

/* -------------------------------------------------------------
   KPI Bento Highlights
   ------------------------------------------------------------- */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    transition: var(--transition-smooth);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(46, 204, 113, 0.15);
    border-color: rgba(46, 204, 113, 0.5);
}

.kpi-label {
    font-size: 0.74rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #64748B;
    margin-bottom: 4px;
}

.kpi-value {
    font-size: 1.8rem;
    font-weight: 900;
    color: #0F2317;
    line-height: 1.15;
}

.kpi-sub {
    font-size: 0.78rem;
    color: #059669;
    font-weight: 700;
    margin-top: 5px;
}

/* -------------------------------------------------------------
   Zoning Bento-Grid Cards
   ------------------------------------------------------------- */
.zone-header-box {
    border-radius: 16px;
    padding: 1.3rem 1.4rem;
    margin-bottom: 1rem;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
}

.zone-1-header {
    background: linear-gradient(135deg, #123320 0%, #1E5033 100%);
    border-left: 6px solid #2ECC71;
}

.zone-2-header {
    background: linear-gradient(135deg, #182C22 0%, #2A4736 100%);
    border-left: 6px solid #34D399;
}

.zone-3-header {
    background: linear-gradient(135deg, #2B211A 0%, #483427 100%);
    border-left: 6px solid #E07A5F;
}

.zone-badge-pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    background: rgba(255, 255, 255, 0.22);
    margin-bottom: 6px;
}

/* Individual Crop Card */
.crop-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 1.25rem;
    margin-bottom: 1.1rem;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
    transition: var(--transition-smooth);
    border-left: 5px solid #2ECC71;
}

.crop-card:hover {
    border-color: #2ECC71;
    transform: translateY(-3px);
    box-shadow: 0 10px 26px rgba(46, 204, 113, 0.16);
}

.crop-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 0.7rem;
}

.crop-icon {
    font-size: 2.1rem;
    line-height: 1;
    background: #F0FDF4;
    padding: 8px;
    border-radius: 12px;
    border: 1px solid #DCFCE7;
}

.crop-title {
    font-size: 1.2rem;
    font-weight: 800;
    color: #0F2317;
    margin: 0;
    line-height: 1.2;
}

.crop-scientific {
    font-size: 0.76rem;
    color: #64748B;
    font-style: italic;
    margin-top: 2px;
}

/* Badge Tags inside Crop Card */
.tag-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 7px;
    margin: 2px 4px 2px 0;
}

.tag-sun {
    background: #FEF3C7;
    color: #92400E;
}

.tag-root {
    background: #EEF2FF;
    color: #3730A3;
}

.tag-water {
    background: #E0F2FE;
    color: #0369A1;
}

.tag-harvest {
    background: #DCFCE7;
    color: #166534;
}

.tag-season {
    background: #F3E8FF;
    color: #6B21A8;
}

.tag-difficulty {
    background: #F1F5F9;
    color: #334155;
}

.crop-touch-grass-box {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-left: 3px solid #10B981;
    border-radius: 0 10px 10px 0;
    padding: 9px 12px;
    font-size: 0.81rem;
    color: #334155;
    margin-top: 0.75rem;
    line-height: 1.45;
}

/* -------------------------------------------------------------
   Companion Synergy Cards
   ------------------------------------------------------------- */
.synergy-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.9rem;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    transition: var(--transition-smooth);
}

.synergy-card:hover {
    border-color: #2ECC71;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(46, 204, 113, 0.12);
}

.synergy-icon-wrap {
    font-size: 1.6rem;
    background: #ECFDF5;
    padding: 8px 12px;
    border-radius: 10px;
    border: 1px solid #D1FAE5;
}

/* -------------------------------------------------------------
   Touch Grass Outdoor Export Box
   ------------------------------------------------------------- */
.touch-grass-export-box {
    background: linear-gradient(135deg, #0D2315 0%, #194628 100%);
    border: 1px solid rgba(46, 204, 113, 0.45);
    border-radius: 20px;
    padding: 2rem;
    color: #FFFFFF;
    margin-top: 1.8rem;
    box-shadow: 0 12px 35px rgba(10, 26, 15, 0.25);
}

/* -------------------------------------------------------------
   Schematic Visualizer Box
   ------------------------------------------------------------- */
.schematic-box {
    background: #09150E;
    border: 1px solid rgba(46, 204, 113, 0.35);
    border-radius: 16px;
    padding: 1.6rem;
    color: #E2E8F0;
    font-family: monospace;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

/* -------------------------------------------------------------
   Open-Source Footer
   ------------------------------------------------------------- */
.footer-badge-box {
    background: #FAF6F0;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin-top: 2.8rem;
    text-align: center;
}

.footer-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #FFFFFF;
    border: 1px solid #D1D5DB;
    padding: 5px 13px;
    border-radius: 999px;
    font-size: 0.77rem;
    font-weight: 700;
    color: #334155;
    margin: 4px;
}

/* Primary Action Button */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #2ECC71 0%, #10B981 100%) !important;
    color: #041F0E !important;
    font-weight: 800 !important;
    font-size: 1.08rem !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.8rem 2rem !important;
    box-shadow: 0 6px 22px rgba(46, 204, 113, 0.38) !important;
    transition: var(--transition-smooth) !important;
    width: 100% !important;
}

div.stButton > button:first-child:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 30px rgba(46, 204, 113, 0.55) !important;
    color: #021207 !important;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ==============================================================================
# 3. HELPER FUNCTIONS & STATE
# ==============================================================================
@st.cache_data(ttl=10)
def get_cached_ollama_status():
    return model_service.check_ollama_status()

# Balcony Presets dictionary
PRESETS = {
    "🛠️ Custom Architecture": None,
    "☀️ Mediterranean Sun Trap (South, 8.5h, Summer)": {
        "facing": "South", "hours": 8.5, "season": "Summer Peak", "size": "Standard (30-50 sq ft)",
        "hardware": ["Railings", "Hanging Mounts", "Wall Hooks / Trellis", "Floor Space"]
    },
    "🌅 Tokyo Morning Studio (East, 4.5h, Spring)": {
        "facing": "East", "hours": 4.5, "season": "Spring Kickoff", "size": "Compact (15-25 sq ft)",
        "hardware": ["Railings", "Wall Hooks / Trellis", "Floor Space"]
    },
    "🔥 High-Rise Sunset Deck (West, 6.5h, Summer)": {
        "facing": "West", "hours": 6.5, "season": "Summer Peak", "size": "Spacious Terrace (60+ sq ft)",
        "hardware": ["Railings", "Hanging Mounts", "Floor Space"]
    },
    "❄️ Nordic Winter Terrace (North, 2.5h, Winter)": {
        "facing": "North", "hours": 2.5, "season": "Winter Resilient", "size": "Standard (30-50 sq ft)",
        "hardware": ["Railings", "Wall Hooks / Trellis", "Floor Space"]
    }
}

# ==============================================================================
# 4. SIDEBAR CONFIGURATION HUB
# ==============================================================================
with st.sidebar:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.6rem;">
            <span style="font-size: 2.3rem;">🌱</span>
            <div>
                <h2 style="margin: 0; color: #0F2317; line-height: 1.05; letter-spacing: -0.02em;">Balconize</h2>
                <span style="font-size: 0.74rem; color: #10B981; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em;">Touch Grass Pro</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.caption("Turn any apartment balcony into a high-yield vertical micro-farm.")
    st.markdown("---")

    st.markdown("#### ⚡ 1. One-Click City Presets")
    selected_preset_name = st.selectbox(
        "Load Urban Balcony Preset:",
        options=list(PRESETS.keys()),
        index=0,
        help="Quickly populate typical urban balcony conditions for instant testing."
    )
    preset_data = PRESETS.get(selected_preset_name)

    # Orientation
    facing_options = ["South", "South-East", "East", "South-West", "West", "North-East", "North-West", "North"]
    default_facing_idx = facing_options.index(preset_data["facing"]) if preset_data else 0

    st.markdown("#### 📐 2. Physical Balcony Specs")
    balcony_facing = st.selectbox(
        "Balcony Facing (Orientation):",
        options=facing_options,
        index=default_facing_idx,
        help="Sun angle, thermal masonry absorption, and wind load vary directly by orientation."
    )

    col_size, col_month = st.columns(2)
    with col_size:
        size_options = ["Compact (15-25 sq ft)", "Standard (30-50 sq ft)", "Spacious Terrace (60+ sq ft)"]
        default_size_idx = size_options.index(preset_data["size"]) if preset_data else 1
        balcony_size = st.selectbox(
            "Balcony Size:",
            options=size_options,
            index=default_size_idx
        )
    with col_month:
        season_options = ["Spring Kickoff", "Summer Peak", "Autumn Harvest", "Winter Resilient"]
        default_season_idx = season_options.index(preset_data["season"]) if preset_data else 0
        current_season = st.selectbox(
            "Season / Cycle:",
            options=season_options,
            index=default_season_idx
        )

    default_sun_val = preset_data["hours"] if preset_data else 6.5
    sunlight_hours = st.slider(
        "Direct Sunlight Hours / Day:",
        min_value=1.0,
        max_value=10.0,
        value=float(default_sun_val),
        step=0.5,
        help="Average hours direct sunlight strikes the balcony railing or floor deck."
    )

    st.markdown("#### 🛠️ 3. Available Mounting Hardware")
    col_hw1, col_hw2 = st.columns(2)
    with col_hw1:
        hw_railings = st.checkbox("Front Railings", value=True)
        hw_hanging = st.checkbox("Hanging Mounts", value=True)
    with col_hw2:
        hw_wall = st.checkbox("Wall Hooks / Trellis", value=True)
        hw_floor = st.checkbox("Corner Floor Space", value=True)

    hardware_selected = []
    if hw_railings: hardware_selected.append("Railings")
    if hw_hanging: hardware_selected.append("Hanging Mounts")
    if hw_wall: hardware_selected.append("Wall Hooks / Trellis")
    if hw_floor: hardware_selected.append("Floor Space")
    if not hardware_selected:
        hardware_selected = ["Railings", "Floor Space"]

    st.markdown("#### 🥗 4. Crop Preferences")
    category_choices = st.multiselect(
        "Preferred Crop Types:",
        options=["Herbs & Aromatics", "Leafy Greens", "Vegetables & Fruiting", "Roots & Fast Yields"],
        default=["Herbs & Aromatics", "Leafy Greens", "Vegetables & Fruiting"]
    )
    if not category_choices:
        category_choices = ["Herbs & Aromatics", "Leafy Greens", "Vegetables & Fruiting"]

    experience_level = st.select_slider(
        "Gardening Skill Level:",
        options=["Beginner", "All Levels", "Intermediate"],
        value="Beginner"
    )

    st.markdown("---")
    st.markdown("#### 🧠 5. Local AI Inference Node")

    ollama_info = get_cached_ollama_status()
    is_ollama_online = ollama_info["is_available"]

    model_options = ["Auto-Detect (phi3 / gemma / llama)", "Deterministic Agro-Engine Only"]
    if is_ollama_online and ollama_info["available_models"]:
        model_options = ollama_info["available_models"] + ["Deterministic Agro-Engine Only"]

    chosen_model = st.selectbox(
        "Inference Engine:",
        options=model_options,
        index=0,
        help="Runs 100% on your machine. $0 cloud cost, zero data telemetry."
    )

    if st.button("🔄 Test Ollama Local Node Link", use_container_width=True):
        st.cache_data.clear()
        updated_status = model_service.check_ollama_status()
        if updated_status["is_available"]:
            st.success(f"🟢 Ollama Local Node Connected! Models: {', '.join(updated_status['available_models']) or 'phi3'}")
        else:
            st.info("⚡ Ollama daemon is offline or not installed. Balconize is operating in 100% Deterministic Agro-Ecological Engine mode!")

# Build active parameters dict
current_params = {
    "balcony_facing": balcony_facing,
    "sunlight_hours": sunlight_hours,
    "hardware": hardware_selected,
    "balcony_size": balcony_size,
    "experience_level": experience_level,
    "categories": category_choices,
    "season": current_season,
    "chosen_model": chosen_model
}

# ==============================================================================
# 5. MAIN DASHBOARD: HERO SECTION & LIVE STATUS
# ==============================================================================
ollama_status = get_cached_ollama_status()
is_llm_active = (
    ollama_status["is_available"] 
    and chosen_model != "Deterministic Agro-Engine Only"
)

if is_llm_active:
    badge_html = f'<span class="status-badge status-active">🟢 Ollama Local Node Active ({ollama_status.get("suggested_model", "phi3")}) • Zero Cloud Data</span>'
else:
    badge_html = '<span class="status-badge status-fallback">⚡ Algorithmic Agro-Engine Active • 100% Local Fallback • 0ms Latency</span>'

st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-tag">🌱 HACKATHON: TOUCH GRASS PRO EDITION</div>
        <h1 class="hero-title">Balconize</h1>
        <div class="hero-subtitle">
            The Urban Micro-Space Sunlight & Yield Optimizer. Transforms apartment balcony dimensions, solar vectors, 
            and physical container specs into an exact 3-tier vertical blueprint. 
            Designed to get you <strong>off screens and out into the real sunlight</strong>.
        </div>
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 10px;">
            {badge_html}
            <span class="status-badge" style="background: rgba(255,255,255,0.12); color: #FFFFFF;">
                🔒 100% Local Privacy • $0 Cloud Cost
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 6. ACTION TRIGGER & REAL-TIME RE-CALCULATION
# ==============================================================================
col_btn, col_gap = st.columns([1, 0.01])
with col_btn:
    generate_clicked = st.button("🌱 Generate Micro-Farm Architecture", use_container_width=True)

if generate_clicked:
    with st.spinner("Analyzing solar vectors, vertical wind shear, and companion synergies..."):
        time.sleep(0.18)
        st.toast("🌿 Micro-Farm Architecture Blueprint Calculated!", icon="🌱")

# Always evaluate fresh blueprint directly based on active inputs
use_ai = (chosen_model != "Deterministic Agro-Engine Only")
model_name = chosen_model if chosen_model not in ["Auto-Detect (phi3 / gemma / llama)", "Deterministic Agro-Engine Only"] else "phi3"
blueprint = model_service.generate_balcony_blueprint(
    current_params,
    use_ai_if_available=use_ai,
    model_name=model_name
)

zones = blueprint.get("zones", {})
zone_1 = zones.get("zone_1", {})
zone_2 = zones.get("zone_2", {})
zone_3 = zones.get("zone_3", {})
all_crops = zone_1.get("crops", []) + zone_2.get("crops", []) + zone_3.get("crops", [])

# Seasonal Telemetry Banner
season_name = blueprint.get("season", current_season)
season_badge = blueprint.get("season_badge", season_name)
season_thermal = blueprint.get("season_thermal_desc", "")
season_water = blueprint.get("season_water_rule", "")
season_mod = blueprint.get("solar_modifier", 1.0)

st.markdown(f"""
    <div style="background: rgba(46, 204, 113, 0.08); border: 1px solid rgba(46, 204, 113, 0.3); border-radius: 14px; padding: 12px 20px; margin-bottom: 1.3rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
        <div>
            <div style="font-weight: 800; color: #0F2317; font-size: 0.98rem;">{season_badge}</div>
            <div style="font-size: 0.82rem; color: #475569; margin-top: 2px;">{season_thermal} • <strong>Hydration:</strong> {season_water}</div>
        </div>
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 5px 12px; border-radius: 9px; font-size: 0.82rem; font-weight: 800; color: #047857;">
            ☀️ Season Factor: {season_mod}x
        </div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 7. KPI BENTO METRICS BAR
# ==============================================================================
st.markdown("<h3 style='margin-top: 0.8rem; color: #0F2317;'>📊 Micro-Climate Architecture Telemetry</h3>", unsafe_allow_html=True)

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

# Estimated monthly harvests and plastic saved
harvest_est = len(all_crops) * 3
plastic_saved_kg = round(len(all_crops) * 0.45, 1)

with kpi1:
    st.markdown(f"""
        <div class="kpi-card">
            <div>
                <div class="kpi-label">Effective Sun</div>
                <div class="kpi-value">{blueprint.get('effective_sunlight_hours', sunlight_hours)}h</div>
            </div>
            <div class="kpi-sub">{balcony_facing} • {season_name}</div>
        </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
        <div class="kpi-card">
            <div>
                <div class="kpi-label">Solar Efficiency</div>
                <div class="kpi-value">{blueprint.get('sun_utilization_pct', 92)}%</div>
            </div>
            <div class="kpi-sub">Photosynthetic Index</div>
        </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
        <div class="kpi-card">
            <div>
                <div class="kpi-label">Vertical Zones</div>
                <div class="kpi-value">3 Tiers</div>
            </div>
            <div class="kpi-sub">Railing • Mid-Tier • Floor</div>
        </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
        <div class="kpi-card">
            <div>
                <div class="kpi-label">Projected Yield</div>
                <div class="kpi-value">~{harvest_est}</div>
            </div>
            <div class="kpi-sub">Fresh Harvests / Month</div>
        </div>
    """, unsafe_allow_html=True)

with kpi5:
    st.markdown(f"""
        <div class="kpi-card">
            <div>
                <div class="kpi-label">Eco & Privacy</div>
                <div class="kpi-value">0 Bytes</div>
            </div>
            <div class="kpi-sub">~{plastic_saved_kg}kg Plastic Saved</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# 8. BENTO-GRID VERTICAL ZONE RECOMMENDATIONS
# ==============================================================================
st.markdown("<h3 style='color: #0F2317; margin-bottom: 0.2rem;'>🏗️ 3-Tier Vertical Stacking Blueprint</h3>", unsafe_allow_html=True)
st.caption("Arranged to maximize vertical sunlight capture, eliminate container shading, and anchor heavy wind loads.")

tab_blueprint, tab_schematic, tab_synergy, tab_challenge = st.tabs([
    "🏛️ Bento-Grid Zones",
    "📐 2D Balcony Elevation Schematic",
    "🤝 Companion Guilds",
    "🧤 Touch Grass Challenge"
])

with tab_blueprint:
    col_z1, col_z2, col_z3 = st.columns(3)

    # ------------------ ZONE 1 ------------------
    with col_z1:
        st.markdown(f"""
            <div class="zone-header-box zone-1-header">
                <span class="zone-badge-pill">TIER 1 (MAX SUN)</span>
                <h4 style="margin: 0.2rem 0; color: #FFFFFF; font-size: 1.15rem;">{zone_1.get('title', 'Zone 1: Railing & Hanging Baskets')}</h4>
                <div style="font-size: 0.8rem; opacity: 0.9;">{zone_1.get('role', 'Solar Front-Line & Trailing Canopy')}</div>
                <div style="font-size: 0.74rem; margin-top: 0.5rem; background: rgba(0,0,0,0.22); padding: 5px 9px; border-radius: 7px;">
                    📦 {zone_1.get('container_types', 'Railing saddle planters & coco-coir baskets')}
                </div>
            </div>
        """, unsafe_allow_html=True)

        if "ai_advice" in zone_1:
            st.info(f"💡 **AI Node Advice:** {zone_1['ai_advice']}")

        for crop in zone_1.get("crops", []):
            st.markdown(f"""
                <div class="crop-card">
                    <div class="crop-header">
                        <div class="crop-icon">{crop['icon']}</div>
                        <div>
                            <div class="crop-title">{crop['name']}</div>
                            <div class="crop-scientific">{crop['scientific_name']}</div>
                        </div>
                    </div>
                    <div>
                        <span class="tag-pill tag-sun">☀️ {crop['sun_requirement']}</span>
                        <span class="tag-pill tag-root">🪴 {crop['container_depth_inches']}" Depth</span>
                        <span class="tag-pill tag-water">💧 {crop['water_frequency']}</span>
                        <span class="tag-pill tag-harvest">⏱️ {crop['harvest_weeks']}</span>
                        <span class="tag-pill tag-season">🗓️ {season_name}</span>
                        <span class="tag-pill tag-difficulty">🟢 {crop['difficulty']}</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #334155; margin-top: 0.6rem;">
                        <strong>Pairing:</strong> {crop['companion_notes']}
                    </div>
                    <div class="crop-touch-grass-box">
                        <strong>🌿 Touch Grass Action:</strong> {crop['touch_grass_action']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # ------------------ ZONE 2 ------------------
    with col_z2:
        st.markdown(f"""
            <div class="zone-header-box zone-2-header">
                <span class="zone-badge-pill">TIER 2 (MID-HEIGHT)</span>
                <h4 style="margin: 0.2rem 0; color: #FFFFFF; font-size: 1.15rem;">{zone_2.get('title', 'Zone 2: Mid-Tier Rail Grid')}</h4>
                <div style="font-size: 0.8rem; opacity: 0.9;">{zone_2.get('role', 'Vertical Stacking & Micro-Climate')}</div>
                <div style="font-size: 0.74rem; margin-top: 0.5rem; background: rgba(0,0,0,0.22); padding: 5px 9px; border-radius: 7px;">
                    📦 {zone_2.get('container_types', 'Tiered ladder planters & felt wall pockets')}
                </div>
            </div>
        """, unsafe_allow_html=True)

        if "ai_advice" in zone_2:
            st.info(f"💡 **AI Node Advice:** {zone_2['ai_advice']}")

        for crop in zone_2.get("crops", []):
            st.markdown(f"""
                <div class="crop-card">
                    <div class="crop-header">
                        <div class="crop-icon">{crop['icon']}</div>
                        <div>
                            <div class="crop-title">{crop['name']}</div>
                            <div class="crop-scientific">{crop['scientific_name']}</div>
                        </div>
                    </div>
                    <div>
                        <span class="tag-pill tag-sun">☀️ {crop['sun_requirement']}</span>
                        <span class="tag-pill tag-root">🪴 {crop['container_depth_inches']}" Depth</span>
                        <span class="tag-pill tag-water">💧 {crop['water_frequency']}</span>
                        <span class="tag-pill tag-harvest">⏱️ {crop['harvest_weeks']}</span>
                        <span class="tag-pill tag-season">🗓️ {season_name}</span>
                        <span class="tag-pill tag-difficulty">🟢 {crop['difficulty']}</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #334155; margin-top: 0.6rem;">
                        <strong>Pairing:</strong> {crop['companion_notes']}
                    </div>
                    <div class="crop-touch-grass-box">
                        <strong>🌿 Touch Grass Action:</strong> {crop['touch_grass_action']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # ------------------ ZONE 3 ------------------
    with col_z3:
        st.markdown(f"""
            <div class="zone-header-box zone-3-header">
                <span class="zone-badge-pill">TIER 3 (FLOOR ANCHOR)</span>
                <h4 style="margin: 0.2rem 0; color: #FFFFFF; font-size: 1.15rem;">{zone_3.get('title', 'Zone 3: Floor & Deep Corner')}</h4>
                <div style="font-size: 0.8rem; opacity: 0.9;">{zone_3.get('role', 'Thermal Anchor & Heavy Root Haven')}</div>
                <div style="font-size: 0.74rem; margin-top: 0.5rem; background: rgba(0,0,0,0.22); padding: 5px 9px; border-radius: 7px;">
                    📦 {zone_3.get('container_types', '12-14" ceramic pots & 7-gal fabric bags')}
                </div>
            </div>
        """, unsafe_allow_html=True)

        if "ai_advice" in zone_3:
            st.info(f"💡 **AI Node Advice:** {zone_3['ai_advice']}")

        for crop in zone_3.get("crops", []):
            st.markdown(f"""
                <div class="crop-card">
                    <div class="crop-header">
                        <div class="crop-icon">{crop['icon']}</div>
                        <div>
                            <div class="crop-title">{crop['name']}</div>
                            <div class="crop-scientific">{crop['scientific_name']}</div>
                        </div>
                    </div>
                    <div>
                        <span class="tag-pill tag-sun">☀️ {crop['sun_requirement']}</span>
                        <span class="tag-pill tag-root">🪴 {crop['container_depth_inches']}" Depth</span>
                        <span class="tag-pill tag-water">💧 {crop['water_frequency']}</span>
                        <span class="tag-pill tag-harvest">⏱️ {crop['harvest_weeks']}</span>
                        <span class="tag-pill tag-season">🗓️ {season_name}</span>
                        <span class="tag-pill tag-difficulty">🟢 {crop['difficulty']}</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #334155; margin-top: 0.6rem;">
                        <strong>Pairing:</strong> {crop['companion_notes']}
                    </div>
                    <div class="crop-touch-grass-box">
                        <strong>🌿 Touch Grass Action:</strong> {crop['touch_grass_action']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

with tab_schematic:
    st.markdown("#### 📐 Elevation Architectural Schematic")
    st.markdown(f"""
        <div class="schematic-box">
<pre style="color: #A7F3D0; font-family: 'Consolas', 'Fira Code', monospace; line-height: 1.38; margin: 0;">
☀️ DIRECT SOLAR ANGLE VECTOR  ===> [Facing: {balcony_facing.upper()} | Sun: {blueprint.get('effective_sunlight_hours')}h | Season: {season_name}]
─────────────────────────────────────────────────────────────────────────────
▲ OPEN SKYLINE HORIZON (UNOBSTRUCTED)
│
│   [ ZONE 1: FRONT RAILING / HANGING BASKETS ] ────────── (Elevation: +3.5 ft to +6.5 ft)
│   • Plant Blueprint: {', '.join([c['name'] for c in zone_1.get('crops', [])])}
│   • Containers: Railing Saddles, 6-8" Coco-Coir Baskets
│   • Physics: Horizon light capture; trailing canopy; high wind exposure tolerance.
│
│       │
│       ▼ (Filtered / Ambient Light Gradient)
│
│   [ ZONE 2: MID-TIER WALL TRELLIS & RAIL GRID ] ─────── (Elevation: +1.5 ft to +3.5 ft)
│   • Plant Blueprint: {', '.join([c['name'] for c in zone_2.get('crops', [])])}
│   • Containers: Tiered Planter Boxes, Felt Vertical Wall Pockets
│   • Physics: Wind-sheltered; optimal for daily cut-and-come-again harvest.
│
│       │
│       ▼ (Thermal Masonry Absorption & Ground Center of Gravity)
│
│   [ ZONE 3: FLOOR & DEEP CORNER POTS ] ──────────────── (Elevation: 0.0 ft Deck Floor)
│   • Plant Blueprint: {', '.join([c['name'] for c in zone_3.get('crops', [])])}
│   • Containers: Heavy 12-14" Pots / 7-Gallon Fabric Grow Bags
│   • Physics: Low center of gravity; deep root anchorage; high thermal mass storage.
─────────────────────────────────────────────────────────────────────────────
🚪 INTERIOR APARTMENT DOOR  (Close Laptop • Step Outside • Breathe Fresh Air)
</pre>
        </div>
    """, unsafe_allow_html=True)

with tab_synergy:
    st.markdown("#### 🤝 Companion Guilds & Spatial Separation Matrix")
    synergies = blueprint.get("companion_synergies", [])
    if synergies:
        for s in synergies:
            st.markdown(f"""
                <div class="synergy-card">
                    <div class="synergy-icon-wrap">🌿</div>
                    <div>
                        <div style="font-weight: 800; color: #0F2317; font-size: 1.05rem;">{s.get('pair')}</div>
                        <span class="tag-pill" style="background: #DCFCE7; color: #166534; font-weight: 800; margin: 4px 0;">{s.get('type')}</span>
                        <div style="font-size: 0.86rem; color: #475569; margin-top: 4px; line-height: 1.45;">{s.get('description')}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No companion conflicts detected. All selected crops share positive spatial resonance!")

with tab_challenge:
    st.markdown("#### 🧤 The Weekly 'Touch Grass' Sensory Challenge")
    st.markdown("""
        The entire philosophy of **Balconize** is to make screen time minimal and physical outdoor time maximal. 
        Complete these 4 physical tasks this week:
    """)
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.checkbox("🖐️ **Soil Moisture Finger Probe:** Push your index finger 1 inch into the soil of Zone 3 before watering.", value=False)
        st.checkbox("👃 **Aromatic Terpene Sniff:** Gently brush foliage of Zone 1 herbs and inhale the invigorating natural oils.", value=False)
    with col_c2:
        st.checkbox("✂️ **Lateral Pinching:** Snip terminal flower buds or harvest outer leaves using the cut-and-come-again method.", value=False)
        st.checkbox("☀️ **Solar Vector Observation:** Step onto the balcony at 2:00 PM and physically observe where the sunlight hits your deck.", value=False)

# ==============================================================================
# 9. "TOUCH GRASS" EXPORT MODE & OUTDOOR ACTION PLAN
# ==============================================================================
action_plan_text = blueprint.get("touch_grass_action_plan", "No action plan generated.")

st.markdown("""
    <div class="touch-grass-export-box">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <span class="hero-tag" style="background: rgba(46,204,113,0.22); border-color: #34D399;">OUTDOOR MISSION</span>
                <h2 style="margin: 0.3rem 0; color: #FFFFFF; font-size: 1.85rem;">🌿 Print / Copy Outdoor Action Plan</h2>
                <div style="font-size: 0.95rem; color: #A7F3D0; max-width: 720px; line-height: 1.5;">
                    The screen is the shortest part of your day. Shut your laptop, grab your gardening trowel, 
                    and take this clean text blueprint outside into the fresh air.
                </div>
            </div>
            <div style="font-size: 3.8rem;">🧤</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.expander("📋 View & Export Printable Outdoor Action Checklist", expanded=True):
    col_dl1, col_dl2 = st.columns([1, 1])
    with col_dl1:
        st.download_button(
            label="📥 Download Outdoor Plan (.txt)",
            data=action_plan_text,
            file_name=f"Balconize_OutdoorPlan_{balcony_facing}_{current_season}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col_dl2:
        st.download_button(
            label="📥 Download Markdown Blueprint (.md)",
            data=action_plan_text,
            file_name=f"Balconize_OutdoorPlan_{balcony_facing}_{current_season}.md",
            mime="text/markdown",
            use_container_width=True
        )

    st.code(action_plan_text, language="markdown")

    st.markdown("""
        <div style="background: #F0FDF4; border: 1px dashed #2ECC71; border-radius: 12px; padding: 14px; margin-top: 10px; text-align: center; color: #166534; font-weight: 700;">
            ✅ Touch Grass Tip: Take a screenshot or tap download, close your laptop, and spend 15 uninterrupted minutes setting up your containers outdoors!
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 10. OPEN-SOURCE PRIVACY CALLOUT FOOTER
# ==============================================================================
st.markdown("""
    <div class="footer-badge-box">
        <div style="font-size: 0.88rem; font-weight: 800; color: #0F2317; margin-bottom: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em;">
            Balconize — Open-Source Privacy Architecture & Hackathon Guarantee
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center;">
            <span class="footer-pill">🔒 100% Local Inference</span>
            <span class="footer-pill">☁️ Zero Cloud Data Sent</span>
            <span class="footer-pill">💰 $0.00 Running Cost</span>
            <span class="footer-pill">🦙 Ollama & Open Weights</span>
            <span class="footer-pill">⚡ Zero-Failure Agro-Engine</span>
            <span class="footer-pill">🌱 Touch Grass Pro Edition</span>
        </div>
        <div style="font-size: 0.76rem; color: #94A3B8; margin-top: 0.9rem;">
            Balconize is 100% Free and Open Source. Crafted with Python, Streamlit, and Open Weights.
        </div>
    </div>
""", unsafe_allow_html=True)
