import numpy as np
import pandas as pd

# Generate random data for house sales
np.random.seed(42)  # For reproducibility with the given seed
n = 1000 # Number of house sales

# Generate features
# 1. House size (in sq ft), normal distribution (mean ~1200, std ~300 for Hyderabad)
house_size = np.round(np.random.normal(1200, 300, n), 0)
house_size = np.clip(house_size, 400, 3000)  # Clamp to realistic range

# 2. Number of bedrooms, random choice among [1, 2, 3]
bedrooms = np.random.choice([1, 2, 3], n, [0.2, 0.5, 0.3])

# 3. Distance to city center (in km), lognormal distribution (mean ~7km, std ~5km)
distance = np.round(np.random.lognormal(1.8, 0.5, n), 1)
distance = np.clip(distance, 1, 30)  # Clamp to realistic range

# 4. Price (in lakhs), normal distribution, correlated with other features
# Base price per sq ft decreases with distance, increases with bedrooms
base_price_per_sqft = 5_000 - (distance * 100) + (bedrooms * 200)
price = house_size * base_price_per_sqft / 100_000  # Convert to lakhs
price = price + np.random.normal(0, 5, n)  # Add some noise
price = np.round(price, 2)
price = np.clip(price, 20, 300)  # Clamp to realistic range

# Create DataFrame
df = pd.DataFrame({
    'Size_sqft': house_size,
    'Bedrooms': bedrooms,
    'Distance_km': distance,
    'Price_lakhs': price
})

# Save to CSV
df.to_csv("house_sales.csv", index=False)
print(df.head())