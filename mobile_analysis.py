import pandas as pd

# Load dataset
df = pd.read_csv("Flipkart_Mobiles.csv")

# Display basic information
print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)
print("\nFirst 5 Rows:")
print(df.head())

# Top 10 brands
print("\nTop 10 Mobile Brands")

top_brands = df["Brand"].value_counts().head(10)

print(top_brands)

import matplotlib.pyplot as plt

# Top 10 brands chart
top_brands.plot(kind="bar", figsize=(10,5))

plt.title("Top 10 Mobile Brands")
plt.xlabel("Brand")
plt.ylabel("Number of Mobiles")

plt.tight_layout()

# Save chart
plt.savefig("top_10_brands.png")

plt.show()



# Price Analysis

print("\nPrice Analysis")

print("Average Selling Price:", df["Selling Price"].mean())

print("Highest Selling Price:", df["Selling Price"].max())

print("Lowest Selling Price:", df["Selling Price"].min())


plt.figure(figsize=(10,5))

df["Selling Price"].hist(bins=30)

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Number of Mobiles")

plt.savefig("price_distribution.png")

plt.show()


# Rating Analysis

print("\nRating Analysis")

print("Average Rating:", round(df["Rating"].mean(), 2))

print("Highest Rating:", df["Rating"].max())

print("Lowest Rating:", df["Rating"].min())

plt.figure(figsize=(10,5))

df["Rating"].hist(bins=10)

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Mobiles")

plt.savefig("rating_distribution.png")

plt.show()


brand_rating = (
    df.groupby("Brand")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Rated Brands")
print(brand_rating)

brand_rating.plot(kind="bar", figsize=(10,5))

plt.title("Top Rated Brands")
plt.xlabel("Brand")
plt.ylabel("Average Rating")

plt.tight_layout()

plt.savefig("top_rated_brands.png")

plt.show()

# Average Selling Price by Brand

brand_price = (
    df.groupby("Brand")["Selling Price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nMost Expensive Brands")
print(brand_price)


plt.figure(figsize=(10,5))

brand_price.plot(kind="bar")

plt.title("Average Selling Price by Brand")
plt.xlabel("Brand")
plt.ylabel("Average Selling Price")

plt.tight_layout()

plt.savefig("average_price_by_brand.png")

plt.show()
