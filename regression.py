import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv('table.csv', index_col = 0)
df.head()


x = df
y = df['point_name']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
pred = knn.predict(x_test)


