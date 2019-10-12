import pandas as pd
import datetime

data = pd.read_csv('matilda_files/Basic.txt', header=None)
df = pd.DataFrame(data)
tdelta = datetime.timedelta(days=0)
tday = datetime.date.today()
dates = [0] * data.size
for i in range(data.size, 1, -1):
    date = tday - tdelta
    dates[i - 1] = date
    tdelta = datetime.timedelta(days=1)
    tday = date
df['Dates'] = dates
print(df)
