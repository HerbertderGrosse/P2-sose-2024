import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from kafe2 import HistContainer, HistFit, XYContainer, Fit, Plot
from scipy import special



########################################################################################################################################
# TABLE OF CONTENTS #
#####################
#
# - Gaussian model function for photopeaks
# - Model function for compton edges using the complementary error function 'erfc' (Convolution of Gaussian and Heaviside-Step-Function)
# - Model function for the energy dependence of the detector resolution
# - Custom wrapper for fitting a custom function to a histogram using Kafe2, combining all relevant steps
# - Custom wrapper for fitting a custom function to an XY dataset using Kafe2, combining all relevant steps
# - Fit a photopeak using a Gaussian model function
# - Fit a compton edge using a complementary error function
# - Determine the resolution and it's energy dependence of the detector
#
########################################################################################################################################



##########################################
# Gaussian model function for photopeaks #
##########################################

def gaussian (x, mu, sigma = 1, A = 1, baseline = 0):
    return A * np.exp(-(x - mu)**2 / (2 * (sigma**2))) + baseline



########################################################################################################################################
# Model function for compton edges using the complementary error function 'erfc' (Convolution of Gaussian and Heaviside-Step-Function) #
########################################################################################################################################

def compton_edge (x, mu, sigma = 1, A = 1, B = 0, baseline = 0):
    return A * (x-B) * special.erfc((x-mu)/(np.sqrt(2) * sigma)) + baseline



#######################################################################
# Model function for the energy dependence of the detector resolution #
#######################################################################

def inv_sqrt_model (x, A=1, B = 0, C = 0):
    return A/np.sqrt(x) + B/x + C



#########################################################################################################
# Custom wrapper for fitting a custom function to a histogram using Kafe2, combining all relevant steps #
#########################################################################################################

def hist_fit_data (x, y, label = 'data', model = None, constraints = [], fixedparams = [], limitedparams = [], parameternames = None, modellabel = None, modelname = None, modelexpression = None, report = False, **initialvalues):
    # Organise data histogram container
    step = x[1]-x[0]
    data = HistContainer(bin_edges = np.arange(x[0]-0.5*step, x[-1]+step, step = step))
    data.set_bins(y)
    data.label = label  
    # Assign data and model to fit
    fit = HistFit(data, model_function = model, density = False)  
    # Assign parameter constraints and set as initial values
    for a in constraints:
        fit.add_parameter_constraint(name = a[0], value = a[1], uncertainty = a[2])
        fit.set_parameter_values(**{a[0]:a[1]})  
    # Assign fixed parameter values (Causes errors concerning non-positive uncertainties)
    for b in fixedparams:
        fit.fix_parameter(name = b[0], value = b[1])   
    # Assign additional initial values
    fit.set_parameter_values(**initialvalues)
    # Limit parameters to be either zero or positive, not negative
    for a in limitedparams:
        fit.limit_parameter(a, lower = 0)
    #Assign parameter names as well as model label, name and expression
    if parameternames != None:
        fit.assign_parameter_latex_names(**parameternames)
    if modellabel != None:
        fit.model_label = modellabel
    if modelname != None:
        fit.assign_model_function_latex_name(modelname)
    if modelexpression != None:
        fit.assign_model_function_latex_expression(modelexpression)
    # Perform fit
    fit.do_fit() 
    # Report fit results if desired
    if report:
        fit.report()
    # Return fit
    return fit



###########################################################################################################
# Custom wrapper for fitting a custom function to an XY dataset using Kafe2, combining all relevant steps #
###########################################################################################################

def fit_data (x, y, xerr = None, yerr = None, label = 'data', model = None, constraints = [], fixedparams = [], limitedparams = [], parameternames = None, modellabel = None, modelname = None, modelexpression = None, report = False, **initialvalues):
    # Organise data and errors in XYContainer
    data = XYContainer(x_data = x, y_data = y)
    data.label = label
    if xerr != None:
        data.add_error(axis='x', err_val = xerr)
    if yerr != None:
        data.add_error(axis='y', err_val = yerr)   
    # Assign data and model to fit
    fit = Fit(data, model_function = model)  
    # Assign parameter constraints and set as initial values
    for a in constraints:
        fit.add_parameter_constraint(name = a[0], value = a[1], uncertainty = a[2])
        fit.set_parameter_values(**{a[0]:a[1]})  
    # Assign fixed parameter values (Causes errors concerning non-positive uncertainties)
    for b in fixedparams:
        fit.fix_parameter(name = b[0], value = b[1])   
    # Assign additional initial values
    fit.set_parameter_values(**initialvalues)
    # Limit parameters to be either zero or positive, not negative
    for a in limitedparams:
        fit.limit_parameter(a, lower = 0)
    #Assign parameter names as well as model label, name and expression
    if parameternames != None:
        fit.assign_parameter_latex_names(**parameternames)
    if modellabel != None:
        fit.model_label = modellabel
    if modelname != None:
        fit.assign_model_function_latex_name(modelname)
    if modelexpression != None:
        fit.assign_model_function_latex_expression(modelexpression)
    # Perform fit
    fit.do_fit() 
    # Report fit results if desired
    if report:
        fit.report()
    # Return fit
    return fit



###################################################
# Fit a photopeak using a Gaussian model function #
###################################################

def fit_peak (data, x1=None, x2=None, baseline = 0, showResult = False, label = None, ax = None, **initparams):
    # Check if a lower x-limit for the fit is given, otherwise use the minimum of the provided dataset
    if x1 == None:
        x1 = min(data[0])
    # Check if an upper x-limit for the fit is given, otherwise use the maximum of the provided dataset
    if x2 == None:
        x2 = max(data[0])
    # Remove datapoints outside the specified fit range
    datax = np.delete(data[0], np.where((x1 > data[0]) | (data[0] > x2)))
    datay = np.delete(data[1], np.where((x1 > data[0]) | (data[0] > x2)))
    # Perform a Gaussian fit on the remaining data, choosing the position of the maximum value in the data as an initial value for the position of the peak and it's value for the height of the peak
    fit = hist_fit_data(datax, datay, model=gaussian, limitedparams = ['mu', 'sigma'], fixedparams = [["baseline", baseline]], mu=datax[np.argmax(datay)], A = np.max(datay), label = label, **initparams)
    # Plot the results of the fit if desired
    if showResult:
        p = Plot(fit)
        p.plot()
        plt.show()
    return fit



###########################################################
# Fit a compton edge using a complementary error function #
###########################################################

def fit_compton (data, x1 = None, x2 = None, showResult = False, label = None, smoothData = False):
    # Check if a lower x-limit for the fit is given, otherwise use the minimum of the provided dataset
    if x1 == None:
        x1 = min(data[0])
    # Check if an upper x-limit for the fit is given, otherwise use the maximum of the provided dataset
    if x2 == None:
        x2 = max(data[0])
    # Remove datapoints outside the specified fit range
    datax = np.delete(data[0], np.where((x1 > data[0]) | (data[0] > x2)))
    datay = np.delete(data[1], np.where((x1 > data[0]) | (data[0] > x2)))
    # Smooth the data before fitting if desired
    if smoothData:
        datay = smooth(datay, r=100)
    # Determine an initial value for the position of the compton edge by estimating where the slope is maximal
    dif = np.diff(datay)
    diffs = []
    for i in range(len(datay-25)):
        diffs.append(np.abs(np.sum(dif[i:i+25])))
    mu0 = datax[np.argmax(diffs)]
    # Perform the fit on the remaining data using the estimated position as an initial value
    fit = hist_fit_data(datax, datay, model=compton_edge, limitedparams = ['mu', 'sigma'], mu=mu0, label = label)
    # Plot the results of the fit if desired
    if showResult:
        Plot(fit)
    return fit



#######################################################################
# Determine the resolution and it's energy dependence of the detector #
#######################################################################

def determine_resolution (fits):
    # Extract position and standard deviation from the fits
    mu = np.array([fit.parameter_values[0] for fit in fits])
    sigma = np.array([fit.parameter_values[1] for fit in fits])
    # Calculate the resolution in percent using the FWHM of the peaks
    r = 100 * 2 * np.sqrt(2 * np.log(2)) * sigma / mu
    # Fit the energy dependence of the resloution
    fit = fit_data(mu, r, xerr = list(sigma), yerr = list(r * sigma / mu), model = inv_sqrt_model)
    # Show the results of the fit
    p = Plot(fit)
    p.x_label = 'Energy (keV)'
    p.y_label = 'Resolution (%)'
    p.y_range = (0,100)
    p.plot()
    plt.show()
    # Return the positions, resolutions and fit
    return (mu, r, fit)
