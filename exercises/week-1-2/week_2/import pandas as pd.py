import pandas as pd

# Download dataset
url ="https://raw.githubusercontent.com/pjournal/boun01g-data-mine-r-s/gh-pages/Assignment/AB_NYC_2019.csv"
df = pd.read_csv(url)

print("Data loaded successfully!")
print("Shape:", df.shape)
df.head()
