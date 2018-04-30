data=csvread('data.csv');
targets=csvread('targets.csv');
num_sample=size(data,1);
dim=size(data,2);

indices=crossvalind('Kfold', num_sample, 10);

for f=1:10
    % prepare fold
    train_x=zeros(num_sample, dim);
    val_x=zeros(num_sample, dim);
    train_y=zeros(num_sample, 1);
    %val_y=zeros(num_sample,1);
    val_idx=zeros(num_sample,1);
    num_train=0;
    num_val=0;
    for i=1:num_sample
        if indices(i)==f
            num_val=num_val+1;
            val_x(num_val,:)=data(i,:);
            %val_y(num_val)=targets(i);
            val_idx(num_val)=i;
        else
            num_train=num_train+1;
            train_x(num_train,:)=data(i,:);
            train_y(num_train)=targets(i);
        end
    end
    train_x=train_x(1:num_train,:);
    val_x=val_x(1:num_val,:);
    train_y=train_y(1:num_train,:);
    %val_y=val_y(1:num_val,:);
    val_idx=val_idx(1:num_val,:);
    
    % normalization
    %train_mu=mean(train_x,1);
    %train_std=std(train_x,1);
    %train_x=(train_x-ones(num_train, 1)*train_mu)./(ones(num_train, 1)*train_std);
    %val_x=(val_x-ones(num_val, 1)*train_mu)./(ones(num_val, 1)*train_std);
    
    train_x=[train_x, ones(num_train, 1)];
    val_x=[val_x, ones(num_val, 1)];
    
    % Newton's method
    beta=zeros(dim+1,1);
    for t=1:5
        p0=1./(1+exp(train_x*beta));
        p1=1-p0;
        dbeta=train_x'*(p1-train_y);
        d2beta=train_x'*diag(p0.*p1)*train_x;
        % prevent matrix singularity
        if cond(d2beta,2)>1e15
            break;
        end
        beta=beta-inv(d2beta)*dbeta;
    end
    pred=(1./(1+exp(-val_x*beta))>0.5);
    csvwrite(['fold',num2str(f),'.csv'], [val_idx, pred]);
end
