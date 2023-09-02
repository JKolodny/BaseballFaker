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

CAREER_STATS = []
for _ in range(CAREER_LENGTH):
    SEASON_STATS = 0
    for _ in range(NUMBER_GAMES_SEASON):
        AT_BATS_IN_GAME = np.random.randint(1, 6)
        OUTCOME = np.random.randint(0, AT_BATS_IN_GAME)
        SEASON_STATS += OUTCOME

    CAREER_STATS.append(SEASON_STATS)

print(CAREER_STATS)
print(sum(CAREER_STATS))
