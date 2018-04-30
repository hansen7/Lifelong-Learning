import numpy as np
import scipy.stats as scst
from statsmodels.stats.libqsturng import qsturng  


def friedman_statistics(arr, n_datasets):
    k = len(arr)
    res = 12 * n_datasets / (k * (k+1)) * (np.sum(arr**2) - k * (k+1)**2 / 4)
    return res

def friedman_statistics_new(arr, n_datasets):
    arr = np.array(arr)
    k = len(arr)
    f_old = friedman_statistics(arr, n_datasets)
    f_new = (n_datasets - 1) * f_old / (n_datasets*(k-1) - f_old)
    return f_new

def friedman(arr, n_datasets):
    f_statistics = friedman_statistics_new(arr, n_datasets)
    k = len(arr)
    dof = (k-1, (k-1)*(n_datasets-1))
    p_value = 1 - scst.f.cdf(f_statistics, *dof)
    return f_statistics, p_value

def nemenyi(k, n, critical=0.05):
    """I cannot find pdf of studentized range distribution. So we must use quantile function.
    
    """
    studentized_range_statistics = qsturng(1-critical, k, 1e5)
    q_alpha = studentized_range_statistics / np.sqrt(2)# 1e5 is close to infinity
    # print r'$q_\alpha$ in Nemenyi test: {}'.format(q_alpha)
    nemenyi_range = np.sqrt(1. * k * (k+1) / (6*n)) * q_alpha
    return nemenyi_range

def nemenyi_plot(point_arr, critical):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_context('poster')
    POINT_STYLE = {}
    LINE_STYLE = {}
    DELIM_LINE_STYLE = {'ls': '--', 'lw': 2, 'alpha': .3}
    COLOR_LIST = ['r', 'b', 'k', 'y', 'orange']
    Blues = plt.get_cmap('Blues')
    Y_START, Y_INTERVAL = 1, 1
    
    n_point = len(point_arr)
    y_arr = np.arange(Y_START, Y_START + n_point * Y_INTERVAL, Y_INTERVAL)
    
    plt.figure(figsize=(14, 6))
    plt.title('Friedman Test Grpah')
    plt.ylabel('Algorithms')
    plt.xlabel('Average Order')
    plot_lim = (y_arr[0] - 2*Y_INTERVAL, y_arr[-1] + 2*Y_INTERVAL)
    plt.ylim(plot_lim)
    for i, x in enumerate(point_arr):
        y = y_arr[i]
        this_color = COLOR_LIST[i]
        plt.plot(x, y, ls='', marker='o', markersize=15, c=this_color, label='Ave. order: {}'.format(x))# plot a point
        line_y = np.ones(2) * y
        range_left, range_right = x - critical/2, x + critical/2
        line_x = np.linspace(range_left, range_right, 2, endpoint=True)
        plt.plot(line_x, line_y, ls='-', c=this_color, lw=3)# range line
        plt.plot(np.ones(2)*range_left, plot_lim, c=this_color, **DELIM_LINE_STYLE)
        plt.plot(np.ones(2)*range_right, plot_lim, c=this_color, **DELIM_LINE_STYLE)
    plt.legend(loc='best')
    plt.show()

def main():
    n_datasets = 5
    average_order_list = [3.2, 3.8, 1.2, 4, 2.8]#[1, 2.125, 2.875]
    n_algorithms = len(average_order_list)
    
    friedman_s, friedman_p = friedman(average_order_list, n_datasets)
    print r'Friedman Test statistics $\tau_F$={}, P value = {}'.format(round(friedman_s, 4), round(friedman_p, 4))
    
    if friedman_p < .05:
        critical_range = nemenyi(n_algorithms, n_datasets)
        import itertools
        result = []
        for pairs in itertools.combinations(average_order_list, 2):
            is_different = abs(pairs[0] - pairs[1]) > critical_range
            result.append((pairs, is_different))
        
        print 'The critical range in Nemenyi Test is: {}'.format(critical_range)
        print 'These are pairs that have different performance:'
        for res in result:
            if res[1]:
                print res[0]
        
        
        nemenyi_plot(average_order_list, critical=critical_range)

if __name__ == '__main__':
    main()