import React, { useEffect, useState } from "react";
import api from "../services/api";

function TopPlayersList() {
  const [topPlayers, setTopPlayers] = useState([]);

  useEffect(() => {
    const fetchTopPlayers = async () => {
      try {
        const response = await api.get("/get_top_players");
        setTopPlayers(response.data);
      } catch (error) {
        console.error("Error fetching top players:", error);
      }
    };

    fetchTopPlayers();
  }, []);

  return (
    <div>
      <h2>Top Players</h2>
      <ul>
        {topPlayers.map((player) => (
          <li key={player.username}>{player.username}</li>
        ))}
      </ul>
    </div>
  );
}

export default TopPlayersList;
