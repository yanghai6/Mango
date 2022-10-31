import React from "react";
import { Routes, Route } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";

import NavBar from "./components/nav/NavBar";
import Footer from "./components/Footer";
import Loading from "./components/Loading";

import Home from "./pages/Home";
import PersonaSelection from "./pages/PersonaSelection";
import PersonaHabit from "./pages/PersonaHabit";
import Dashboard from "./pages/Dashboard";
import Train from "./pages/Train";
import Trends from "./pages/Trends";

function App() {
  const { isLoading } = useAuth0();

  if (isLoading) {
    return <Loading />;
  }

  return (
    <div className="App">
      <div className="page-container">
        <div className="content-wrapper">
          <NavBar />
          <Routes>
            <Route exact path="/" element={<Home />} />
            {/* PROTECTED LINKS BELOW*/}
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/trends" element={<Trends />} />
            <Route path="/persona" element={<PersonaSelection />} />
            <Route path="/persona/habit" element={<PersonaHabit />} />
            <Route path="/train" element={<Train />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </div>
  );
}

export default App;
