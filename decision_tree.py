# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original training features to numbers and add to the 4D array X. Forinstance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2,2, 2], ...]]
# --> add the Python code here
# X =
for row in db:
    rowData = []
    for i, value in enumerate(row):
        if i == 0:
            if value == 'Young':
                rowData.append(1)
            if value == 'Prepresbyopic':
                rowData.append(2)
            if value == 'Presbyopic':
                rowData.append(3)
        elif i == 1:
            if value == 'Myope':
                rowData.append(1)
            else:
                rowData.append(2)
        elif i == 2:
            if value == 'No':
                rowData.append(1)
            else:
                rowData.append(2)
        elif i == 3:
            if value == 'Reduced':
                rowData.append(1)
            else:
                rowData.append(2)
    X.append(rowData)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> addd the Python code here
# Y =
for row in db:
    if row[-1] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)

# fiiting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=[
               'Yes', 'No'], filled=True, rounded=True)
plt.show()
