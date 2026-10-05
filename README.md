# Self-Learning Flappy Bird AI (NEAT-Python)

Originally built as a first-year engineering project using Pygame, this repository has been upgraded into a machine learning simulation. Instead of relying on manual keyboard input, the game is now controlled by an artificial intelligence that learns to play entirely on its own using **NEAT** (NeuroEvolution of Augmenting Topologies).

The AI is implemented via an external wrapper (`ai_runner.py`) that imports the original, untouched game classes and trains a population of neural networks to master the game through simulated biological evolution.

## How the AI Works: The Magic of NEAT

Traditional neural networks (like those used in image recognition) have a fixed architecture and learn by tweaking their internal weights using gradient descent. 

NEAT takes a different, biologically-inspired approach. It doesn't just alter the weights; it evolves the **topology** (the actual structure) of the network itself. It starts with incredibly simple brains and slowly mutates them, adding new neurons and connections over generations only when they provide a survival advantage.

### The Genetic Algorithm in Action

To teach the AI how to play Flappy Bird, the script mimics natural selection using the following steps:

1. **Observation (The Senses)** 
   Each bird is given its own neural network. Every frame, the network looks at exactly three variables:
   * The bird's current Y-coordinate.
   * The absolute distance to the top pipe.
   * The absolute distance to the bottom pipe.
   
2. **The Initial Population (Generation 0)**
   The simulation spawns a population of 50 birds. Initially, their neural networks have random weights. Most will instantly dive into the ground or fly off into space.

3. **Fitness Evaluation (Survival of the Fittest)**
   As the birds play, they are scored based on a **Fitness Function**:
   * `+0.1` points for every frame they stay alive (encouraging survival).
   * `+5.0` points for successfully passing through a pipe (encouraging progression).
   * `-1.0` point penalty for hitting a pipe or the floor (punishing failure).

4. **Natural Selection & Crossover (Reproduction)**
   When all 50 birds die, the generation ends. The algorithm evaluates the fitness scores and kills off the worst-performing birds. The top performers (the "elite") are selected to breed. Their neural networks are crossed over (mixing traits from two successful parents) to spawn the next generation of 50 birds.

5. **Mutation & Speciation (Evolution)**
   As new offspring are generated, there is a small mathematical probability of mutation:
   * **Weight Mutations:** Existing connection strengths are randomly tweaked.
   * **Structural Mutations:** A new hidden node or a brand-new connection between nodes is randomly added.
   
   To prevent new, promising mutations from being immediately wiped out by established networks, NEAT uses **Speciation**. It groups similar neural networks into "species" so they only compete with their peers until they have time to optimize their new structures.

By Generation 15–30, the algorithm typically discovers a neural structure capable of playing the game flawlessly forever.

## Project Structure

* **Original Source (`bird.py`, `pipe.py`, `world.py`):** The foundational Pygame mechanics built during my first year. These remain completely unmodified.
* **`ai_runner.py`:** The AI wrapper. It imports the original game objects, bypasses the manual game loop, and handles the NEAT population evaluation and fitness tracking.
* **`config-feedforward.txt`:** The configuration file containing the hyper-parameters for the genetic algorithm (population size, mutation rates, threshold limits).

## Running the Simulation

**Prerequisites:**
You will need Python installed along with Pygame and NEAT-Python.

```bash
pip install pygame neat-python

https://github.com/user-attachments/assets/3230df57-65c6-43aa-a169-d8bea472aa76



