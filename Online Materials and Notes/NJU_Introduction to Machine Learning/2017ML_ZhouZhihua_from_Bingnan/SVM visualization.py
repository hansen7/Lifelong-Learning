# source: http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
# edited for ML4_programming by Yuri Wu, 2017-04-23
# for SVM visualization
"""
Lines that are wrapped by #---- are edited by Bingnan Liu.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# import some data to play with
X=np.genfromtxt('demo_data.csv',delimiter=',')
y=np.genfromtxt('demo_targets.csv')

#----
if X.shape[1] > 2:
    X=X[:, :2]
#----

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
demo_list=[svm.SVC(kernel='linear', C=1).fit(X, y),
           svm.SVC(kernel='poly', degree=3, C=1).fit(X, y),
           svm.SVC(kernel='rbf', gamma=10, C=1).fit(X, y),
           svm.SVC(kernel='rbf', gamma=10, C=10).fit(X, y),
           svm.SVC(kernel='rbf', gamma=100, C=1).fit(X, y),
           svm.SVC(kernel='rbf', gamma=100, C=10).fit(X, y)]

# title for the plots
titles = ['linear kernel',
          'polynomial (degree 3) kernel',
          'RBF kernel, gamma=10, C=1',
          'RBF kernel, gamma=10, C=10',
          'RBF kernel, gamma=100, C=1',
          'RBF kernel, gamma=100, C=10']

# create a mesh to plot in
#----
x_min, x_max = np.min(X[:, 0]), np.max(X[:, 0])
x_min -= (x_max - x_min) * .1
x_max += (x_max - x_min) * .1
y_min, y_max = np.min(X[:, 1]), np.max(X[:, 1])
h = (x_max - x_min) / 1e3  # step size in the mesh
#----
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

plt.figure(figsize=(16, 12), dpi=120)
for i, clf in enumerate(demo_list):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    plt.subplot(len(demo_list) // 2 + 1, 2, i + 1)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # set cmap
    CMAP = plt.cm.coolwarm
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=CMAP, alpha=0.5)

    #-----
    n_support = np.sum(clf.n_support_)
    support_index = clf.support_
    is_support = np.zeros(X.shape[0]).astype(bool)
    is_support[support_index] = True
    not_support = np.logical_not(is_support)
    
    support_style = {"marker": 'D', "s": 38, "alpha": 0.8, "edgecolors": 'white'}
    unsupport_style = {"marker": 'D', "s": 30, "alpha": 0.6, "edgecolors": None}
    #-----
    # Plot also the training points
    plt.scatter(X[is_support, 0], X[is_support, 1], 
                c=y[is_support], cmap=CMAP, **support_style)
    plt.scatter(X[not_support, 0], X[not_support, 1], 
                c=y[not_support], cmap=CMAP, **unsupport_style)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i] 
              + "    |    {}% points are S.V.".format(round(n_support * 100. / X.shape[0], 2)))
    print(n_support)

#----
plt.suptitle("Points with a larger size, deeper color and a white edge are S.V.")
plt.savefig('SVM_visualization.png', format='png')
#----
plt.show()
