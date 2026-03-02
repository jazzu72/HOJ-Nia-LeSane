import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import NiaCoreScreen from "../rooms/NiaCore/NiaCoreScreen";
import MuseforgeScreen from "../rooms/Museforge/MuseforgeScreen";
import PolishScreen from "../rooms/Polish/PolishScreen";
import MoneyMunchkinsScreen from "../rooms/MoneyMunchkins/MoneyMunchkinsScreen";
import CounselScreen from "../rooms/Counsel/CounselScreen";
import RockyScreen from "../rooms/Rocky/RockyScreen";

const AppRoutes: React.FC = () => {
  return (
    <BrowserRouter>
      <nav style={{ display: "flex", gap: "1rem", padding: "0.5rem 1rem" }}>
        <Link to="/">Nia</Link>
        <Link to="/museforge">Museforge</Link>
        <Link to="/polish">Polish</Link>
        <Link to="/money">Money</Link>
        <Link to="/counsel">Counsel</Link>
        <Link to="/rocky">Rocky</Link>
      </nav>

      <Routes>
        <Route path="/" element={<NiaCoreScreen />} />
        <Route path="/museforge" element={<MuseforgeScreen />} />
        <Route path="/polish" element={<PolishScreen />} />
        <Route path="/money" element={<MoneyMunchkinsScreen />} />
        <Route path="/counsel" element={<CounselScreen />} />
        <Route path="/rocky" element={<RockyScreen />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
