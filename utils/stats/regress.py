import numpy as np

def regress(ty,tX, include_constant=True):
    """
    Perform a multiple linear regression of y onto X.  X is a num
    observations by (num variables +1) array.  X should contain a
    column of ones to generate the intercept.  y is a num observations
    array of independent variables

    return value B, residuals, stats

    B: the regression coeffients;  Ypred = B.T * X.T
    residuals: array( y - Ypred.T)
    stats = Rsquared, F, p
    
    """

    # regression coeffs are given by (Xt*X)-1*Xt*y
    X = np.array(tX)
    y = np.array(ty)
    
    N = X.shape[0]
    y.shape = N, 1
    
    X = np.matrix(X)
    Y = np.matrix(y)
    Xt = X.T
    
    Xt_X = Xt*X
    try: 
        Xt_X_i = np.matrix(np.linalg.inv(Xt_X) )
    except Exception, e:
        Xt_X_i = np.empty_like(Xt_X)
        Xt_X_i.fill(np.NaN)
    
    B = Xt_X_i*Xt*Y

    Ypred = B.T * Xt
    residuals = np.array(Y-Ypred.T)
    CF = N*np.mean(y)**2     # correction factor

    SStotal = float(Y.T*Y-CF)
    SSregress =  float(B.T * Xt * Y - CF)
    SSerror =  SStotal - SSregress
    try:
        Rsquared = SSregress/SStotal
    except Exception, e:
        Rsquared = np.NaN

    dfTotal = N-1
    dfRegress = len(B)-1
    dfError = dfTotal - dfRegress

    F = SSregress/dfRegress / (SSerror/dfError)
    #prob = 1-fcdf(F, dfRegress, dfError)

    stats = Rsquared, F#, prob
    return B, residuals, stats
