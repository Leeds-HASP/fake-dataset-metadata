
import random

import numpy as np
import pandas as pd

random.seed(42)
rng = np.random.default_rng(42)

N = 10

# four sorted speeds per row so p25 <= p50 <= p75 <= p85
speeds = np.sort(rng.uniform(20, 55, size=(N, 4)), axis=1).round(2)

df = pd.DataFrame({
    "link_toid": ["osgb4000000003" + f"{rng.integers(0, 1_000_000):06d}" for _ in range(N)],
    "hour": rng.integers(0, 24, N),
    "count": rng.integers(10, 21, N),
    "n_trips": rng.integers(1, 6, N),
    "p25_speed_mph": speeds[:, 0],
    "p50_speed_mph": speeds[:, 1],
    "p75_speed_mph": speeds[:, 2],
    "p85_speed_mph": speeds[:, 3],
})

# mean sits between p25 and p75
df["mean_speed_mph"] = rng.uniform(df["p25_speed_mph"], df["p75_speed_mph"]).round(2)

df = df[[
    "link_toid", "hour", "count", "n_trips", "mean_speed_mph",
    "p25_speed_mph", "p50_speed_mph", "p75_speed_mph", "p85_speed_mph",
]]

df.to_csv("./2024/hourly/vehicletype_hourly.csv", index=False)

# drop the hour
df = df.drop(columns="hour")
df.to_csv("./2024/allday/vehicletype_allday.csv", index=False)