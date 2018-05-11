import pylab as plt
import numpy as np
import data_import as di
import analyses as an
from scipy.stats import sem
from collections import OrderedDict
import datetime 

surgery_date_p8 =  datetime.date(year = 2018, month = 4,day = 13)
surgery_date_p6 =  datetime.date(year = 2018,month = 4, day = 5)
LED_change_day =  datetime.date(year = 2018,month = 4, day = 25)

files_locked_days = ['p8-VTA-2018-04-21-154042.ppd',
        'p8-VTA-2018-04-20-141632.ppd',
                'p6-VTA-2018-04-18-163630.ppd',
                'p6-VTA-2018-04-19-151656.ppd',
                'p6-VTA-2018-04-20-145009.ppd',
                'p6-VTA-2018-04-23-160639.ppd',
                'p6-VTA-2018-04-24-135449.ppd',
                'p6-VTA-2018-04-25-150903.ppd',
                'p6-VTA-2018-04-26-152443.ppd',
                'p6-VTA-2018-04-27-161456.ppd',
                'p6-VTA-2018-04-30-143356.ppd',
                'p6-VTA-2018-05-01-144341.ppd',
                'p6-VTA-2018-05-02-152339.ppd',
                'p8-VTA-2018-04-23-154732.ppd',
                'p8-VTA-2018-04-24-134041.ppd',
                'p8-VTA-2018-04-25-152234.ppd',
                'p8-VTA-2018-04-26-153813.ppd',
                'p8-VTA-2018-04-27-163015.ppd',
                'p8-VTA-2018-05-04-122255.ppd',
                'p8-VTA-2018-05-03-133907.ppd',
                'p8-VTA-2018-05-02-153608.ppd',
                'p8-VTA-2018-05-01-151122.ppd',
                'p8-VTA-2018-04-30-145304.ppd']
                     
                

files_isbs_locked = ['p8-VTA-2018-04-23-154732.ppd',
                     'p8-VTA-2018-04-24-134041.ppd',
                     'p8-VTA-2018-04-25-152234.ppd',
                     'p8-VTA-2018-04-26-153813.ppd',
                     'p8-VTA-2018-04-27-163015.ppd',
                     'p6-VTA-2018-05-02-152339.ppd',
                     'p6-VTA-2018-05-01-144341.ppd',
                     'p6-VTA-2018-04-26-152443.ppd',
                     'p6-VTA-2018-04-27-161456.ppd',
                     'p6-VTA-2018-04-25-150903.ppd',
                     'p6-VTA-2018-04-24-135449.ppd',
                     'p6-VTA-2018-04-23-160639.ppd',
                     'p6-VTA-2018-04-19-151656.ppd',
                     'p8-VTA-2018-05-04-122255.ppd',
                     'p8-VTA-2018-05-03-133907.ppd',
                     'p8-VTA-2018-05-02-153608.ppd',
                     'p8-VTA-2018-05-01-151122.ppd',
                     'p8-VTA-2018-04-30-145304.ppd']

files_isbs_lk100z = ['p8-VTA-2018-04-27-163542.ppd',
                     'p8-VTA-2018-04-30-145846.ppd',
                     'p6-VTA-2018-04-30-143919.ppd']                     

files_isbs_unlckd = ['p8-VTA-2018-04-23-154216.ppd',
                     'p8-VTA-2018-04-24-133506.ppd',
                     'p8-VTA-2018-04-25-151702.ppd',
                     'p8-VTA-2018-04-26-153228.ppd',
                     'p8-VTA-2018-04-27-162419.ppd',
                     'p8-VTA-2018-04-30-144708.ppd',
                     'p6-VTA-2018-05-02-151813.ppd',
                     'p6-VTA-2018-05-01-143814.ppd',
                     'p6-VTA-2018-04-30-142811.ppd',
                     'p6-VTA-2018-04-27-160841.ppd',
                     'p6-VTA-2018-04-27-161456.ppd',
                     'p6-VTA-2018-04-26-151911.ppd',
                     'p6-VTA-2018-04-25-150118.ppd',
                     'p6-VTA-2018-04-24-134834.ppd',
                     'p6-VTA-2018-04-23-160153.ppd',
                     'p8-VTA-2018-05-04-121723.ppd',
                     'p8-VTA-2018-05-03-133318.ppd',
                     'p8-VTA-2018-05-02-153036.ppd',
                     'p8-VTA-2018-05-01-150520.ppd']

files_rdif_locked = ['p8-VTA-2018-04-23-153033.ppd',
                     'p8-VTA-2018-04-24-143557.ppd',
                     'p8-VTA-2018-04-25-142439.ppd',
                     'p8-VTA-2018-04-27-165210.ppd',
                     'p8-VTA-2018-04-30-135202.ppd',
                     'p6-VTA-2018-05-02-145505.ppd',
                     'p6-VTA-2018-05-01-160659.ppd',
                     'p6-VTA-2018-04-30-140550.ppd',
                     'p6-VTA-2018-04-27-172926.ppd',
                     'p6-VTA-2018-04-26-150452.ppd',
                     'p6-VTA-2018-04-25-144501.ppd',
                     'p6-VTA-2018-04-24-141014.ppd',
                     'p8-VTA-2018-05-04-120709.ppd',
                     'p8-VTA-2018-05-03-141556.ppd',
                     'p8-VTA-2018-05-02-144244.ppd',
                     'p8-VTA-2018-05-01-155250.ppd']

files_rdif_unlckd = ['p8-VTA-2018-04-23-152515.ppd',
                     'p8-VTA-2018-04-24-142901.ppd',
                     'p8-VTA-2018-04-25-141746.ppd',
                     'p8-VTA-2018-04-26-143507.ppd',
                     'p8-VTA-2018-04-27-164631.ppd',
                     'p8-VTA-2018-04-30-134545.ppd',
                     'p6-VTA-2018-05-02-144943.ppd',
                     'p6-VTA-2018-05-01-155942.ppd',
                     'p6-VTA-2018-04-30-140002.ppd',
                     'p6-VTA-2018-04-27-172358.ppd',
                     'p6-VTA-2018-04-26-145856.ppd',
                     'p6-VTA-2018-04-25-143729.ppd',
                     'p6-VTA-2018-04-24-140451.ppd',
                     'p8-VTA-2018-05-04-120123.ppd',
                     'p8-VTA-2018-05-03-140922.ppd',
                     'p8-VTA-2018-05-02-143709.ppd',
                     'p8-VTA-2018-05-01-154024.ppd']

files_rcon_unlckd = ['p8-VTA-2018-04-27-165829.ppd',
                     'p8-VTA-2018-04-30-133317.ppd',
                     'p6-VTA-2018-05-02-150032.ppd',
                     'p6-VTA-2018-05-01-161249.ppd',
                     'p6-VTA-2018-04-30-141148.ppd',
                     'p6-VTA-2018-04-27-171140.ppd',
                     'p6-VTA-2018-04-24-141554.ppd',
                     'p8-VTA-2018-05-04-114923.ppd',
                     'p8-VTA-2018-05-03-134958.ppd',
                     'p8-VTA-2018-05-02-142430.ppd',
                     'p8-VTA-2018-05-01-152653.ppd']

files_rcon_locked = ['p8-VTA-2018-04-20-141632.ppd',
                     'p8-VTA-2018-04-25-135250.ppd',
                     'p8-VTA-2018-04-27-170423.ppd',
                     'p8-VTA-2018-04-30-133859.ppd',
                     'p6-VTA-2018-05-02-150558.ppd',
                     'p6-VTA-2018-05-01-161845.ppd',
                     'p6-VTA-2018-04-30-141740.ppd',
                     'p6-VTA-2018-04-27-171711.ppd',
                     'p6-VTA-2018-04-24-142118.ppd',
                     'p8-VTA-2018-05-04-115502.ppd',
                     'p8-VTA-2018-05-03-140309.ppd',
                     'p8-VTA-2018-05-02-143100.ppd',
                     'p8-VTA-2018-05-01-153359.ppd',
                     'p8-VTA-2018-04-30-133859.ppd']

data_dict = OrderedDict([
    #('isbs_lk100z', [di.import_data(file_name) for file_name in files_isbs_lk100z]),
    ('isbs_locked', [di.import_data(file_name) for file_name in files_isbs_locked]),
    ('isbs_unlckd', [di.import_data(file_name) for file_name in files_isbs_unlckd]),
    ('rdif_locked', [di.import_data(file_name) for file_name in files_rdif_locked]),
    ('rdif_unlckd', [di.import_data(file_name) for file_name in files_rdif_unlckd]),
    ('rcon_locked', [di.import_data(file_name) for file_name in files_rcon_locked]),
    ('rcon_unlckd', [di.import_data(file_name) for file_name in files_rcon_unlckd])])


def control_signal_CV_plot(fig_no=1):
    motion_signal_CV = [[an.motion_signal_CV(data) for data in condition]
                         for condition in data_dict.values()]
    bar_plot(motion_signal_CV, fig_no, data_dict.keys(), 'Control signal CV')


def motion_correction_CV_plot(fig_no=2):
    '''Bar chart of the coefficient of variation of estimated motion correction to the GCaMP 
    signal across conditions.'''
    motion_corr_CV = [[np.sqrt(an.motion_ESS(data)) for data in condition]
                       for condition in data_dict.values()]
    bar_plot(motion_corr_CV, fig_no, data_dict.keys(), 'Motion correction CV')

def predicted_control_R2_plot(fig_no=3):
    '''Bar chart of the r^2 of a linear prediction of the control signal from the GCaMP signal.'''
    pred_con_R2 = [[np.sqrt(an.control_R2(data)) for data in condition]
                    for condition in data_dict.values()]
    bar_plot(pred_con_R2, fig_no, data_dict.keys(), 'predicted control signal R2')

def signal_correlation_plot(fig_no=4):
    '''Bar chart of the correlation between the two channels across conditions'''
    sig_corrs = [[np.corrcoef(data['ADC1_filt'],data['ADC2_filt'])[0,1] for data in condition]
                 for condition in data_dict.values()]
    bar_plot(sig_corrs, fig_no, data_dict.keys(), 'GCaMP - control correlation')

def bar_plot(x, fig_no, xticks, ylabel):
    plt.figure(fig_no, figsize=[3.5,3]).clf()
    mean_x = [np.mean(x_i) for x_i in x]
    sem_x  = [sem(x_i)     for x_i in x]
    plt.bar(np.arange(len(x)), mean_x, yerr=sem_x)
    if min(mean_x)>0: plt.ylim(ymin=0)
    plt.ylabel(ylabel)
    plt.xticks(np.arange(len(x)), xticks, rotation=-45, ha='left')
    plt.tight_layout()