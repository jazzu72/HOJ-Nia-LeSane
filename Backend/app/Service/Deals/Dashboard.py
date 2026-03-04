from datetime import datetime
from typing import List, Dict, Any
from statistics import mean
from app.services.deals.deal_scoring import score_deals
from app.services.deals.daily_summary import daily_summary

def generate_alerts(ranked_deals: List[Dict[str, Any]]) -> List[str]:
    alerts = []
    if not ranked_deals:
        return alerts

    top = ranked_deals[0]
    roi = top["raw"]["roi_percent"]
    risk = top["raw"]["risk_score"]
    time_cap = top["raw"]["time_to_capital"]

    if roi >= 25:
        alerts.append(f"High ROI opportunity detected: {roi}%")
    if risk <= 20:
        alerts.append("Low-risk opportunity available")
    if time_cap <= 30:
        alerts.append("Fast time-to-capital opportunity detected")

    return alerts

def build_dashboard(deals: List[Dict[str, Any]]) -> Dict[str, Any]:
    ranked = score_deals(deals)
    summary = daily_summary(ranked)
    alerts = generate_alerts(ranked)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "ranked_deals": ranked,
        "summary": summary,
        "alerts": alerts
    }
