# AI‑First Software Development Workshop

Welcome to the AI‑First Software Development Workshop — a hands-on, real-world guided experience for junior developers who want to master AI-first workflows and practices.

## 🌟 Workshop Goals

- Introduce the AI‑First Software Development (AIFSD) mindset
- Learn to integrate GitHub Copilot and prompt engineering into daily development
- Practice real-world workflows using an open-source Flask to-do app
- Shift from human-led to AI-assisted and eventually AI-augmented coding

## 🧰 Tech Stack

- Python 3.10+
- Flask (based on [patrickloeber/flask-todo](https://github.com/patrickloeber/flask-todo))
- GitHub Copilot
- Markdown & Prompt Files

## 🗂️ Project Structure

.
├── app/                    # Flask to-do app
├── copilot/                # Copilot instructions and prompts
├── docs/                   # Workshop lessons and walkthroughs
├── requirements.txt        # Flask app dependencies
└── README.md               # You're here!

## ⚙️ Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/patrickloeber/flask-todo.git app
   cd app
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Run the App**
   ```bash
   python app.py
   ```

Then go to `http://localhost:5000` in your browser.

## 🧠 Workshop Modules

Each module lives in the `docs/` folder and includes a combination of:
- Lessons
- Group exercises
- Prompts
- Live demos

## 🚀 Start with `docs/00_agenda.md`

<!-- 
Workshop Structure and Roadmap
This workshop is structured into six sessions, each focusing on a specific aspect of AI-first software development. Below is an overview of the sessions (with estimated durations) and what you’ll learn in each. Detailed instructions and activities for each session are available in the /docs directory.

[docs/01-introduction-to-ai-first-development.md]Introduction to AI-First Development (30 min) – Overview of the AI-First Software Development Manifesto (by Tembo) and key mindset shifts. Includes discussion of current AI usage and a demonstration of letting AI generate a first attempt at code.
[docs/02-customizing-github-copilot-in-ides.md]Customizing GitHub Copilot in IDEs (45 min) – Learn how to tailor Copilot’s behavior using custom instructions and prompt files, and explore Copilot’s different modes (inline vs. chat). Includes a live demo of adding a .copilot-instructions.md file to the project.
[docs/03-ai-onboarding-with-an-open-source-app.md]AI Onboarding with an Open Source App (30 min) – Use AI to rapidly understand a new codebase (the Flask to-do app). You will practice exploring the code with Copilot, generating documentation, and identifying key components with AI’s help.
[docs/04-implementing-user-stories-with-ai.md]Implementing User Stories with AI Collaboration (90 min) – Work on new feature development for the to-do app using Copilot as your pair programmer. You’ll implement given user stories, iteratively prompt Copilot, and refine your .copilot-instructions.md based on AI’s output.
[docs/05-vibe-coding-beast-mode.md]Vibe Coding with Beast Mode (60 min) – An advanced exercise in which you let the AI attempt to complete a task end-to-end (“Beast Mode”). You’ll provide high-context instructions (an extensive prompt) for a feature and let Copilot drive the implementation, then assess the results.
[docs/06-wrap-up-reflection.md]Wrap-Up & Reflection (30 min) – Conclude with a group reflection on lessons learned and challenges faced. We’ll discuss how an AI-first approach can be adopted in real-world team workflows, its impact on team dynamics, and strategies for using AI responsibly at scale.
Feel free to navigate to each session’s document for detailed guidance. We recommend going through the sessions in order, as they build on each other. Good luck, and enjoy the workshop! -->