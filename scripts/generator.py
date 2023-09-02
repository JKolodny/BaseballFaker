""" Generating Fake Baseball Data """
import json
import numpy as np

# importing assumptions
with open("../assumptions.json", "r", encoding="utf-8") as f:
    assumptions = json.load(f)

# assumptions
RANDOM_SEED = assumptions["RANDOM_SEED"]
CAREER_LENGTH = assumptions["CAREER_LENGTH"]
NUMBER_GAMES_SEASON = assumptions["NUMBER_GAMES_SEASON"]

# seed
np.random.seed(RANDOM_SEED)

CAREER_STATS = {"Hits": [], 
                "AB": [],
                "AVG": []}
for _ in range(CAREER_LENGTH):
    SEASON_STATS = 0
    AB = 0
    for _ in range(NUMBER_GAMES_SEASON):
        AT_BATS_IN_GAME = np.random.randint(1, 6)
        OUTCOME = np.random.randint(0, AT_BATS_IN_GAME)
        SEASON_STATS += OUTCOME
        AB += AT_BATS_IN_GAME

    CAREER_STATS["Hits"].append(SEASON_STATS)
    CAREER_STATS["AB"].append(AB)
    CAREER_STATS["AVG"].append(round(SEASON_STATS/AB, 3))

print(CAREER_STATS)
