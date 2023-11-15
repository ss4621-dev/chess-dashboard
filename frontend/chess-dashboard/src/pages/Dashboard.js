import React from "react";
import TopPlayersList from "../components/TopPlayersList";
import RatingHistoryChart from "../components/RatingHistoryChart";

function Dashboard() {
  return (
    <div>
      <TopPlayersList />
      <RatingHistoryChart username="selectedUsername" />
    </div>
  );
}

export default Dashboard;
