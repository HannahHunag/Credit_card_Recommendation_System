import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import cluster
from sklearn.cluster import KMeans
# import VisualizeHelper.VisualizeCluster as VisualizeCluster

# read-in the excel spreadsheet using pandas 
df = pd.read_csv(r'kmeans_data_4_5.csv')
# print(df.head())

#create model
model = KMeans(n_clusters = 4).fit(df)
df['Cluster'] = model.labels_

pd.DataFrame(df).to_csv(r"kmeans_4c_5.csv", index=0, encoding = 'utf-8-sig')

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
def PlotElbow(df):
    sse = []
    krange = list(range(2,11))
    X = df[['外送平台','影音娛樂','網路購物','行動支付','超商']].values
    for n in krange:
        model = cluster.KMeans(n_clusters=n, random_state=3)
        model.fit_predict(X)
        cluster_assignments = model.labels_
        centers = model.cluster_centers_
        sse.append(np.sum((X - centers[cluster_assignments]) ** 2))
        #sse.append(model.inertia_)

    plt.plot(krange, sse)
    plt.xlabel("$K$")
    plt.ylabel("Sum of Squares")
    plt.savefig('elbow.png')
    plt.show()

PlotElbow(df)
