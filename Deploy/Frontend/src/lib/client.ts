// frontend/src/lib/api/client.ts

export class NiaAPI {
  base = "/api"; // Vercel routes /api/* → backend/*

  async post(path: string, data: any) {
    try {
      const res = await fetch(`${this.base}${path}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`API Error: ${res.status} — ${text}`);
      }

      return await res.json();
    } catch (err) {
      console.error("NiaAPI POST Error:", err);
      throw err;
    }
  }

  async get(path: string) {
    try {
      const res = await fetch(`${this.base}${path}`);

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`API Error: ${res.status} — ${text}`);
      }

      return await res.json();
    } catch (err) {
      console.error("NiaAPI GET Error:", err);
      throw err;
    }
  }

  // Deal Scoring
  async scoreDeal(payload: {
    address: string;
    arv: number;
    asking: number;
    repairs: number;
  }) {
    return this.post("/score", payload);
  }

  // BirdDog Engine (future)
  async birddogSearch(payload: any) {
    return this.post("/birddog", payload);
  }

  // Tax Lien Engine (future)
  async taxLiens(payload: any) {
    return this.post("/taxliens", payload);
  }
}

// Export a single instance
export const nia = new NiaAPI();
