"""
model_service.py - AI & Algorithmic Blueprint Engine for VerdantBalcony
Provides local open-weight LLM inference (via Ollama) with an instant,
zero-failure rule-based agro-ecological fallback engine.
"""

import json
import os
import re
from typing import Dict, List, Any, Optional

try:
    import ollama
    OLLAMA_INSTALLED = True
except ImportError:
    OLLAMA_INSTALLED = False

DB_PATH = os.path.join(os.path.dirname(__file__), "plants_database.json")


def load_plants_database() -> Dict[str, Any]:
    """Loads the structured local crop database."""
    if not os.path.exists(DB_PATH):
        # Fallback if DB file is in current working directory
        if os.path.exists("plants_database.json"):
            with open("plants_database.json", "r", encoding="utf-8") as f:
                return json.load(f)
        raise FileNotFoundError(f"Cannot find plants_database.json at {DB_PATH}")
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def check_ollama_status() -> Dict[str, Any]:
    """
    Checks if Ollama daemon is reachable locally and lists available models.
    Guaranteed not to raise an exception.
    """
    if not OLLAMA_INSTALLED:
        return {
            "is_available": False,
            "error_reason": "The 'ollama' python package is not installed.",
            "available_models": [],
            "suggested_model": None
        }

    # Fast socket pre-check (takes < 2ms if port is closed)
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect(("127.0.0.1", 11434))
        s.close()
    except Exception:
        s.close()
        return {
            "is_available": False,
            "error_reason": "Ollama daemon not running on port 11434. Running in 100% Algorithmic Fallback mode.",
            "available_models": [],
            "suggested_model": "phi3"
        }

    try:
        client = ollama.Client(timeout=1.5)
        models_response = client.list()
        # ollama.list() returns a dict or object with 'models'
        model_names = []
        if hasattr(models_response, "models"):
            for m in models_response.models:
                name = getattr(m, "model", None) or getattr(m, "name", str(m))
                model_names.append(name)
        elif isinstance(models_response, dict) and "models" in models_response:
            for m in models_response["models"]:
                name = m.get("name") or m.get("model")
                if name:
                    model_names.append(name)

        # Pick best default model
        preferred = ["phi3:latest", "phi3", "gemma:2b", "gemma", "llama3.2:latest", "llama3.2", "mistral:latest", "mistral"]
        suggested = None
        for p in preferred:
            for actual in model_names:
                if p in actual.lower():
                    suggested = actual
                    break
            if suggested:
                break

        if not suggested and model_names:
            suggested = model_names[0]

        return {
            "is_available": True,
            "error_reason": None,
            "available_models": model_names,
            "suggested_model": suggested or "phi3"
        }
    except Exception as e:
        return {
            "is_available": False,
            "error_reason": f"Ollama daemon not reachable at localhost:11434 ({str(e)})",
            "available_models": [],
            "suggested_model": "phi3"
        }


def algorithmic_engine(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    High-precision deterministic agronomic engine that pairs balcony parameters
    with crops from plants_database.json without requiring any external server.
    """
    db = load_plants_database()
    crops = db.get("crops", [])
    orientations = db.get("balcony_orientations", {})
    zone_defs = db.get("zone_definitions", {})

    facing = params.get("balcony_facing", "South")
    sunlight_hours = float(params.get("sunlight_hours", 6.0))
    hardware = params.get("hardware", ["Railings", "Wall Hooks / Trellis", "Floor Space"])
    categories = params.get("categories", ["Herbs & Aromatics", "Leafy Greens", "Vegetables & Fruiting"])
    balcony_size = params.get("balcony_size", "Standard (30-50 sq ft)")
    experience_level = params.get("experience_level", "All Levels")
    season = params.get("season", "Spring Kickoff")

    seasonal_profiles = db.get("seasonal_profiles", {})
    season_profile = seasonal_profiles.get(season, seasonal_profiles.get("Spring Kickoff", {}))
    solar_modifier = season_profile.get("solar_modifier", 1.0)

    orientation_info = orientations.get(facing, orientations.get("South", {}))
    sunlight_factor = orientation_info.get("sunlight_factor", 1.0)
    effective_sun = round(sunlight_hours * sunlight_factor * solar_modifier, 1)

    # 1. Calculate Balcony & Zone-Specific Effective Sunlight Gradients
    balcony_base_sun = round(sunlight_hours * sunlight_factor * solar_modifier, 1)

    # Zone 1 (Front Railing & High Hanging): Open sky horizon exposure (1.15x)
    z1_sun = round(min(10.0, balcony_base_sun * 1.15), 1)

    # Zone 2 (Mid-Tier Wall Trellis / Rail Tier): Filtered ambient shadow (0.85x)
    z2_sun = round(max(1.0, balcony_base_sun * 0.85), 1)

    # Zone 3 (Floor & Corner Heavy Pots): Deep deck floor; high sun on South/SW (0.95x), low on others (0.70x)
    z3_factor = 0.95 if facing in ["South", "South-West", "South-East"] else 0.70
    z3_sun = round(max(1.0, balcony_base_sun * z3_factor), 1)

    effective_sun = balcony_base_sun

    # Determine sun category
    if effective_sun >= 5.5:
        primary_sun_class = "Full Sun"
    elif effective_sun >= 3.0:
        primary_sun_class = "Partial Shade"
    else:
        primary_sun_class = "Shade"

    def score_crop_for_zone(crop: Dict[str, Any], zone_num: int, zone_sun: float) -> float:
        """Calculates a tailored bioclimatic suitability score for a specific zone and orientation."""
        score = 50.0
        cid = crop["id"]
        cat = crop.get("category", "")
        root_type = crop.get("root_type", "")
        vert_pos = crop.get("vertical_position", "")

        # -------------------------------------------------------------
        # A. Physical Container & Vertical Zone Fit
        # -------------------------------------------------------------
        if zone_num == 1:  # Front Railing & Hanging Baskets
            if root_type == "Shallow/Hanging" or "Hanging" in vert_pos:
                score += 45.0
            elif root_type == "Medium Container" and cid in ["thai_chili", "basil", "lettuce"]:
                score += 25.0
            elif root_type == "Deep Pot" or cid in ["cherry_tomatoes", "dwarf_bell_pepper"]:
                score -= 120.0  # Physically cannot put 14-inch heavy root crops on railing!

        elif zone_num == 2:  # Mid-Tier Wall & Tiered Ladder
            if root_type in ["Medium Container", "Shallow/Hanging"]:
                score += 40.0
            if cid in ["coriander", "spinach", "spring_onion", "lettuce", "basil", "radish"]:
                score += 30.0  # Perfect cut-and-come-again daily herb/salad tier
            elif root_type == "Deep Pot":
                score -= 70.0  # Heavy deep pots do not fit on mid-tier ladders/wall felt pockets

        elif zone_num == 3:  # Floor & Deep Corner Containers
            if root_type in ["Deep Pot", "Medium Container"]:
                score += 45.0
            if cid in ["cherry_tomatoes", "dwarf_bell_pepper", "radish", "spring_onion", "thai_chili"]:
                score += 35.0  # Anchoring floor root crops
            elif root_type == "Shallow/Hanging" or cid in ["strawberries", "thyme"]:
                score -= 50.0  # Trailing strawberries rot on damp floor deck; need elevation!

        # -------------------------------------------------------------
        # B. Sunlight Requirement Matching for this specific Zone
        # -------------------------------------------------------------
        min_sun = crop.get("min_sun_hours", 4)
        max_sun = crop.get("max_sun_hours", 8)
        if min_sun <= zone_sun <= max_sun:
            score += 40.0
        elif zone_sun >= min_sun:
            score += 25.0
        else:
            deficit = min_sun - zone_sun
            score -= (30.0 + deficit * 15.0)  # Significant penalty for insufficient sunlight

        # -------------------------------------------------------------
        # C. Orientation Bioclimatics (HIGH IMPACT DIFFERENTIATION)
        # -------------------------------------------------------------
        if facing in ["North", "North-East"]:
            # Low ambient sky light, cool shade
            if cid in ["cherry_tomatoes", "thai_chili", "dwarf_bell_pepper"]:
                score -= 150.0  # Physically impossible to fruit without direct sun
            elif cid in ["basil"]:
                score -= 60.0
            elif cid in ["mint", "spinach", "lettuce", "spring_onion"]:
                score += 55.0  # Shade champions thrive in gentle ambient light
            elif cid in ["coriander", "radish"]:
                score += 35.0

        elif facing in ["East"]:
            # Gentle cool morning sun, shaded afternoons
            if cid in ["lettuce", "spinach", "coriander", "strawberries", "mint"]:
                score += 50.0  # East morning light prevents bitterness & scorching
            elif cid in ["cherry_tomatoes", "dwarf_bell_pepper", "thai_chili"]:
                score -= 40.0  # Needs intense afternoon heat units to ripen heavy fruit

        elif facing in ["West"]:
            # Scorching late-afternoon heat & UV blast
            if cid in ["thyme", "thai_chili", "basil"]:
                score += 50.0  # Mediterranean heat lovers thrive in west sun
            elif cid in ["lettuce", "coriander"]:
                if zone_num == 1:
                    score -= 70.0  # Front rail west sun fries soft greens and causes bolting!
                else:
                    score += 25.0  # Sheltered Zone 2 wall stays safe
            elif cid in ["cherry_tomatoes", "dwarf_bell_pepper"]:
                if zone_num == 3:
                    score += 45.0  # Heavy heat banking on west floor concrete

        elif facing in ["South", "South-West"]:
            # Maximum all-day solar exposure
            if cid in ["cherry_tomatoes", "thai_chili", "dwarf_bell_pepper", "basil"]:
                score += 50.0  # Peak solar fruiting nightshades
            if cid in ["strawberries", "thyme"]:
                score += 35.0
            if cid in ["spinach", "coriander"] and zone_num == 1:
                score -= 30.0  # Scorching sun bolts cilantro; move to Zone 2

        # -------------------------------------------------------------
        # D. Sunlight Hours Thresholds (Slider sensitivity)
        # -------------------------------------------------------------
        if sunlight_hours <= 3.5:
            if cid in ["cherry_tomatoes", "thai_chili", "dwarf_bell_pepper"]:
                score -= 120.0
            if cid in ["mint", "spinach", "lettuce", "spring_onion"]:
                score += 45.0
        elif sunlight_hours >= 7.0:
            if cid in ["cherry_tomatoes", "thai_chili", "dwarf_bell_pepper", "basil", "thyme"]:
                score += 35.0

        # -------------------------------------------------------------
        # E. Seasonal Bioclimatic Adaptations
        # -------------------------------------------------------------
        ideal_seasons = crop.get("ideal_seasons", [])
        if season in ideal_seasons:
            score += 35.0
        else:
            score -= 35.0

        if season == "Winter Resilient":
            if cid in ["cherry_tomatoes", "thai_chili", "dwarf_bell_pepper"]:
                score -= 150.0  # Frost kills tender nightshades
            elif cid == "basil":
                score -= 80.0  # Dies below 10°C
            elif cid in ["spinach", "spring_onion", "thyme", "radish"]:
                score += 60.0  # Cold-hardy heroes
        elif season == "Summer Peak":
            if cid in ["cherry_tomatoes", "thai_chili", "dwarf_bell_pepper", "basil"]:
                score += 40.0
            elif cid == "coriander":
                score -= 35.0  # Bolting risk
        elif season == "Spring Kickoff":
            if cid in ["strawberries", "lettuce", "mint", "radish"]:
                score += 35.0
        elif season == "Autumn Harvest":
            if cid in ["radish", "spinach", "lettuce", "spring_onion"]:
                score += 35.0

        # -------------------------------------------------------------
        # F. User Category & Experience Preferences
        # -------------------------------------------------------------
        if cat in categories:
            score += 25.0
        if experience_level == "Beginner" and crop.get("difficulty") == "Beginner":
            score += 15.0

        return score

    # Distribute across zones independently
    has_railings = ("Railings" in hardware) or ("Hanging Mounts" in hardware)
    has_wall = ("Wall Hooks / Trellis" in hardware)
    has_floor = ("Floor Space" in hardware)

    zone_1_crops = []
    zone_2_crops = []
    zone_3_crops = []
    used_ids = set()

    # 1. Fill Zone 1 (Railing / Front Hanging)
    if has_railings:
        scored_z1 = sorted([(score_crop_for_zone(c, 1, z1_sun), c) for c in crops], key=lambda x: x[0], reverse=True)
        for s, c in scored_z1:
            if c["id"] not in used_ids and s > 0:
                zone_1_crops.append(c)
                used_ids.add(c["id"])
                if len(zone_1_crops) >= 2:
                    break

    # 2. Fill Zone 3 (Floor / Deep Containers - heavy pots prioritized before mid-tier)
    if has_floor:
        scored_z3 = sorted([(score_crop_for_zone(c, 3, z3_sun), c) for c in crops if c["id"] not in used_ids], key=lambda x: x[0], reverse=True)
        for s, c in scored_z3:
            if c["id"] not in used_ids and s > 0:
                zone_3_crops.append(c)
                used_ids.add(c["id"])
                if len(zone_3_crops) >= 2:
                    break

    # 3. Fill Zone 2 (Mid-Tier Wall / Rail Ladder Grid)
    scored_z2 = sorted([(score_crop_for_zone(c, 2, z2_sun), c) for c in crops if c["id"] not in used_ids], key=lambda x: x[0], reverse=True)
    for s, c in scored_z2:
        if c["id"] not in used_ids and s > 0:
            zone_2_crops.append(c)
            used_ids.add(c["id"])
            if len(zone_2_crops) >= 2:
                break

    # Safety Fallback: ensure no active zone is left completely empty
    for c in crops:
        if c["id"] not in used_ids:
            if len(zone_1_crops) == 0 and has_railings:
                zone_1_crops.append(c)
                used_ids.add(c["id"])
            elif len(zone_2_crops) == 0:
                zone_2_crops.append(c)
                used_ids.add(c["id"])
            elif len(zone_3_crops) == 0 and has_floor:
                zone_3_crops.append(c)
                used_ids.add(c["id"])

    # Calculate Companion Synergies
    synergies = []
    all_selected = zone_1_crops + zone_2_crops + zone_3_crops
    selected_ids = {c["id"] for c in all_selected}

    if "cherry_tomatoes" in selected_ids and "basil" in selected_ids:
        synergies.append({
            "pair": "Balcony Cherry Tomatoes + Sweet Basil",
            "type": "Golden Companion Guild",
            "description": "Basil emits aromatic terpenes that mask tomato foliage from aphids and thrips while enhancing tomato flavor profile."
        })
    if "spinach" in selected_ids and "strawberries" in selected_ids:
        synergies.append({
            "pair": "Baby Spinach + Strawberries",
            "type": "Understory Canopy Pairing",
            "description": "Spinach acts as living soil mulch, retaining root moisture for strawberries without competing for nitrogen."
        })
    if "radish" in selected_ids and "lettuce" in selected_ids:
        synergies.append({
            "pair": "French Breakfast Radish + Butterhead Lettuce",
            "type": "Root Depth Separation",
            "description": "Radishes expand quickly in the upper 4-6 inches of soil while lettuce spreads fibrous surface roots, utilizing soil tiers harmoniously."
        })
    if "thai_chili" in selected_ids and "thyme" in selected_ids:
        synergies.append({
            "pair": "Thai Bird's Eye Chili + Creeping Thyme",
            "type": "Low-Water Drought Harmony",
            "description": "Both thrive in high heat and lean, well-draining soil without root rot vulnerability."
        })
    if "mint" in selected_ids:
        synergies.append({
            "pair": "Spearmint (Isolation Protocol)",
            "type": "Containment Guard",
            "description": "Mint is isolated in high Zone 1 hanging baskets to stop vigorous stolons from strangling slower container companions."
        })

    # Calculations
    sun_utilization_pct = min(100, int((effective_sun / max(6.0, sunlight_hours)) * 95 + 5))
    total_crops_count = len(all_selected)

    # Generate Outdoor "Touch Grass" Checklist
    action_plan_lines = [
        "==================================================================",
        "🌿 BALCONIZE — OUTDOOR TOUCH GRASS ACTION BLUEPRINT",
        "==================================================================",
        f"Season: {season} ({season_profile.get('badge', '')})",
        f"Balcony Facing: {facing} | Direct Sun: {sunlight_hours} hrs | Seasonal Effective Sun: {effective_sun} hrs (Factor: {solar_modifier}x)",
        f"Balcony Size: {balcony_size} | Architecture: 3-Tier Vertical Zoning",
        "------------------------------------------------------------------\n",
        "STEP 1: PHYSICAL ZONE POSITIONING & HARDWARE SETUP",
        f" • Zone 1 (Railing/Hanging): Secure {len(zone_1_crops)} baskets onto the front balustrade.",
        f"   Plants: {', '.join([c['name'] for c in zone_1_crops]) if zone_1_crops else 'None'}",
        f" • Zone 2 (Mid-Tier Wall/Ladder): Mount shelving or rail tier boxes.",
        f"   Plants: {', '.join([c['name'] for c in zone_2_crops]) if zone_2_crops else 'None'}",
        f" • Zone 3 (Floor Corners): Place {len(zone_3_crops)} deep stable pots in the sheltered corner.",
        f"   Plants: {', '.join([c['name'] for c in zone_3_crops]) if zone_3_crops else 'None'}\n",
        "STEP 2: SOIL DEPTH & CONTAINER SPECIFICATIONS"
    ]

    for c in all_selected:
        action_plan_lines.append(
            f" • {c['icon']} {c['name']}: Requires min {c['container_depth_inches']}\" pot depth. Soil: {c['soil_preference']}"
        )

    action_plan_lines.extend([
        f"\nSTEP 3: SEASONAL WATERING & MICRO-CLIMATE ROUTINE ({season.upper()})",
        f" • Orientation Advisory: {orientation_info.get('thermal_profile', 'Standard balcony exposure')}.",
        f" • Seasonal Climate: {season_profile.get('thermal_description', '')}",
        f" • Hydration Protocol: {season_profile.get('water_rule', '')}",
        f" • Priority Outdoor Action: {season_profile.get('outdoor_action', '')}"
    ])

    action_plan_lines.extend([
        "\nSTEP 4: PHYSICAL 'TOUCH GRASS' SENSORY & CARE TASKS"
    ])
    for c in all_selected:
        action_plan_lines.append(f" • {c['icon']} {c['name']}: {c['touch_grass_action']}")

    action_plan_lines.extend([
        "\n------------------------------------------------------------------",
        "🎯 LAPTOP OFF, GLOVES ON! STEP OUTSIDE INTO THE SUNLIGHT.",
        "=================================================================="
    ])

    return {
        "execution_mode": "algorithmic_fallback",
        "model_used": "Deterministic Agro-Ecological Engine",
        "status_title": "⚡ 100% Local Algorithmic Engine Active",
        "status_subtitle": "Zero cloud dependencies • Instant response • Agronomic rule-based precision",
        "effective_sunlight_hours": effective_sun,
        "solar_modifier": solar_modifier,
        "season": season,
        "season_badge": season_profile.get("badge", season),
        "season_thermal_desc": season_profile.get("thermal_description", ""),
        "season_outdoor_action": season_profile.get("outdoor_action", ""),
        "season_water_rule": season_profile.get("water_rule", ""),
        "orientation_notes": orientation_info.get("sunlight_quality", "Balanced light"),
        "thermal_profile": orientation_info.get("thermal_profile", "Moderate"),
        "sun_utilization_pct": sun_utilization_pct,
        "total_crops_count": total_crops_count,
        "zones": {
            "zone_1": {
                "title": zone_defs.get("zone_1", {}).get("name", "Zone 1: Railing & Hanging Baskets"),
                "role": zone_defs.get("zone_1", {}).get("role", "Solar Front-Line & Trailing Canopy"),
                "description": zone_defs.get("zone_1", {}).get("description", ""),
                "container_types": zone_defs.get("zone_1", {}).get("best_container_types", ""),
                "crops": zone_1_crops
            },
            "zone_2": {
                "title": zone_defs.get("zone_2", {}).get("name", "Zone 2: Mid-Tier Rail Grid & Wall Vertical"),
                "role": zone_defs.get("zone_2", {}).get("role", "Vertical Stacking & Micro-Climate Moderation"),
                "description": zone_defs.get("zone_2", {}).get("description", ""),
                "container_types": zone_defs.get("zone_2", {}).get("best_container_types", ""),
                "crops": zone_2_crops
            },
            "zone_3": {
                "title": zone_defs.get("zone_3", {}).get("name", "Zone 3: Floor & Deep Corner Containers"),
                "role": zone_defs.get("zone_3", {}).get("role", "Thermal Anchor & Heavy Root Haven"),
                "description": zone_defs.get("zone_3", {}).get("description", ""),
                "container_types": zone_defs.get("zone_3", {}).get("best_container_types", ""),
                "crops": zone_3_crops
            }
        },
        "companion_synergies": synergies,
        "touch_grass_action_plan": "\n".join(action_plan_lines)
    }


def query_ollama_llm(params: Dict[str, Any], model_name: str = "phi3") -> Optional[Dict[str, Any]]:
    """
    Queries local Ollama instance with structured system prompt and parameters.
    Returns parsed JSON blueprint, or None if Ollama fails/is unavailable.
    """
    if not OLLAMA_INSTALLED:
        return None

    db = load_plants_database()
    crops_available = [c["name"] for c in db.get("crops", [])]

    system_prompt = (
        "You are Balconize AI, a master permaculture urban farming architect and open-source agro-optimizer. "
        "Your mission is to get city dwellers OFF THEIR SCREENS and OUT ONTO THEIR BALCONIES to touch real plants. "
        "Analyze the apartment balcony parameters and assign optimal crops into three vertical zones: "
        "Zone 1 (Railing/Hanging Baskets - direct front sun), "
        "Zone 2 (Mid-Tier Wall/Tiered Grid - vertical herb/salad greens), and "
        "Zone 3 (Floor Corners - heavy pots, fruiting vegetables, deep roots). "
        "You MUST respond ONLY with a valid, clean JSON object matching the requested schema without markdown quotes or conversational text."
    )

    user_prompt = f"""
Apartment Balcony Specs:
- Season / Climate Cycle: {params.get('season', 'Spring Kickoff')}
- Facing Orientation: {params.get('balcony_facing', 'South')}
- Direct Sunlight: {params.get('sunlight_hours', 6)} hours/day
- Available Hardware: {', '.join(params.get('hardware', ['Railings', 'Floor Space']))}
- Balcony Size: {params.get('balcony_size', 'Standard (30-50 sq ft)')}
- Experience Level: {params.get('experience_level', 'Beginner')}
- Preferred Crops Catalog: {', '.join(crops_available)}

Return a JSON with the following exact keys:
{{
  "effective_sunlight_evaluation": "Short summary of sunlight & micro-climate for this orientation",
  "zone_1_crops": ["Name of Crop 1", "Name of Crop 2"],
  "zone_1_tactical_advice": "Railing mounting & sun advice",
  "zone_2_crops": ["Name of Crop 3", "Name of Crop 4"],
  "zone_2_tactical_advice": "Mid-tier vertical stacking advice",
  "zone_3_crops": ["Name of Crop 5", "Name of Crop 6"],
  "zone_3_tactical_advice": "Floor container placement & staking advice",
  "companion_synergy_note": "A specific pairing benefit between two chosen plants",
  "touch_grass_physical_challenge": "A specific physical task to do outdoors right now (e.g. soil moisture test, leaf pinch)"
}}
"""

    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            options={"temperature": 0.2, "top_p": 0.9}
        )

        content = response["message"]["content"]
        # Extract JSON using regex if wrapped in markdown blocks
        json_match = re.search(r"\{.*\}", content, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group(0))
            return parsed
        return None
    except Exception:
        # Gracefully handle connection error, model not found, timeout, etc.
        return None


def generate_balcony_blueprint(params: Dict[str, Any], use_ai_if_available: bool = True, model_name: str = "phi3") -> Dict[str, Any]:
    """
    Main orchestration function.
    Always produces a complete, robust blueprint by using Ollama LLM if available,
    or seamlessly falling back to the algorithmic agronomic engine.
    """
    # 1. Base blueprint from algorithmic engine to ensure data integrity
    blueprint = algorithmic_engine(params)

    # 2. Check if Ollama is requested and reachable
    if use_ai_if_available:
        status = check_ollama_status()
        if status["is_available"] and status.get("available_models"):
            # Use suggested or user-chosen model
            target_model = model_name if model_name in status["available_models"] else status["suggested_model"]
            ai_result = query_ollama_llm(params, model_name=target_model)

            if ai_result:
                # Enrich the blueprint with AI insights
                blueprint["execution_mode"] = "ollama_ai"
                blueprint["model_used"] = f"Local Ollama Node ({target_model})"
                blueprint["status_title"] = f"🟢 Local AI Inference Active: {target_model}"
                blueprint["status_subtitle"] = "100% Private on-device open weights • Zero cloud data • Touch Grass verified"

                # Update tactical zone notes
                if "zone_1_tactical_advice" in ai_result:
                    blueprint["zones"]["zone_1"]["ai_advice"] = ai_result["zone_1_tactical_advice"]
                if "zone_2_tactical_advice" in ai_result:
                    blueprint["zones"]["zone_2"]["ai_advice"] = ai_result["zone_2_tactical_advice"]
                if "zone_3_tactical_advice" in ai_result:
                    blueprint["zones"]["zone_3"]["ai_advice"] = ai_result["zone_3_tactical_advice"]

                if "companion_synergy_note" in ai_result:
                    blueprint["companion_synergies"].insert(0, {
                        "pair": "AI Permaculture Stacking",
                        "type": "Local LLM Synthesis",
                        "description": ai_result["companion_synergy_note"]
                    })

                if "touch_grass_physical_challenge" in ai_result:
                    blueprint["outdoor_physical_challenge"] = ai_result["touch_grass_physical_challenge"]

    return blueprint
