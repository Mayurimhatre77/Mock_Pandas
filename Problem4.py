import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['year'] = orders['order_date'].dt.to_period('Y')
    orders_2019 = orders[orders['year'] == '2019']
    num_orders = orders_2019.groupby('buyer_id')['order_id'].count().reset_index(name = 'orders_in_2019')
    result = users.merge(num_orders, how = 'left', left_on = 'user_id', right_on = 'buyer_id')
    result = result[['user_id', 'join_date', 'orders_in_2019']]
    result = result.rename(columns = {'user_id':'buyer_id'})
    result = result.fillna(0)
    return result