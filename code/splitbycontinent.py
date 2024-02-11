import pandas as pd
df = pd.read_csv("export.csv")
continent_dfs = {}
for continent in df["continent"].unique():
 
    temp_df = df[df["continent"] == continent]

    continent_dfs[continent] = temp_df

for continent, df in continent_dfs.items():
    df.to_csv(f"{continent}.csv", index=False)