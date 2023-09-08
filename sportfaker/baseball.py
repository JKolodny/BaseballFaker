""" Generating Fake Baseball Data """

# import libraries
import numpy as np
from faker import Faker
import pandas as pd


def batting(CAREER_LENGTH=20, NUMBER_GAMES_SEASON=162, DETERMINISTIC=True):

    """
    Generates fake baseball career data for a player using random statistics.

    Parameters:
    - CAREER_LENGTH (int, optional): Number of years the player's career lasts. Default is 20.
    - NUMBER_GAMES_SEASON (int, optional): Number of games in a season. Default is 162.
    - DETERMINISTIC (bool, optional): If True, the career length is fixed. If False, the career length is randomized. Default is True.

    Returns:
    - pd.DataFrame: A DataFrame containing the player's career statistics, including At Bats (AB), Hits, Doubles (2B), Triples (3B), Home Runs (HR), Runs Batted In (RBI), Batting Average (AVG), Slugging Percentage (SLG), and the player's Name. The last row contains the career totals.

    Note:
    The function uses the Faker library to generate a random player name and numpy for random number generation.
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

    CAREER_STATS = {
        "AB": [],
        "Hits": [],
        "2B": [],
        "3B": [],
        "HR": [],
        "RBI": [],
        "BB": [],
        "AVG": [],
        "OBP": [],
        "SLG": [],
        "OPS": [],
        "Name": [f"{first_name} {last_name}"] * CAREER_LENGTH,
    }

    for _ in range(CAREER_LENGTH):

        HITS = 0
        AB = 0
        _2B = 0
        _3B = 0
        HR = 0
        RBI = 0
        _BB = 0

        for _ in range(NUMBER_GAMES_SEASON):
            AT_BATS_IN_GAME = round(np.random.uniform(2, 5))
            HIT_MULTIPLIER = np.random.uniform(0.5, 0.9)
            OUTCOME = np.random.randint(0, AT_BATS_IN_GAME)
            HITS += round(OUTCOME * HIT_MULTIPLIER)
            AB += AT_BATS_IN_GAME
            BB_MULTIPLIER = np.random.uniform(0.06, 0.2)

            for _ in range(HITS):
                HIT_TYPE = np.random.randint(0, 22)
                if HIT_TYPE < 16:
                    break
                elif HIT_TYPE < 20:
                    RBI += 0.5
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
        WALKS = AB * BB_MULTIPLIER
        CAREER_STATS["BB"].append(round(WALKS))
        OBP = round(((HITS + WALKS)/(AB + _BB)), 3)
        CAREER_STATS["OBP"].append(OBP)


        singles = HITS - (_2B + _3B + HR)
        total_bases = singles + (2 * _2B) + (3 * _3B) + (4 * HR)
        SLUGGING = round((total_bases / AB), 3)
        CAREER_STATS["SLG"].append(SLUGGING)
        CAREER_STATS["OPS"].append(SLUGGING + OBP)

    CAREER_STATS = pd.DataFrame(CAREER_STATS)
    totals = pd.DataFrame(CAREER_STATS.sum()).T
    totals["AVG"] = round(CAREER_STATS["AVG"].mean(), 3)
    totals["SLG"] = round(CAREER_STATS["SLG"].mean(), 3)
    totals["OBP"] = round(CAREER_STATS["OBP"].mean(), 3)
    totals["OPS"] = round(CAREER_STATS["OPS"].mean(), 3)
    totals["Name"] = CAREER_STATS["Name"][0]

    CAREER_STATS = pd.concat([CAREER_STATS, totals])
    CAREER_STATS.index = list(CAREER_STATS.index)[:-1] + ["Career Totals"]

    return CAREER_STATS


def pitching():

    """
    Generates Fake Baseball Career Pitching Data

    INPUT:

    OUTPUT:
    """
    return "Nothing Yet!"


def fielding():

    """
    Generates Fake Baseball Career Fielding Data

    INPUT:

    OUTPUT:
    """
    return "Nothing Yet!"
