""" Generating Fake Baseball Data """

# import libraries
import numpy as np
from faker import Faker
import pandas as pd

def baseball_batting(CAREER_LENGTH = 20,
                NUMBER_GAMES_SEASON = 162,
                DETERMINISTIC = True):

    """
    Generates Fake Baseball Career Data
    """

    fake = Faker()

    # variable career length
    if not DETERMINISTIC:
        CAREER_MULTIPLIER = np.random.uniform(0.7, 1.2)
        CAREER_LENGTH = round(CAREER_LENGTH * CAREER_MULTIPLIER)

    # generating name
    # Generate a random male first name
    first_name = fake.first_name_male()

    # Generate a random last name
    last_name = fake.last_name()

    CAREER_STATS = {"AB": [],
                    "Hits": [], 
                    "AVG": [], 
                    "2B": [], 
                    "3B": [], 
                    "HR": [],
                    "RBI": [],
                    "Name":[f"{first_name} {last_name}"] * CAREER_LENGTH}

    for _ in range(CAREER_LENGTH):

        HITS = 0
        AB = 0
        _2B = 0
        _3B = 0
        HR = 0
        RBI = 0

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
                    RBI += .5
                    _2B += 1
                elif HIT_TYPE < 21:
                    RBI += 1
                    _3B += 1
                else:
                    RBI += 2
                    HR += 1


        CAREER_STATS["AB"].append(AB)
        CAREER_STATS["Hits"].append(HITS)
        CAREER_STATS["2B"].append(_2B)
        CAREER_STATS["3B"].append(_3B)
        CAREER_STATS["HR"].append(HR)
        CAREER_STATS["RBI"].append(round(RBI))
        CAREER_STATS["AVG"].append(round(HITS / AB, 3))

    CAREER_STATS = pd.DataFrame(CAREER_STATS)
    totals = pd.DataFrame(CAREER_STATS.sum()).T
    totals['AVG'] = round(CAREER_STATS['AVG'].mean(), 3)
    totals['Name'] = CAREER_STATS['Name'][0]

    CAREER_STATS = pd.concat([CAREER_STATS, totals])
    CAREER_STATS.index = list(CAREER_STATS.index)[:-1] + ['Career Totals']

    return CAREER_STATS