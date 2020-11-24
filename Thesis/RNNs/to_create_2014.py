#!/usr/bin/env python
# coding: utf-8

#only run once~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#creates csv with :::2014's::: feature data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#:::hmi.sharp_720s from JSOC:::
#http://jsoc.stanford.edu/doc/data/hmi/sharp/sharp.htm

import pandas as pd
import drms #https://pypi.org/project/drms/

#compile :::2014::: feature dataframe
#multiple queries needed due to record return limit

def get_2014_Features():

	h = drms.Client()

	k = h.query('hmi.sharp_720s[][2014.01.01_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = k

	k = h.query('hmi.sharp_720s[][2014.01.10_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.01.19_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.01.29_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.02.08_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.02.18_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.02.27_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.03.09_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.03.19_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.03.28_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.04.06_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.04.16_TAI/8d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.04.24_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.05.01_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.05.11_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.05.21_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.05.31_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.06.10_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.06.19_TAI/12d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.07.01_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.07.11_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.07.21_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.07.31_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.08.10_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.08.20_TAI/12d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.09.01_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.09.10_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.09.20_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.09.30_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.10.10_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.10.20_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.10.30_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.11.06_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.11.16_TAI/11d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.11.27_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.12.06_TAI/10d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.12.16_TAI/9d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	k = h.query('hmi.sharp_720s[][2014.12.25_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	#tests
	#print('The time series starts from: ', f_dataframe['T_REC'].min())
	#print('The time series ends on: ', f_dataframe['T_REC'].max())
	#print(f_dataframe.shape)

	f_dataframe.to_csv('create_2014_features.csv')
	
	return()
