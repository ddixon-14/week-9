import pandas as pd

#Turn into a class 
def GroupEstimate(object):
    def __init__(self, estimate):
        self.estimate = estimate
    
    def fit(self, X, y):
    #X- DataFrame of categorical data, Y- 1-D array of continuous values, there should be no miss. vals.
    #1. Group df by columns in X, abstracted
    #2. for.ea. calculate mean or med. of y, depending on estimate arg
        if GroupEstimate(estimate='mean'):
            return df_coffee.groupby(X.columns).agg(['mean'])
        else:
            return df_coffee.groupby(X.columns).agg(['median'])

    def predict(self, X_):
    #Takes an array of obv. corresponding to columns in X_,
    # determines appropriate groups, and returns est. for y 
    # return Nan for any missing combinations of data
    # print missing no. of groups
    # 1. loc to select data, search for existing matches
    # 2. Take avg of existing matches
    # 3. count missing combinations 
        predictions = []
        missing_combo = 0
        for i in X_:
            self.table.loc[i]

        return None
    
"""Initialized df for testing 
DF based on possible existing pokemon type combinations and likelihood of capture in the wild. 
"""

coffee_reviews = {
    "loc_country": ["Guatemala", "Japan", "Fiji", "Fiji", "Japan", "Japan", "Fiji", "Guatemala"],
    "roast": ["Dark", "Medium", "Light", "Dark", "Medium", "Medium", "Light", "Dark"],
    "rating": [17.22, 84.34, 39.01, 52.01, 71.89, 25.57, 96.18]
}

df_coffee = pd.DataFrame(coffee_reviews)

X = df_coffee[["loc_country", "roast"]]
y = df_coffee["rating"]

gm = GroupEstimate(estimate='mean')
gm.fit(X,y)

X_ = [["Japan", "Medium"],
      ["Guatemala", "Dark"], 
      ["Fiji", "Dark"]] # no dark Fiji

gm.predict(X_)

