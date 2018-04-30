% configuration
input_dim=400;
hidden_dim=100;
output_dim=10;
eta=0.8;  % step length
max_t=20;

% data input
X_train=csvread('train_data.csv');
Y_train=csvread('train_targets.csv');
X_test=csvread('test_data.csv');
%Y_test=csvread('test_targets.csv');
num_train=size(X_train,1);
num_test=size(X_test,1);
input_dim=size(X_train,2);

v=(rand(input_dim, hidden_dim)-0.5)/10;
gamma=(rand(hidden_dim, 1)-0.5)/10;
w=(rand(hidden_dim, output_dim)-0.5)/10;
theta=(rand(output_dim, 1)-0.5)/10;

% training
t=0;
while t<max_t
    for i=1:num_train
        alpha=(X_train(i,:)*v)';
        b=1./(1+exp(gamma-alpha));
        beta=w'*b;
        y=1./(1+exp(theta-beta));
        y_real=zeros(10,1);
        y_real(Y_train(i)+1)=1;
        g=y.*(1-y).*(y_real-y);
        e=b.*(1-b).*(w*g);
        w=w+eta.*(b*g');
        theta=theta-eta.*g;
        v=v+eta.*X_train(i,:)'*e';
        gamma=gamma-eta.*e;
    end
    t=t+1;
end

alpha=X_test*v;
b=1./(1+exp(ones(num_test,1)*gamma'-alpha));
beta=b*w;
y=1./(1+exp(ones(num_test,1)*theta'-beta));
[~, y_prediction]=max(y');
y_prediction=y_prediction'-1;
csvwrite(['test_predictions.csv'], y_prediction);