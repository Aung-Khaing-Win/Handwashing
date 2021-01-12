from scipy.stats import t
import numpy as np
import math

def unbiased_estimator(dataframe):
        df = dataframe.copy()
        xbar = df.mean()
        n = df.shape[0]

        df['squared_difference'] = (df - xbar) ** 2
        return df['squared_difference'].sum() / (n-1)

def dof(sample_1, sample_2):
    var_estimator_1 = unbiased_estimator(sample_1)
    var_estimator_2 = unbiased_estimator(sample_2)
    n1 = sample_1.shape[0]
    n2 = sample_2.shape[0]
    
    numerator = ((var_estimator_1/n1) + (var_estimator_2/n2))**2
    denominator = ((var_estimator_1/n1)**2 /(n1-1)) + ((var_estimator_2/n2)**2 /(n2-1))
    dof = numerator/denominator
    
    return dof
    
    
def welch_ttest(sample_1, sample_2, alpha=0.05, two_tail=True):
    # Numerator
    x1_bar = sample_1.mean()
    x2_bar = sample_2.mean()
    
    numerator = x1_bar-x2_bar
    # Denominator
    n1 = sample_1.shape[0]
    n2 = sample_2.shape[0]
    
    var_estimator_1 = unbiased_estimator(sample_1)
    var_estimator_2 = unbiased_estimator(sample_2)
    denominator = np.sqrt((var_estimator_1/n1)+(var_estimator_2/n2))
    # t-stat
    t_statistics = numerator / denominator
    df = dof(sample_1, sample_2)
    p = 1-t.cdf(t_statistics, df)
    if two_tail:
        p = 2 * p
    
    if p < alpha:
        print('Null hypothesis can be rejected.')
    else:
        print('Fail to reject null hypothesis.')

    return t_statistics, p, df
