import pandas as pd
import time
# Accessing a very large (1.5 million rows) .CSV file to illustrate time consumption.

df = pd.read_csv("C:/D/GitRepos/StatisticsBAandDS/statistics/python/railways/train_ticket_data.csv")
print(df.info())
print("counting the number of rows")

n = 100000

inicio = time.perf_counter_ns()
for i in range(0, n):
    df.shape[0]
print(f"df.shape[0]:   {time.perf_counter_ns()-inicio} ns")

inicio = time.perf_counter_ns()
for i in range(0,n):
    len(df)
print(f"len(df):       {time.perf_counter_ns()-inicio} ns")

inicio = time.perf_counter_ns()
for i in range(0, n):
    len(df.index)
print(f"df.index:      {time.perf_counter_ns()-inicio} ns")

inicio = time.perf_counter_ns()
for i in range(0, n):
    df.index.size
print(f"df.index.size: {time.perf_counter_ns()-inicio} ns")
