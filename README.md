
## Snake AI with Reinforcement Learning
This project implements the classic Snake game in Python using Pygame, enhanced with a simple reinforcement learning 
AI that learns and improves over generations.

# Features
Classic Snake game mechanics with grid-based movement.

AI controlled by a genetic algorithm for reinforcement learning.

Real-time visualization of the game and AI performance graph side-by-side.

Organized code in classes and modules for easy maintenance and extension.

Adjustable parameters for number of episodes, grid size, and AI behavior.

Learning curve visualization using matplotlib.

# Technologies

Python 3.10+

Pygame for game rendering

Matplotlib for plotting

Genetic algorithm for AI training

How to run
Clone the repository:

git clone <repo-url>

cd snake-ai-project

Create and activate a virtual environment (recommended):

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows

Install dependencies:

pip install pygame matplotlib numpy

Run the main script:

python main.py

The AI will train for a set number of episodes, displaying the game and the learning graph side-by-side.

# Project structure

snake-ai-project/

├── main.py          # Main script with game loop and AI training

├── game.py          # SnakeGame class and game logic

├── ai.py            # AI logic and genetic algorithm

├── plotter.py       # Code for plotting graphs

├── assets/          # Assets folder (images, fonts etc)

├── README.md        # This documentation file


# Contribution
Contributions welcome! Open issues or pull requests.

# Author
Rodrigo Assarice

--

## Snake AI com Aprendizado por Reforço

Este projeto implementa o clássico jogo da cobrinha (Snake) em Python usando Pygame, com uma IA simples baseada em 
aprendizado por reforço que aprende a jogar e melhorar ao longo de gerações.

Funcionalidades
Mecânica tradicional do jogo Snake com movimento em grade.

IA controlada por algoritmo genético para aprendizado por reforço.

Visualização em tempo real do jogo e do gráfico de desempenho da IA lado a lado.

Código organizado em classes e módulos para fácil manutenção e expansão.

Parâmetros ajustáveis para número de episódios, tamanho da grade e comportamento da IA.

Visualização da curva de aprendizado com matplotlib.

# Tecnologias
Python 3.10+

Pygame para renderização do jogo

Matplotlib para gráficos

Algoritmo genético para treinamento da IA

Como executar
Clone o repositório:

git clone <url-do-repositorio>

cd snake-ai-project

Crie e ative um ambiente virtual (recomendado):

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows

Instale as dependências:

pip install pygame matplotlib numpy
Rode o script principal:


python main.py
A IA irá treinar por um número definido de episódios, mostrando o jogo e o gráfico de evolução lado a lado.

# Estrutura do projeto

snake-ai-project/

├── main.py          # Script principal com loop do jogo e treinamento da IA

├── game.py          # Classe SnakeGame e lógica do jogo

├── ai.py            # Lógica da IA e algoritmo genético

├── plotter.py       # Código para gerar gráficos

├── assets/          # Pasta de assets (imagens, fontes etc)

├── README.md        # Este arquivo de documentação

# Contribuição
Contribuições são bem-vindas! Abra issues ou pull requests.

# Autor
Rodrigo Assarice