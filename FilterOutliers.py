import pandas as pd

# Load the parquet file
df_pq = pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
print(df_pq[df_pq['outlier'] == True])
print(df_pq.shape)
# Filter out rows where outlier is True
df_pq = df_pq[df_pq['outlier'] == False]
print(df_pq.shape)
df_pq.to_parquet('example-data/2025-01-01.taxi-rides.parquet', index=False)