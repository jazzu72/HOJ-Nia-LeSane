def calculate_lien_roi(lien_amount: float, state: str, hold_months: int = 12) -> dict:
    rules = get_state_rate(state)
    if not rules["interest_rate"]:
        return {"error": "State not supported"}
    
    annual_rate = rules["interest_rate"] / 100
    interest = lien_amount * annual_rate * (hold_months / 12)
    roi = (interest / lien_amount) * 100
    
    return {
        "lien_amount": lien_amount,
        "state": state,
        "annual_rate": rules["interest_rate"],
        "expected_interest": round(interest, 2),
        "roi_percent": round(roi, 2)
    }
