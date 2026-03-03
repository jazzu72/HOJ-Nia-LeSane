from fastapi import APIRouter

router = APIRouter()

@router.get("/roi-demo")
async def roi_demo(amount: float = 1000, rate: float = 10.0, months: int = 12):
    interest = amount * (rate / 100) * (months / 12)
    return {
        "amount": amount,
        "rate": rate,
        "months": months,
        "interest": round(interest, 2),
    }
