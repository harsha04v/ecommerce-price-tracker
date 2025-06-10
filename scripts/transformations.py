import pandas as pd

dataset_path=r'C:\Users\CC245MD\OneDrive - EY\Desktop\DESK\Projects\ecommerce-de-project\data\cleaned_data.csv'

df=pd.read_csv(dataset_path,sep=',',header=0)


df['timestamp']=pd.to_datetime(df['timestamp'])
df['date']=df['timestamp'].dt.date
df['year']=df['timestamp'].dt.year
df['month']=df['timestamp'].dt.month
df['day']=df['timestamp'].dt.day


df['initial_price'] = df['initial_price'].astype(float)
df['final_price'] = df['final_price'].astype(float)
df['discount_pct'] = ((df['initial_price'] - df['final_price']) / df['initial_price']) * 100


df['is_discounted'] = df['discount_pct'] > 0
df['is_price_dropped'] = df['discount_pct'] > 0
df['is_same_price'] = df['initial_price'] == df['final_price']


df['categories_array'] = df['categories'].apply(lambda x: x.strip('[]').split(',') if pd.notnull(x) else [])

df['main_category'] = df['categories_array'].apply(lambda x: x[0].strip().strip('"') if len(x) > 0 else None)
df['sub_category'] = df['categories_array'].apply(lambda x: x[1].strip().strip('"') if len(x) > 1 else None)


high_rated = df[df['rating'] >= 4.0]


brand_avg_price = df.groupby('brand')['final_price'].mean().reset_index()

df.to_csv("C:/Users/CC245MD/OneDrive - EY/Desktop/DESK/Projects/ecommerce-de-project/data/transformed_ecommerce_data.csv", index=False)
high_rated.to_csv("C:/Users/CC245MD/OneDrive - EY/Desktop/DESK/Projects/ecommerce-de-project/data/high_rated_products.csv", index=False)
brand_avg_price.to_csv("C:/Users/CC245MD/OneDrive - EY/Desktop/DESK/Projects/ecommerce-de-project/data/brand_avg_price.csv", index=False)

#print(df.columns)