#!/usr/bin/env python
# coding: utf-8

#only run once~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#creates csv with :::2012's::: feature data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#:::hmi.sharp_720s from JSOC:::
#http://jsoc.stanford.edu/doc/data/hmi/sharp/sharp.htm

import pandas as pd
import drms #https://pypi.org/project/drms/

#compile :::2012::: feature dataframe
#multiple queries needed due to record return limit

def get_2012_Features():

	h = drms.Client()

	k = h.query('hmi.sharp_720s[][2012.01.01_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = k

	k = h.query('hmi.sharp_720s[][2012.01.08_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.01.15_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.01.22_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.01.29_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.02.05_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.02.12_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.02.19_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.02.26_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.03.04_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.03.11_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.03.18_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.03.25_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.04.01_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.04.08_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.04.15_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.04.22_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.04.29_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.05.06_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.05.13_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.05.20_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.05.27_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.06.03_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.06.10_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.06.17_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.06.24_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.07.01_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.07.08_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.07.15_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.07.22_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.07.29_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.08.05_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.08.12_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.08.19_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.08.26_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.09.02_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.09.09_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.09.16_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.09.23_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.09.30_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.10.07_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.10.14_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.10.21_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.10.28_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.11.04_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.11.11_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.11.18_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.11.25_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.12.02_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.12.09_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.12.16_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.12.23_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2012.12.30_TAI/2d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	#tests
	#print('The time series starts from: ', f_dataframe['T_REC'].min())
	#print('The time series ends on: ', f_dataframe['T_REC'].max())
	#print(f_dataframe.shape)

	f_dataframe.to_csv('create_2012_features.csv')
	
	return()

