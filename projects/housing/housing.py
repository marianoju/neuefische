import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.tree import _tree
import seaborn as sns
sns.set()

from sklearn.tree import DecisionTreeRegressor


data = pd.read_csv("data/housing.csv")
data.head()


max_depth = 3

dTree = DecisionTreeRegressor(max_depth=max_depth)
dTree.fit(data[['latitude', 'longitude']], data['median_house_value'])
data['predicted_value'] = dTree.predict(data[['latitude', 'longitude']])


fig = plt.figure(figsize=(20,10))
sub1 = plt.subplot(1,2,1)
sub1.set_title('Original')
plt.scatter(x=data['longitude'], y=data['latitude'], c=data['median_house_value'], s=10, cmap='cool');

sub2=plt.subplot(1,2,2)
sub2.set_title('Tree')
plt.scatter(x=data['longitude'], y=data['latitude'], c=data['predicted_value'], s=10, cmap='cool');


def tree_to_rectangles(tree, feature_names, lat, lon):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))

    rectangles = []

    def recurse(node, lat, lon, rectangles):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]

            lon_left = lon.copy()
            lat_left = lat.copy()

            lon_right = lon.copy()
            lat_right = lat.copy()

            if name == "lat":
                lat_left[1] = tree_.threshold[node]
                lat_right[0] = tree_.threshold[node]
                recurse(tree_.children_left[node], lat_left, lon_left, rectangles)
                recurse(tree_.children_right[node], lat_right, lon_right, rectangles)
            else:
                lon_left[1] = tree_.threshold[node]
                lon_right[0] = tree_.threshold[node]
                recurse(tree_.children_left[node], lat_left, lon_left, rectangles)
                recurse(tree_.children_right[node], lat_right, lon_right, rectangles)

        else:
            rectangles.append([lat[0], lat[1], lon[0], lon[1]])

    recurse(0, lat, lon, rectangles)
    return rectangles


lat = np.zeros(2)
lon = np.zeros(2)
lat[0] = data['latitude'].min()
lat[1] = data['latitude'].max()

lon[0] = data['longitude'].min()
lon[1] = data['longitude'].max()

print(lat, lon)
rect = tree_to_rectangles(dTree, ['lat','lon'], lat, lon)


pd_rect = pd.DataFrame(rect, columns=['lat_0','lat_1','lon_0','lon_1'])
pd_rect.head()

coordinates = []
for row in rect:
    for i in [0, 1]:
        for j in [0, 1]:
            coordinates.append([row[i], row[2 + j]])

pd_coord = pd.DataFrame(coordinates)


fig = plt.figure(figsize=(20,10))
sub1 = plt.subplot(1,2,1)
sub1.set_title('Original')
plt.scatter(x=data['longitude'], y=data['latitude'], c=data['median_house_value'], s=10, cmap='cool');

sub2=plt.subplot(1,2,2)
sub2.set_title('Tree')
plt.scatter(x=data['longitude'], y=data['latitude'], c=data['predicted_value'], s=10, cmap='cool');
plt.scatter(x=pd_coord[1], y=pd_coord[0], marker='+', c='green', s=100);


def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print ("def tree({}):".format(", ".join(feature_names)))

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print ("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print ("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print ("{}return {}".format(indent, tree_.value[node]))

    recurse(0, 1)


tree_to_code(dTree,['lat','lon'])

clf = tree.DecisionTreeClassifier(max_depth=max_depth)
clf_ = clf.fit(data[['latitude', 'longitude']], data['median_house_value'])
data['predicted_value'] = clf.predict(data[['latitude', 'longitude']])

tree.export_graphviz(clf, out_file='tree.dot')