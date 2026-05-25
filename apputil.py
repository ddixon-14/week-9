import pandas as pd

#Turn into a class 
class GroupEstimate(object):
    def __init__(self, estimate):
        if estimate not in ('mean', 'median'):
            raise ValueError("Estimate must only be 'mean' or 'median'")
        self.estimate = estimate 
    
    def fit(self, X, y):
    #X- DataFrame of categorical data, Y- 1-D array of continuous values, there should be no miss. vals.
    #1. Group df by columns in X, abstracted
    #2. for.ea. calculate mean or med. of y, depending on estimate arg
        df = X.copy()
        df["y"] = y

        group_cols = list(X.columns)
        self.table = df.groupby(group_cols)["y"].agg(self.estimate)
        print(self.table)
        self.columns = group_cols
        return self

    def predict(self, X_):
    #Takes an array of obv. corresponding to columns in X_,
    # determines appropriate groups, and returns est. for y 
    # return Nan for any missing combinations of data
    # print missing no. of groups
    # 1. search for existing matches
    # 2. Take avg of existing matches
    # 3. count missing combinations 
        predictions = []
        missing_combo = 0
        for i in X_:
            try:
                predictions.append(self.table.loc[i]) #self is pandas series, therefore, loc works
            except KeyError: #counts no. of missing combos and states which are missing
                print(f"Missing combination: {i}")
                predictions.append(float("NaN"))
                missing_combo += 1
        if missing_combo > 0:
            print(f"Total missing groups: {missing_combo}")
        return predictions
    
"""Initialized df for testing 
DF based on possible existing pokemon type combinations and likelihood of capture in the wild. 
"""

coffee_reviews = {
    "loc_country": ["Guatemala", "Japan", "Fiji", "Fiji", "Japan", "Japan", "Fiji", "Guatemala"],
    "roast": ["Dark", "Medium", "Light", "Dark", "Medium", "Medium", "Light", "Dark"],
    "rating": [17.22, 84.34, 39.01, 52.01, 71.89, 25.57, 96.18, 49.03]
}

df_coffee = pd.DataFrame(coffee_reviews)

X = df_coffee[["loc_country", "roast"]]
y = df_coffee["rating"]

gm = GroupEstimate(estimate='mean')
gm.fit(X,y)

X_ = [["Japan", "Medium"],
      ["Guatemala", "Dark"], 
      ["Fiji", "Dark"]] # no dark Fiji

print(gm.predict(X_))

