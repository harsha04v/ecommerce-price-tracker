import pandas as pd

dataset_path=r"C:\Users\CC245MD\OneDrive - EY\Desktop\DESK\Projects\ecommerce-de-project\data\amazon-products.csv"

output_path=r"C:\Users\CC245MD\OneDrive - EY\Desktop\DESK\Projects\ecommerce-de-project\data\cleaned_data.csv"

imp_col= ['timestamp','title', 'brand', 'initial_price', 'final_price', 'currency','availability','is_available',
          'rating','discount','seller_id','asin','categories']

def clean_data(dataset_path,output_path):
    df=pd.read_csv(dataset_path,sep="," ,header=0,quotechar='"')

    df= df[imp_col]

    df.dropna(subset=['timestamp','title','initial_price','final_price','asin'], inplace=True)

    df.fillna({
        'brand':'unknown',
        'currency':'unknown',
        'availability': 'Unknown',
        'rating': 0,
        'categories': 'Unknown',}, inplace=True)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['initial_price'] = df['initial_price'].astype(str).str.replace('"', '').astype(float)
    df['final_price'] = df['final_price'].astype(str).str.replace('"', '').astype(float)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)

    df.to_csv(output_path,index=False)
    print(f"Cleaned data saved to {output_path}")

clean_data(dataset_path,output_path)
