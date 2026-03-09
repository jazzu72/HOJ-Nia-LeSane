STATE_TAX_RULES = {
    "FL": {"interest_rate": 18.0, "redemption_years": 2, "bid_type": "premium"},
    "TX": {"interest_rate": 25.0, "redemption_years": 2, "bid_type": "premium"},
    "IL": {"interest_rate": 36.0, "redemption_years": 2.5, "bid_type": "penalty"},
    # ... more states
}

def get_state_rate(state: str):
    return STATE_TAX_RULES.get(state.upper(), {"interest_rate": 0, "redemption_years": 0})
