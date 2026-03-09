from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DealInput(BaseModel):
    address: str
    arv: float
    asking: float
    repairs: float

@app.post("/")
def score_deal(data: DealInput):
    spread = data.arv - data.asking - data.repairs
    ratio = spread / data.arv if data.arv > 0 else 0
    score = round(ratio * 100)

    recommended_offer = data.arv * 0.70 - data.repairs

    text_block = f"""
Lead Package — House of Jazzu / Nia Executive Engine

Address: {data.address}
ARV: ${data.arv:,.0f}
Asking: ${data.asking:,.0f}
Repairs: ${data.repairs:,.0f}
Net Spread: ${spread:,.0f}
Score: {score}/100

Summary:
This property presents a value-add opportunity with a solid spread and manageable repairs.
Recommended offer range: ${recommended_offer:,.0f} depending on investor strategy.

Prepared by: Nia LeSane, Executive Intelligence Engine
"""

    return {
        "address": data.address,
        "arv": data.arv,
        "asking": data.asking,
        "repairs": data.repairs,
        "spread": spread,
        "score": score,
        "recommendedOffer": recommended_offer,
        "summary": "Lead package generated successfully.",
        "textBlock": text_block.strip()
    }
