import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# import some data to play with
data=np.genfromtxt('illustrate_data.csv',delimiter=',')
y=data[16:,2]
X=data[16:,0:2]

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM re2ularization parameter
demo_list=[svm.SVC(kernel='linear', C=10).fit(X, y),
           svm.SVC(kernel='poly', degree=3, C=10).fit(X, y),
           svm.SVC(kernel='rbf', gamma=10, C=1).fit(X, y),
           svm.SVC(kernel='rbf', gamma=10, C=10).fit(X, y),
           svm.SVC(kernel='rbf', gamma=100, C=1).fit(X, y),
           svm.SVC(kernel='rbf', gamma=100, C=10).fit(X, y)]

# title for the plots
titles = ['linear, C=10',
          'poly(degree 3), C=10',
          'RBF, gamma=10, C=1',
          'RBF, gamma=10, C=10',
          'RBF, gamma=100, C=1',
          'RBF, gamma=100, C=10']

# create a mesh to plot in
h = .005  # step size in the mesh
x_min, x_max = 0,1
y_min, y_max = 0,1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))


for i, clf in enumerate(demo_list):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    plt.subplot(3, 2, i + 1)
    plt.subplots_adjust(wspace=0.5, hspace=0.4)

    p=np.c_[xx.ravel(), yy.ravel()];
    Z = clf.predict(p);

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    if i==0:
      print(Z)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm,alpha=0.5)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y,cmap=plt.cm.coolwarm)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], marker='.', color='w');
    #plt.legend();
    print(len(clf.support_))

plt.show()