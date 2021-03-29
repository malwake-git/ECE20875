import numpy as np
import matplotlib.pyplot as plt

# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    
    
    file_path = open( datapath,  "r")
    X = []
    Y = []
    #X = []
    #Y = []
    y_1 = []
    y_2 = []
    y_3 = []
    y_4 = []
    #count = 0
    y_5 = []
    file_data_path = file_path.readlines()
    
    for i in file_data_path:
        i = i.split(" ")
        l1 = float(i[0])
        l2 = float(i[1])
        X.append(l1)
        Y.append(l2)
        
        
    for j in degrees:
        mitrx = feature_matrix(X, j)
        ##matrix
        paramFits.append(least_squares(mitrx, Y))
        
    xsort = sorted(X)
    
    for l in sorted(X):
        res1 = paramFits[0][0] * l + paramFits[0][1]
        res2 = paramFits[1][0] * (l ** 2) + paramFits[1][1] * l + paramFits[1][2]
        res3 = paramFits[2][0] * (l ** 3) + paramFits[2][1] * (l ** 2) + paramFits[2][2] * l + paramFits[2][3]
        res4 = paramFits[3][0] * (l ** 4) + paramFits[3][1] * (l ** 3) + paramFits[3][2] * (l ** 2) + paramFits[3][3] * l + paramFits[3][4]
        res5 = paramFits[4][0] * (l ** 5) + paramFits[4][1] * (l ** 4) + paramFits[4][2] * (l ** 3) + paramFits[4][3] * (l ** 2) + paramFits[4][4] * l + paramFits[4][5]
        y_1.append(res1)
        y_2.append(res2)
        y_3.append(res3)
        y_4.append(res4)
        y_5.append(res5)
        
    #close    
    file_path.close()
    
    plt.scatter(X, Y, color='b', marker='*')
    
    plt.plot(sorted(X), y_1, color='g', linestyle='-.')
    plt.plot(sorted(X), y_2, color='b', linestyle='-.')
    plt.plot(sorted(X), y_3, color='m', linestyle='-.')
    plt.plot(sorted(X), y_4, color='y', linestyle='-.')
    plt.plot(sorted(X), y_5, color='r', linestyle='-.')
    
    plt.legend(["data = 1", "data = 2", "data = 3", "data = 4", "data = 5", "Path Data"], loc='upper right')
    plt.ylabel("Y Data")
    plt.xlabel("X Data")
 
    plt.show()
    ##
    return paramFits

# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X_list = []
    ind = 0
    for i in x:
        d1 = d
        
        X_list.append([])
        
        while d1 >= 0:
            X_list[ind].append(i**d1)
            d1 -= 1
        # d = 1    
        ind += 1
    return X_list


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X_array = np.array(X)
    # X_array = list(X)
    Y_array = np.array(y)

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    
    return (np.linalg.inv(X_array.T @ X_array)) @ (X_array.T @ Y_array)


if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [1, 2, 3, 4, 5]
    paramFits = main(datapath, degrees)
    print(paramFits)
