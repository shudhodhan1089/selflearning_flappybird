# 🐦 Self-Learning Flappy Bird Bot

A **self-learning AI bot** that learns to play **Flappy Bird** automatically using reinforcement learning. Instead of manually controlling the bird, the bot observes the game environment, makes decisions, and gradually improves its performance through trial and error.

## 🧠 How It Works

The bot uses a simple learning approach:

* **State:** Bird's position, velocity, and distance/position of the pipes.
* **Action:** Jump or do nothing.
* **Reward:** Positive reward for surviving and passing pipes, with a penalty for hitting a pipe or the ground.
* **Learning:** The bot updates its strategy based on the rewards it receives.

Over multiple generations/episodes, the bot learns to avoid pipes and achieve higher scores.

## 🛠️ Technologies

* Python
* Pygame
* Reinforcement Learning
* NumPy

## 🚀 Goal

The main goal of this project is to demonstrate how an AI agent can **learn to play a game autonomously without being explicitly programmed with the solution**.

## 📌 Future Improvements

* Improve the learning algorithm
* Add visualization of the learning process
* Experiment with neural networks
* Optimize training speed

---

**Made as an AI/ML self-learning project.**
