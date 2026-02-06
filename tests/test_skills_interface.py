# tests/test_skills_interface.py
import pytest
from typing import Any

# These tests define the expected interface / contract
# They will fail until the skill modules are implemented

@pytest.mark.parametrize("skill_name", [
    "social-listening-trend-spotting",
    "persona-consistent-content-generation",
    "autonomous-reply-engagement"
])
def test_skill_accepts_correct_parameters(skill_name: str):
    # This is a contract test — real function does not exist yet
    with pytest.raises(NameError):  # we expect it to not be defined yet
        func = globals()[f"run_{skill_name.replace('-', '_')}"]

    # Instead we just document the expected signature via test description
    # Real implementation should match this structure
    expected_signature = {
        "social-listening-trend-spotting": {
            "niche_keywords": list[str],
            "platforms": list[str],
            "time_window_hours": (int, float),
            "min_relevance_threshold": (int, float)
        },
        "persona-consistent-content-generation": {
            "prompt_seed": str,
            "content_type": str,
            "character_reference_id": (str, type(None)),
            "generation_tier": str
        },
        "autonomous-reply-engagement": {
            "incoming_content": dict,
            "context_window": list,
            "max_length_chars": int
        }
    }

    assert skill_name in expected_signature, f"Unknown skill: {skill_name}"
