import { render, screen } from "@testing-library/react";
import { createMemoryHistory } from "history";
import { BrowserRouter, Router } from "react-router-dom";

import React from "react";

import NavBar from "../../App/components/nav/NavBar";
import Footer from "../../App/components/Footer";
import Profile from "../../App/components/Profile";
import Dashboard from "../../App/pages/Dashboard";
import Home from "../../App/pages/Home";
import PersonaHabit from "../../App/pages/PersonaHabit";
import PersonaSelection from "../../App/pages/PersonaSelection";
import Train from "../../App/pages/Train";
import Trends from "../../App/pages/Trends";

test("Home loading text initially", () => {
  render(
    <BrowserRouter>
      <Home />
    </BrowserRouter>
  );
  const linkElement = screen.getByText(/Book a demo/i);
  expect(linkElement).toBeInTheDocument();
});

test("Navbar renders pre-signin", () => {
  render(
    <BrowserRouter>
      <NavBar />
    </BrowserRouter>
  );
  const linkElement = screen.getByText(/Catered towards your usage/i);
  expect(linkElement).toBeInTheDocument();
});

test("Footer renders pre-signin", () => {
  render(
    <BrowserRouter>
      <Footer />
    </BrowserRouter>
  );
  const linkElement = screen.getByText(/Mango Technologies/i);
  expect(linkElement).toBeInTheDocument();
});

test("Profile renders pre-signin", () => {
  render(<Profile />);
  const linkElement = screen.getByText(/Ripening/i);
  expect(linkElement).toBeInTheDocument();
});

test("Dashboard renders pre-signin", () => {
  render(<Dashboard />);
  const linkElement = screen.getByText(/Dashboard/i);
  expect(linkElement).toBeInTheDocument();
});

test("PersonaHabit loading text initially", () => {
  const history = createMemoryHistory();
  const state = { selection: 123, b: 456 };
  history.push("/persona/habit", state);
  render(
    <Router location={history.location} navigator={history}>
      <PersonaHabit />
    </Router>
  );
  const linkElement = screen.getByText(/Prediction General Habits/i);
  expect(linkElement).toBeInTheDocument();
});

test("PersonaSelection loading text initially", () => {
  const history = createMemoryHistory();
  const state = {
    selection: {
      age: { value: 0 },
      gender: { value: 0 },
      marital_status: { value: 0 },
      education: { value: 0 },
      income: { value: 0 },
    },
    b: 456,
  };
  history.push("/persona", state);
  render(
    <Router location={history.location} navigator={history}>
      <PersonaSelection />
    </Router>
  );
  const linkElement = screen.getByText(/Persona Prediction/i);
  expect(linkElement).toBeInTheDocument();
});

test("Train loading text initially", () => {
  const history = createMemoryHistory();
  const state = {
    selection: 0,
    b: 456,
  };
  history.push("/train", state);
  render(
    <Router location={history.location} navigator={history}>
      <Train />
    </Router>
  );
  const linkElement = screen.getByText(/Enhancing Your model/i);
  expect(linkElement).toBeInTheDocument();
});

test("Trends loading text initially", () => {
  const history = createMemoryHistory();
  const state = {
    selection: 0,
    b: 456,
  };
  history.push("/trend", state);
  render(
    <Router location={history.location} navigator={history}>
      <Trends />
    </Router>
  );
  const linkElement = screen.getByText(/Change in consumption/i);
  expect(linkElement).toBeInTheDocument();
});
