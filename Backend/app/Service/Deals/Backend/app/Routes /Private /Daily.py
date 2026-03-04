from fastapi import APIRouter, Depends
from app.auth.guards import founder_required
from app.services.deals.deal_scoring import score_deals
from app.services.deals.daily_summary import daily_summary

router = APIRouter()

@router.post("/summary")
async def generate_daily_summary(payload: dict, user = Depends(founder_required)):
    """
    Payload example:
    {
        "deals": [
            {"category": "flip", "roi_percent": 32, "risk_score": 40, "time_to_capital": 120},
            {"category": "tax_lien", "roi_percent": 18, "risk_score": 20, "time_to_capital": 365},
            {"category": "mining", "roi_percent": 12, "risk_score": 10, "time_to_capital": 1}
        ]
    }
    """
    deals = payload.get("deals", [])
    ranked = score_deals(deals)
    summary = daily_summary(ranked)
    return summary
