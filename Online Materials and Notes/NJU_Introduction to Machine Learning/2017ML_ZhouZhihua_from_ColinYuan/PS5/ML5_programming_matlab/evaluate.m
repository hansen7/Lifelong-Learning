load('test_targets.mat');
predictions=csvread('test_predictions.csv');
acc=sum(predictions==test_targets)/size(test_targets,1);
fprintf('%f\n',acc);