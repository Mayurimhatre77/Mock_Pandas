import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged_df = sales.groupby("product_id")["sale_date"].agg([min, max]).reset_index()
    merged_df=merged_df[(merged_df['min']>='2019-01-01') & (merged_df['min']<='2019-03-31')]
    merged_df=merged_df[(merged_df['max']>='2019-01-01') & (merged_df['max']<='2019-03-31')]
    return pd.merge(left=product,right=merged_df,on='product_id')[['product_id','product_name']]