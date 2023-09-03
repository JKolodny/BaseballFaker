""" Generating Fake Baseball Data """

# import libraries
import numpy as np
from faker import Faker

def generation(SEED = 42, 
               CAREER_LENGTH = 20,
                NUMBER_GAMES_SEASON = 162 ):

    """
    Generates Fake Baseball Career Data
    """

    fake = Faker()

    # variable career length
    CAREER_MULTIPLIER = np.random.uniform(0.7, 1.2)
    CAREER_LENGTH = round(CAREER_LENGTH * CAREER_MULTIPLIER)

    # seed
    np.random.seed(SEED)

    # generating name
    # Generate a random male first name
    first_name = fake.first_name_male()

    # Generate a random last name
    last_name = fake.last_name()

    CAREER_STATS = {"Hits": [],
                    "AB": [], 
                    "AVG": [], 
                    "2B": [], 
                    "3B": [], 
                    "HR": [],
                    "Name":[f"{first_name} {last_name}"] * CAREER_LENGTH}

    for _ in range(CAREER_LENGTH):
        HITS = 0
        AB = 0
        _2B = 0
        _3B = 0
        HR = 0
        for _ in range(NUMBER_GAMES_SEASON):
            AT_BATS_IN_GAME = np.random.randint(1, 6)
            OUTCOME = np.random.randint(0, AT_BATS_IN_GAME)
            HITS += OUTCOME
            AB += AT_BATS_IN_GAME

            for _ in range(HITS):
                HIT_TYPE = np.random.randint(0, 22)
                if HIT_TYPE < 16:
                    break
                elif HIT_TYPE < 20:
                    _2B += 1
                elif HIT_TYPE < 21:
                    _3B += 1
                else:
                    HR += 1


        CAREER_STATS["Hits"].append(HITS)
        CAREER_STATS["AB"].append(AB)
        CAREER_STATS["2B"].append(_2B)
        CAREER_STATS["3B"].append(_3B)
        CAREER_STATS["HR"].append(HR)
        CAREER_STATS["AVG"].append(round(HITS / AB, 3))

    return CAREER_STATS