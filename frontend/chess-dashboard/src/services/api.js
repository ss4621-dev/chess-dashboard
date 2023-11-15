import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Replace with your FastAPI server URL
});

export default api;
