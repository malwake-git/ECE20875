import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities



    :param hist: list
    :return: list
    """


    j = 0;
    hist_sum = 0;

    hist_new = [];

    while j < len(hist):
        hist_sum =  hist_sum + hist[j];
        j += 1;

    for i in hist:
        p = i / hist_sum
        hist_new.append(p);

    return(hist_new)
    
    pass


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width



    :param histo: list 
    :param width: float
    :return: float
    """
    

    sq_sum = 0;
    m = 0;
    k = 0;

    hist_p = norm_histogram(histo)
    
    hist_sq =[0] * len(hist_p)
    
    while k < len(hist_p):
        hist_sq[k] = hist_p[k] ** 2;
        sq_sum += (hist_sq[k]);
        m += histo[k];
        k += 1;


    j = 2/((m - 1) * width) - (((m + 1)/((m-1)*width))*(sq_sum))
    return(j);
    pass


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    optimal_hist = []

    b = min_bins

    while b <= max_bins:
        j = compute_j(plt.hist(data, b, (minimum,maximum))[0], (maximum-minimum)/b);
        
        optimal_hist.append(j)
        
        b += 1;


    return(optimal_hist)

    pass


def find_min(l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """

    list_min = min(l);
    
    min_index = l.index(list_min);

    min_tuple = (list_min,min_index);
    

    return(min_tuple)
    
    pass


if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
