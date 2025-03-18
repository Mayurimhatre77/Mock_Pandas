import pandas as pd

def biggest_single_number(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby('num').size().reset_index(name='count')
    single_numbers_arr = grouped[ ( grouped['count'] == 1 ) ]
    single_number = single_numbers_arr['num'].max()
    single_dataFrame = pd.DataFrame( { 'num':[single_number] } )
    return single_dataFrame