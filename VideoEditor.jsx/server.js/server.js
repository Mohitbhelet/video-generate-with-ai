// server.js
const express = require("express");
const cors = require("cors");
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// Mock data for templates
const templates = [
  {
    id: "template_123",
    name: "Marketing Promo",
    description: "Perfect for social media ads.",
    thumbnail: "https://example.com/template-thumbnail.jpg",
  },
];

// GET /api/templates
app.get("/api/templates", (req, res) => {
  res.json(templates);
});

// POST /api/video/generate
app.post("/api/video/generate", (req, res) => {
  const { templateId, script, voiceoverSettings, media, effects } = req.body;

  // Simulate video generation process
  console.log("Generating video with:", { templateId, script, voiceoverSettings, media, effects });

  res.json({ message: "Video generation started!", status: "processing" });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});