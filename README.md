🌌 SentinelVerse
🔍 Overview
SentinelVerse is an innovative WebGL-based cybersecurity simulation game, crafted by Nexus Game India for Google Summer of Code 2025. Designed to educate users through immersive interaction, the project gamifies real-world digital threats using a nostalgic 8-bit retro aesthetic.

In a browser-accessible experience hosted on GitHub Pages, users encounter 80 realistic threat scenarios—ranging from phishing to misinformation—and must choose whether to "Trust," "Visit this Link," or "Use Guardian AI." Every decision earns or loses points, turning cybersecurity awareness into a challenge of intuition and smart choices.

✨ Features
🎮 Retro Pixel Design
A 1280×720 interface styled with 8-bit graphics, glowing green code, red/green buttons, and animated effects (e.g., blinking alerts).

🧠 Interactive Gameplay
Cycle through 80 curated digital threats, making decisions that affect your score:

✅ Trust → +30 if correct

🔗 Visit link → +10 if safe, –10 if unsafe

🛡 Use Guardian AI → +10, with a 5-use limit (refreshed after 5 correct choices)

🤖 Guardian AI Assistant
A built-in decision advisor that evaluates threats and offers safe recommendations—limited to 5 uses per session.

🌐 WebGL Compatibility
Seamlessly playable in any modern browser (Chrome, Firefox, etc.), optimized for low-end devices.

🎓 Educational Value
Enhances digital literacy through gamification—ideal for students, professionals, and cyber-awareness campaigns.

🚀 Getting Started
✅ Prerequisites
A modern web browser (Chrome, Firefox, Edge)

Git (for cloning the repository)

GitHub account (for deployment)

🧩 Installation Steps
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/SentinelVerse.git
cd SentinelVerse
Prepare the Dataset

Place your output.json (with 80 threat entries) inside Assets/Resources/

Sample entry:

json
Copy
Edit
{
  "id": 1,
  "analysis": {"type": "phishing", "confidence": 0.9},
  "recommendation": "Use Guardian AI"
}
Host on GitHub Pages

Build your WebGL version in Unity or export via your chosen frontend tool.

Push the /Build folder to your repository.

Go to Settings > Pages and set the source to /main or /docs.

Your live link will be:
https://yourusername.github.io/SentinelVerse/

🕹 Usage
Launch the WebGL game from your deployed link.

Review threat messages and choose:

🔓 Trust

🔗 Visit Link

🛡 Use Guardian AI

Earn or lose points based on your choice and the AI’s analysis.

Progress through all 80 scenarios.

The Guardian AI resets after 5 correct guesses, adding strategic depth.

🗂 Project Structure
graphql
Copy
Edit
SentinelVerse/
├── Assets/
│   └── Resources/
│       └── output.json        # Threat data
├── Build/                     # WebGL build for deployment
├── README.md                  # You're reading it!
└── LICENSE                    # Add MIT, Apache, or preferred license
🧰 Development Tools
Tool	Purpose
Unity	Prototyping and WebGL build generation
Lovable AI (or similar)	No-code/low-code WebGL frontend creation
GitHub Pages	Deployment and live demo hosting
⚙ Implementation Details
UI Design: Retro-styled Canvas, pixel art fonts, neon highlights

Logic:

If "Trust" and confidence > 0.5 → +30 points

If "Visit Link" and safe → +10 points; if unsafe → –10

Using Guardian AI → +10 (5-use cap)

Data Handling:

Reads output.json dynamically

Cycles seamlessly through 80 scenarios

🤝 Contributing
We welcome community contributions!

Fork this repo

Create a new branch

bash
Copy
Edit
git checkout -b feature-name
Commit your changes

bash
Copy
Edit
git commit -m "Add feature"
Push and create a pull request.

📝 Please follow coding standards and test before submitting.

📄 License
This project is open-source.
Feel free to use, modify, and distribute with proper attribution.

(Specify MIT, Apache 2.0, or other license here)

🙏 Acknowledgments
Google Summer of Code 2025 – For enabling this innovative initiative

Nexus Game India – For mentorship, design, and vision

Open-source Community – For libraries, tools, and inspiration

📫 Contact
For collaboration, suggestions, or feedback:
📧 your.email@example.com
📌 Or open an issue on this GitHub repository

🔗 Live Demo
🎮 Experience the Guardian AI in action:
🌍 https://yourusername.github.io/SentinelVerse/
(Replace with your actual deployed URL)

⚠ Notes
✅ Focuses on user success and functionality—avoids technical struggle talk

🔧 Customize usernames, emails, and URLs before submission

📊 Confirm output.json is valid and placed in Assets/Resources/

🔁 Test GitHub Pages link before sharing

Let me know if you want:

A shortened README version (for slides or mobile view)

A .md file to copy directly

A visual layout suggestion for your GitHub repo

You’re killing it. Let’s make SentinelVerse unforgettable 🚀🛡
