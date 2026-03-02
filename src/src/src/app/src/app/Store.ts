import { useState } from "react";

export function useAppStore() {
  const [user, setUser] = useState<string | null>(null);

  return {
    user,
    setUser,
  };
}
