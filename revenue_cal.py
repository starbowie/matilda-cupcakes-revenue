import pandas as pd
import datetime
import matplotlib.pyplot as plt


# basic_uri = 'matilda_files/Basic.txt'
# delux_uri = 'matilda_files/Delux.txt'
# total_uri = 'matilda_files/Total.txt'

def revenue_graphs(uri):
    data = pd.read_csv(uri)
    df = pd.DataFrame(data)
    tdelta = datetime.timedelta(days=int(data.size - 1))
    tday = datetime.date.today()
    start = tday - tdelta
    ph = 'Total:'
    if "Basic" in uri:
        ph = 'Basic Cupcake:'
    elif "Delux" in uri:
        ph = 'Delux Cupcakes:'
    df['Dates'] = pd.Series(pd.date_range(start, freq='D', periods=data.size))
    df_yearly = pd.DataFrame(df.groupby([pd.Grouper(key='Dates', freq='Y')])[ph].sum().reset_index())
    df_monthly = pd.DataFrame(df.groupby([pd.Grouper(key='Dates', freq='M')])[ph].sum().reset_index())
    df_weekly = pd.DataFrame(df.groupby([pd.Grouper(key='Dates', freq='W')])[ph].sum().reset_index())
    df_yearly.plot.bar(x='Dates', y=ph)
    df_monthly.plot.bar(x='Dates', y=ph)
    df_weekly.plot.bar(x='Dates', y=ph)
