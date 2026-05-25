import pandas as pd


def GroupEstimate(object):
    def __init__(self, estimate):
        self.estimate = estimate
    
    def fit(self, X, y):
    #X- DataFrame of categorical data, Y- 1-D array of continuous values, there should be no miss. vals.

        return None

    def predict(self, X):
        return None
    
"""Initialized df for testing 
DF based on possible existing pokemon type combinations and win percentage in battle. 
"""
pokemon_df = {
    "pokemon_name": ["Volcanion", "Ludicolo", "Sceptile", "Bewear", "Zebstrika", "Houndoom", "Druddigon", "Fezandipiti", "Gallade"],
    "type1": ["fire", "water", "grass", "normal", "electric", "dark", "dragon", "fairy", "fighting"],
    "type2": ["water", "grass", None, "fighting", None, "fire", None, "poison", "psychic"],
    "win_percentage": [17.22, 84.34, 39.01, 52.01, 71.89, 25.57, 96.10, 41.72, 63.68]
}