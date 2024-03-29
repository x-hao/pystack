import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df_train = pd.read_csv('train.csv')
    df_train['SalePrice'].describe()
    sns.distplot(df_train['SalePrice'])
    # skewness and kurtosis
    print("Skewness: %f" % df_train['SalePrice'].skew())
    print("Kurtosis: %f" % df_train['SalePrice'].kurt())

    for column in df_train.columns:
        if df_train[column].dtype not in ('int64', 'float64'):
            continue
        data = pd.concat([df_train['SalePrice'], df_train[column]], axis=1)
        data.plot.scatter(x=column, y='SalePrice', ylim=(0, 800000))
        plt.show()

