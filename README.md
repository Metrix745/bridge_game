# Bridge Game

This is part of student-developed curriculum in the Quantitative Methods workshop of Meyerhoff Summer Bridge 2025.  The students voted on a project that they wanted to create using python, with the winner being a platformer video game.  The goal of this project was to help familiarize students with Python, Anaconda, tools like random and pygame, and the UMBC UNIX system.  At the end of the 6 week workshop, students presented their custom game to the class and professor.

This repository holds the example game that was developed through live coding sessions during discussion sections.

A small side-scrolling platformer built with Pygame. Enemies drop in every few seconds. Jump on them to score points, and avoid touching them any other way.

## Running

```bash
pip install pygame
python main.py
```

Run it from this folder. The game loads `Parallax/` and `scores.csv` using paths relative to where you start it.

## Controls

| Key | Action |
|-----|--------|
| Left / Right | Move |
| Space or Up | Jump |
| Down | Drop through a platform |

## Scoring

Each enemy you stomped is worth some amount of points. When an enemy touches your side, you lose and type your name and press Enter. The top 5 scores are saved to `scores.csv`.

## Settings

Screen size, speeds, gravity and the enemy spawn rate are set in `settings.py`.

## Credits

The parallax background art in `Parallax/` comes from [russs123/pygame_tutorials](https://github.com/russs123/pygame_tutorials).
