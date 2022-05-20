import pandas as pd

from pandas_profiling import ProfileReport

heart = pd.read_csv('../data/raw/heart.csv', index_col=0)

profile = ProfileReport(heart, title='Heart report', explorative=True)
profile.to_file('../reports/heart_report.html')
