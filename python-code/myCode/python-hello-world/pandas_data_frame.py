import pandas as pd
import time
import matplotlib.pyplot as plt
# Accessing a very large (1.5 million rows) .CSV file to illustrate time consumption.


def perf_eval_map(dframe, cycles):
    print("map")
    init = time.perf_counter_ns()
    for i in range(0, n):
        dframe['vehicle_category'] = dframe['vehicle_type'].map(
            lambda x: 'High-Speed' if x == 'AVE' or x == 'AVE-TGV' else 'Standard')
    print(f"Creating column with map: {time.perf_counter_ns() - init}")# 120.397.314.800

def perf_eval_apply(dframe, cycles):
    print("apply")
    init = time.perf_counter_ns()
    for i in range(0, cycles):
        dframe['vehicle_category'] = dframe['vehicle_type'].apply(
            lambda x: 'High-Speed' if x == 'AVE' or x == 'AVE-TGV' else 'Standard')
    print(f"Creating column with apply: {time.perf_counter_ns() - init}") #116.919.231.000

def perf_eval_case_when(dframe, cycles):
    print("case_when")
    init = time.perf_counter_ns()
    for i in range(0, cycles):
        dframe['High_speed'] = 'High-Speed'
        dframe['High_speed'] = dframe['High_speed'].case_when(
            [
                ((dframe['vehicle_type']!='AVE') & (dframe['vehicle_type'] != 'AVE-TGV'),'Standard')
            ]
        )
    print(f"Creating column with default value + case_when: {time.perf_counter_ns()-init}") #121.846.130.000

def perf_eval_fillna(dframe, cycles):
    print(".loc + fillna()")
    init = time.perf_counter_ns()
    for i in range(0, cycles):
        dframe.loc[((dframe['vehicle_type'] != 'AVE') & (dframe['vehicle_type'] != 'AVE-TGV')), 'High_speed2'] = 'Standard'
        dframe['High_speed2']=dframe['High_speed2'].fillna('High-Speed')
    print(f"Creating column with .loc + fillna(): {time.perf_counter_ns()-init}") #172.918.244.100

def index_perf_shape(dframe, cycles):
    init = time.perf_counter_ns()
    for i in range(0, n):
        df.shape[0]
    print(f"df.shape[0]:   {time.perf_counter_ns()-init} ns")

def index_perf_len(dframe, cycles):
    init = time.perf_counter_ns()
    for i in range(0,n):
        len(df)
    print(f"len(df):       {time.perf_counter_ns()-init} ns")

def index_perf_index(dframe, cycles):
    init = time.perf_counter_ns()
    for i in range(0, n):
        len(df.index)
    print(f"df.index:      {time.perf_counter_ns()-init} ns")

def index_perf_indexsize(dframe,cycles):
    init = time.perf_counter_ns()
    for i in range(0, n):
        df.index.size
    print(f"df.index.size: {time.perf_counter_ns()-init} ns")

import datetime

df = pd.read_csv("C:/D/GitRepos/StatisticsBAandDS/statistics/python/railways/train_ticket_data.csv")
print(df.info())
print("counting the number of rows")

n = 100

new_date = datetime.datetime.strptime("2019-05-18 21:30:00", '%Y-%m-%d %H:%M:%S')
print(new_date.date())
print(new_date.time())
print(new_date.weekday()) #Sunday = 6

increment = new_date + datetime.timedelta(hours=1.98)
print(f"date with increment: {increment}")

print(df.index)

print("Performance of dataframe indexing, size calculation")
#index_perf_shape(df,n)
#index_perf_len(df,n)
#index_perf_indexsize(df,n)
index_perf_index(df,n)  # 11.100

print("\nPerformance of column creation methods")
#perf_eval_map(df,n)
#perf_eval_case_when(df,n)
#perf_eval_fillna(df,n)
perf_eval_apply(df,n) # 12.438.156.500


## Easy example of plot()
#exercise = pd.read_csv("C:/D/GitRepos/StatisticsBAandDS/statistics/python/nba_statistics/Exercise.csv")
#exercise.plot()
#plt.show()

print("get data")
duration_vs_time = df.loc[:,['departure','duration']]
print("Plot")
# kind={'scatter', 'pie','area','box','hist','bar','barh','line','density'}
# marker={'o'}
# linestyle={'-','--'}
#secondary_y={True,False)
#duration_vs_time.plot(kind='scatter', x='departure', y='duration')
duration_hist = df.loc[:,['duration']]
print(duration_hist.describe())
duration_hist.plot(kind='hist')
print("show plot")
plt.show()
