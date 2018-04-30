import numpy as np
from sklearn.svm import SVC

X=np.genfromtxt('train_data.csv',delimiter=',')
y=np.genfromtxt('train_targets.csv')
Xt=np.genfromtxt('test_data.csv',delimiter=',')
yt=np.genfromtxt('test_targets.csv')

passed=0
gamma_list=[0.1,1,10]
for gamma in gamma_list:
    model=SVC(kernel="rbf", C=1, gamma=gamma) 
    model.fit(X,y)
    
    y_pred_true=model.predict(Xt)
    model.predict=None
    model.decision_function=None

    ##################################################################
    # you should implement the "predict" function in your main.py code
    # we will import and use it as following:
    from main import predict
    y_pred=predict(Xt,model)
    ##################################################################

    passed+=sum(y_pred==y_pred_true)/y_pred_true.shape[0]

if passed==len(gamma_list):
    print('passed')
else:
    print('failed')



