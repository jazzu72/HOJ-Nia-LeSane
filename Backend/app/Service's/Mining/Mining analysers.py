import math
from datetime import datetime

def mining_profitability(
    hash_rate_ths: float,
    power_watts: float,
    electricity_cost_kwh: float,
    btc_price: float,
    network_difficulty: float,
    block_reward: float = 3.125
):
    """
    Basic Bitcoin mining profitability model.
    All values are owner-only and never exposed to Nia.
    """

    # Convert TH/s to H/s
    hash_rate_hs = hash_rate_ths * 1e12

    # Bitcoin difficulty → expected BTC/day
    seconds_per_day = 86400
    expected_blocks_per_day = seconds_per_day / 600  # ~144 blocks/day

    # Probability of finding a block
    probability = hash_rate_hs / (network_difficulty * 2**32)

    btc_per_day = probability * expected_blocks_per_day * block_reward

    # Power cost
    kwh_per_day = (power_watts / 1000) * 24
    daily_power_cost = kwh_per_day * electricity_cost_kwh

    # Revenue
    daily_revenue = btc_per_day * btc_price
    daily_profit = daily_revenue - daily_power_cost

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "hash_rate_ths": hash_rate_ths,
        "power_watts": power_watts,
        "electricity_cost_kwh": electricity_cost_kwh,
        "btc_price": btc_price,
        "network_difficulty": network_difficulty,
        "btc_per_day": round(btc_per_day, 8),
        "daily_revenue_usd": round(daily_revenue, 2),
        "daily_power_cost_usd": round(daily_power_cost, 2),
        "daily_profit_usd": round(daily_profit, 2),
    }
