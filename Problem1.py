import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[cinema["description"] != "boring"]
    df = test[test["id"] % 2 != 0]
    df.sort_values(by = "rating", ascending = False, inplace = True)
    return df
    