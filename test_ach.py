"""
ach-return-codes / test_ach.py
Author:  Raghav Anand
Created: 2026-11-06

Tests for ach.py. Run with:
  python3 -m pytest -v
"""

from ach import format_card, lookup, normalize
from codes import CODES


def test_normalize_handles_messy_input():
    assert normalize(" r1 ") == "R01"
    assert normalize("R01") == "R01"
    assert normalize("r29") == "R29"


def test_lookup_known_code():
    assert lookup("R01")["title"] == "Insufficient Funds"


def test_unknown_code_is_friendly():
    assert "Unknown code" in format_card("R99")


def test_only_funds_codes_allow_automatic_retry():
    # Per NACHA rules, only R01 and R09 can be re-presented without new authorization.
    auto_retry = {code for code, info in CODES.items() if info["retry"].startswith("Yes: up to 2")}
    assert auto_retry == {"R01", "R09"}


def test_every_code_has_all_fields():
    fields = {"title", "meaning", "retry", "window", "customer_message"}
    for code, info in CODES.items():
        assert set(info) == fields, code