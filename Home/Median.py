# -*- coding: utf-8 *-*

def checkio(data):
    '''
        Takes a list and returns the median.
    '''
    data.sort()    
    if len(data) % 2 == 1:
        ind_median = int((len(data)-1)/2)
        return data[ind_median]
    else:
        ind_median1 = int(len(data)/2)-1
        ind_median2 = int(len(data)/2)
        return (data[ind_median1] + data[ind_median2]) / 2
