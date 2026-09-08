import pandas as pd

df = pd.read_excel("Flipkart_Data_Extract_Final.xlsx")

df.columns = df.columns.str.strip()

df = df.rename(columns={
    "name": "Product_Name",
    "Rating": "Rating",
    "price": "Price",
    "brand": "Brand",
    "product_url": "Product_URL"
})

df["Product_Name"] = (
    df["Product_Name"]
    .fillna("")
    .astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

df["Brand"] = (
    df["Brand"]
    .fillna("")
    .astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

df["Price"] = (
    df["Price"]
    .fillna("")
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

df["Rating"] = (
    df["Rating"]
    .fillna("")
    .astype(str)
    .str.extract(r"(\d+(?:\.\d+)?)")[0]
)

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

df["Product_URL"] = (
    df["Product_URL"]
    .fillna("")
    .astype(str)
    .str.strip()
)

df.loc[
    ~df["Rating"].between(0, 5),
    "Rating"
] = pd.NA

df.loc[
    df["Price"] < 0,
    "Price"
] = pd.NA

df = df.drop_duplicates()
df = df.reset_index(drop=True)
df.to_csv(
    "Flipkart_Data_Extract_Final_Cleaned.csv",
    index=False
)

df.to_excel(
    "Flipkart_Data_Extract_Final_Cleaned.xlsx",
    index=False
)
print("Cleaning Completed Successfully")
