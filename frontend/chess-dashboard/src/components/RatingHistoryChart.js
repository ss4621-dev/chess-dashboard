import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import api from "../services/api";

function RatingHistoryChart({ username }) {
  const [ratingHistory, setRatingHistory] = useState([]);

  useEffect(() => {
    const fetchRatingHistory = async () => {
      try {
        const response = await api.get(`/get_rating_history/${username}`);
        setRatingHistory(response.data);
      } catch (error) {
        console.error(`Error fetching rating history for ${username}:`, error);
      }
    };

    fetchRatingHistory();
  }, [username]);

  // Prepare data for the chart (modify based on your API response structure)
  const chartData = {
    labels: ratingHistory.map(
      (entry) => `${entry[0] + 1}/${entry[1]}/${entry[2]}`
    ),
    datasets: [
      {
        label: "Rating History",
        data: ratingHistory.map((entry) => entry[3]),
      },
    ],
  };

  return (
    <div>
      <h2>{`${username}'s Rating History`}</h2>
      <Line data={chartData} />
    </div>
  );
}

export default RatingHistoryChart;
