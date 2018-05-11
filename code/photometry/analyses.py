import numpy as np
import pylab as plt
import matplotlib as plot
from sklearn.linear_model import LinearRegression
import data_import as di
import os
import script 
from datetime import datetime

def motion_ESS(data, fig_no=False):
    # Evaluate the variance in the GCaMP signal explained by the control signal.
    OLS = LinearRegression()
    OLS.fit(data['ADC2_filt'][:,None], data['ADC1_filt'][:,None])
    estimated_motion = OLS.predict(data['ADC2_filt'][:,None]).squeeze()
    corrected_signal = data['ADC1_filt'] - estimated_motion
    ESS = np.var(estimated_motion)  # Explained sum of squares per sample.
    TSS = np.var(data['ADC1_filt']) # Total     sum of squares per sample.
    r2 = ESS/TSS                    # Fraction of explained variance.
    ESS_norm = ESS/(np.mean(data['ADC1'])**2) # Explained variance per sample normalised by average fluorescence squred.
    if fig_no:
        plt.figure(fig_no).clf()
        plt.subplot(2,1,1)
        plt.plot(data['t'], data['ADC1'])
        plt.plot(data['t'], data['ADC2'])
        plt.subplot(2,1,2)
        plt.plot(data['t'], data['ADC1_filt'])
        plt.plot(data['t'], corrected_signal)
        plt.figure(fig_no+1).clf()
        plt.plot(estimated_motion, corrected_signal)
        plt.xlabel('Motion signal')
        plt.ylabel('Corrected signal')
    return ESS_norm

def std_mean_relationship():
    path = '/Users/veronikasamborska/Desktop/photometry_code/code/data'
    files = os.listdir(path)
    mean_signal_corrected_list=[]
    std_list=[]
    plt.figure()
    for file in files:
       if 'p8-VTA-2018-04-20-142431.ppd' in file:
           data = di.import_data(file)
           OLS = LinearRegression()
           OLS.fit(data['ADC2_filt'][:,None], data['ADC1_filt'][:,None])
           estimated_motion = OLS.predict(data['ADC2_filt'][:,None]).squeeze()
           corrected_signal = data['ADC1_filt'] - estimated_motion
           mean_signal_corrected = np.mean(data['ADC1'])
           std_signal_corrected = np.std(corrected_signal)
           mean_signal_corrected_list.append(mean_signal_corrected)
           std_list.append(std_signal_corrected)
           plt.xscale('linear')
           plt.scatter(mean_signal_corrected, std_signal_corrected)
           plt.pause(0.05)
           plt.xlabel('Mean Signal')
           plt.ylabel('Standard Deviationj of the Signal')
    z = np.polyfit(mean_signal_corrected_list,std_list, 1)
    p = np.poly1d(z)
    plt.plot(mean_signal_corrected_list,p(mean_signal_corrected_list),"r")
    plt.show()

def calcium():
    path = '/Users/veronikasamborska/Desktop/photometry_code/code/data'
    files = os.listdir(path)
    session_list=[]
    std_list=[]
    plt.figure()
    date_list = []
    session_list_old_LED = []
    date_list_old_LED = []
    std_list_old_LED =[]
    for file in files:
       if 'p8' in file:
           if file in files_locked_days:
               data = di.import_data(file)
               if data['datetime'] <= LED_change_day: 
                   date_int_old_LED = data['datetime'] -surgery_date_p8
                   std_old_LED = np.std(data['ADC1_filt'])
                   std_list_old_LED.append(std_old_LED)
                   session_list_old_LED.append(data['datetime_str'])
                   date_list_old_LED.append(date_int_old_LED.days)
               else: 
                   date_int = data['datetime'] -surgery_date_p8
                   std = np.std(data['ADC1_filt'])
                   std_list.append(std)
                   session_list.append(data['datetime_str'])
                   date_list.append(date_int.days)
               #if std < 0.05: 
                   #print(file)   
    date_list_old_LED.sort()  
    date_list.sort()
    print(date_list)
    sorted_ind = np.argsort(session_list)
    session_list.sort(key=lambda date: datetime.strptime(date,'%Y-%m-%d %H:%M:%S'))
    np_std = np.asarray(std_list)
    newarray = np_std[sorted_ind]
    
    sorted_ind_old_LED = np.argsort(session_list_old_LED)
    session_list_old_LED.sort(key=lambda date: datetime.strptime(date,'%Y-%m-%d %H:%M:%S'))
    np_std_old = np.asarray(std_list_old_LED)
    newarray_old_LED = np_std_old[sorted_ind_old_LED]
    #plt.xlim(min(date_list_old_LED), max(date_list))
    plt.scatter(date_list,newarray, color = 'red', label = 'Old LED')
    plt.scatter(date_list_old_LED,newarray_old_LED, color = 'blue', label = 'New LED')
    plt.legend()
    plt.xlabel('Days from Surgery')
    plt.ylabel('Standard Deviationj of the Signal')
    plt.title('p8')
    plt.show()
    
def control_R2(data):
    # Evaluate the R^2 for a linear prediction of teh control signal from the GCaMP signal.
    OLS = LinearRegression()
    OLS.fit(data['ADC1_filt'][:,None], data['ADC2_filt'][:,None])
    estimated_control_sig = OLS.predict(data['ADC1_filt'][:,None]).squeeze()
    ESS = np.var(estimated_control_sig)  # Explained sum of squares per sample.
    ESS_norm = ESS/(np.mean(data['ADC2'])**2) # Explained variance per sample normalised by average fluorescence squred.
    R2 = ESS / np.var(data['ADC2_filt'])
    return R2

def motion_signal_CV(data):
    # Evaluate the coefficient of variation of the motion control signal.
    return np.std(data['ADC2_filt']) / np.mean(data['ADC2']) 

def motion_gcamp_correlation(data, n_fold=10, fig_no=False):
    '''Evaluate the cross validated correlation between the estimated motion signal and
    the GCaMP signal after motion correction.'''
    OLS = LinearRegression()
    t = data['t']
    estimated_motion = np.zeros(t.shape)
    corrected_signal = np.zeros(t.shape)
    for i in range(n_fold):
        test_mask  = ((i/n_fold)*t[-1] < t) & (t < ((i+1)/n_fold)*t[-1])
        train_mask = ~test_mask
        OLS.fit(data['ADC2_filt'][train_mask,None], data['ADC1_filt'][train_mask,None])
        estimated_motion[test_mask] = OLS.predict(data['ADC2_filt'][test_mask,None]).squeeze()
        corrected_signal[test_mask] = data['ADC1_filt'][test_mask] - estimated_motion[test_mask]
    if fig_no:
        plt.figure(fig_no).clf()
        plt.plot(data['t'], data['ADC1_filt'])        
        plt.plot(data['t'], corrected_signal)
        plt.plot(data['t'], estimated_motion)
    return np.corrcoef(estimated_motion, corrected_signal)
