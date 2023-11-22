from ydata_profiling import ProfileReport
import pandas as pd

df =pd.read_csv("diabetes.csv")

pf =ProfileReport(df, title="EDA report", explorative=True)

pf.to_file("EDA report.html")