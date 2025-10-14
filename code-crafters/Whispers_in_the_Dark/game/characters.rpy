""" 
Characters file: add all the playable characters here
Each Character has 5 different stats: name, strength, intelligence, fortitude, and bio.

Once a player makes a selection in the character_selection and character_confirm screen
the game will jump to label: start_game. Everwhere after this point the selected characters
stats can be summoned with char['name'] , char['strength'] , char['bio'], ... ect 


-Tanner did this, ask me for questions
    -This was changed from a custom class to a dictionary to fix the save/reload functionality
"""
# Define the selectable characters as dictionaries
default mc_e = {
    "name": "Evelyn Carter",
    "strength": 4,
    "intelligence": 6,
    "fortitude": 9,
    "bio": "A fearless electrician who believes every paranormal event has a logical explanation. Her expertise with electrical systems and lighting proves invaluable in the mansion’s eerie darkness."
}

default mc_j = {
    "name": "Jeremy Hardin",
    "strength": 2,
    "intelligence": 7,
    "fortitude": 4,
    "bio": "A stoic cameraman who prefers to observe rather than interfere. His advanced camera tech captures what the naked eye cannot, revealing hidden threats in the shadows."
}

default mc_s = {
    "name": "Sam Winchester",
    "strength": 3,
    "intelligence": 9,
    "fortitude": 7,
    "bio": "A historian and occult expert with a fascination for the unknown. His ability to decipher symbols and analyze EVP recordings helps uncover the mansion’s dark secrets."
}

default mc_d = {
    "name": "Dean Winchester",
    "strength": 9,
    "intelligence": 2,
    "fortitude": 8,
    "bio": "A hardened survivalist and skeptic who trusts in preparation over superstition. His combat skills and quick thinking make him the team’s best defense against the unknown."
}

default mc_m = {
    "name": "Michael Redwood",
    "strength": 6,
    "intelligence": 6,
    "fortitude": 7,
    "bio": "A determined journalist obsessed with exposing the truth. His sharp instincts and leadership keep the team together, but his drive sometimes blinds him to danger."
}