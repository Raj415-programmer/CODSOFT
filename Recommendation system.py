import pandas as pd

data = {
    'User': ['Kashif', 'Kashif', 'Kashif', 'Ali', 'Ali', 'John', 'John', 'John'],
    'Item': ['Biscuits', 'Chocolate', 'icecream', 'Biscuits', 'icecream', 'Chocolate', 'Biscuits', 'icecream'],
    'Rating': [5, 4, 3, 4, 2, 3, 5, 4]
}

df = pd.DataFrame(data)

def recommend_items(user, df, n=3):

    target_user_data = df[df['User'] == user]

    item_avg_rating = df.groupby('Item').agg({'Rating': 'mean'}).reset_index()

    similar_items = pd.merge(df, target_user_data, on='Item')
    similar_items = similar_items[similar_items['User_x'] != user]
    similar_items_avg = similar_items.groupby('Item').agg({'Rating_x': 'mean'}).reset_index()

    similar_items_avg = similar_items_avg.sort_values(by='Rating_x', ascending=False)

    top_items = similar_items_avg.head(n)['Item'].tolist()

    return item_avg_rating[item_avg_rating['Item'].isin(top_items)].head(n)

user = 'Kashif'  
recommendations = recommend_items(user, df)
print("Recommendations for", user, ":")
print(recommendations)

user = 'Ali'  
recommendations = recommend_items(user, df)
print("Recommendations for", user, ":")
print(recommendations)

user = 'John'  
recommendations = recommend_items(user, df)
print("Recommendations for", user, ":")
print(recommendations)