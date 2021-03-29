import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    #Importing dataset
    diamonds = pd.read_csv('diamonds.csv')

    #Feature and target matrices
    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]
    y = diamonds[['price']]

    #Training and testing split, with 25% of the data reserved as the test set
    X = X.to_numpy()
    y = y.to_numpy()
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    #Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    #print(len(X_train))
    X_test = normalize_test(X_test, trn_mean, trn_std)
    #print(len(X_test))
    #print(len(y_train))
    #Define the range of lambda to test
    lmbda = np.logspace(0, 3,endpoint = True) #fill in
    #lmbda = [1,100]
    #print(lmbda.shape)
    #for i in np.arange(-2, 2.01,0.01):
        #lmbda.append(10*10**(i)) #fill in#fill in
    #print(len(y_train)
    MODEL = []
    MSE = []
    for l in lmbda:
        #Train the regression model using a regularization parameter of l
        model = train_model(X_train,y_train,l)
        #print(model)
        #Evaluate the MSE on the test set
        mse = error(X_test,y_test,model)
        #print(mse)
        #Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    #Plot the MSE as a function of lmbda
    plt.plot(lmbda, MSE) #fill in
    plt.xlabel('Lambda')
    plt.ylabel('MSE')
    plt.title('MSE as a function of Lambda')
    plt.show()

    #Find best value of lmbda in terms of MSE
    ind = MSE.index(min(MSE))#fill in
    #ind = MSE.index(MSE[0])
    #print(ind)
    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]

    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))

    return model_best


#Function that normalizes features in training set to zero mean and unit variance.
#Input: training data X_train
#Output: the normalized version of the feature matrix: X, the mean of each column in
#training set: trn_mean, the std dev of each column in training set: trn_std.
def normalize_train(X_train):

    #fill in
    X = []
    mean = []
    std = []
    #count = 0
    for i in range(X_train.shape[1]):
        k = X_train[:,i]
        col = k
        mean1 = col.mean()
        std1 = np.std(col)
        mean.append(col.mean())
        std.append(np.std(col))
        x1 = []
        for j in col:
            new = (j - mean1) / std1
            x1.append(new)  
        X.append(x1)
        #count = count + 1
    #fill in

    #mean = X_train[0].mean()
    #std = np.std(X_train[0])
    return np.array(X).T, mean, std


#Function that normalizes testing set according to mean and std of training set
#Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each
#column in training set: trn_std
#Output: X, the normalized version of the feature matrix, X_test.
def normalize_test(X_test, trn_mean, trn_std):

    #fill in
    X = []
    x1 = []
    for i in range(X_test.shape[1]):
        k = X_test[:,i]
        col = k
        mean = trn_mean[i]
        std = trn_std[i]
        x1 = []
        for j in col:
            new = (j - mean) / std
            x1.append(new)  
        X.append(x1)


    return np.array(X).T



#Function that trains a ridge regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model.
def train_model(X,y,l):

    #model =  linear_model.Ridge(alpha= l, fit_intercept=True)
    #model = linear_model.LinearRegression(fit_intercept = True)
    model = linear_model.Ridge(alpha = l, fit_intercept = True)
    model.fit(X, y)
    #fill in

    return model


#Function that calculates the mean squared error of the model on the input dataset.
#Input: Feature matrix X, target variable vector y, numpy model object
#Output: mse, the mean squared error
def error(X,y,model):

    y_pred_test = model.predict(X)
    y_pred = (model * np.std(y)) + np.mean(y)
    #mse = float(sum((y-y_pred_test)**2))/len(y)
    #mse = mean_squared_error(y, y_pred_test)
    #Fill in
    return(mse)

if __name__ == '__main__':
    model_best = main()
    #We use the following functions to obtain the model parameters instead of model_best.get_params()
    print(model_best.coef_)
    print(model_best.intercept_)

    price_para = [0.25,60,55,4,3,2,5,3,3]
    price = sum(sum(price_para * model_best.coef_) + model_best.intercept_)

    print("Using the coef and intercept founded, the intacipated price is:",price)
