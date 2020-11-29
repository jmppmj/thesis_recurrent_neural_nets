#!/usr/bin/env python
# coding: utf-8

#only run once~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#creates csv with :::2010's::: feature data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#:::hmi.sharp_720s from JSOC:::
#http://jsoc.stanford.edu/doc/data/hmi/sharp/sharp.htm

import pandas as pd
import drms #https://pypi.org/project/drms/

#compile :::2010::: feature dataframe
#multiple queries needed due to record return limit

def get_2010_Features():

	h = drms.Client()

	k = h.query('hmi.sharp_720s[][2010.01.01_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = k

	k = h.query('hmi.sharp_720s[][2010.01.08_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.01.15_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.01.22_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.01.29_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.02.05_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.02.12_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.02.19_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.02.26_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.03.05_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.03.12_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.03.19_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.03.26_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.04.02_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.04.09_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.04.16_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.04.23_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.04.30_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.05.07_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.05.14_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.05.21_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.05.28_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.06.04_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.06.11_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.06.18_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.06.25_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.07.02_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.07.09_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.07.16_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.07.23_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.07.30_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.08.06_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.08.13_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.08.20_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.08.27_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.09.03_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.09.10_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.09.17_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.09.24_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.10.01_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.10.08_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.10.15_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.10.22_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.10.29_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.11.05_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.11.12_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.11.19_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.11.26_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.12.03_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.12.10_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.12.17_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.12.24_TAI/7d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)
	
	k = h.query('hmi.sharp_720s[][2010.12.31_TAI/1d]', key='T_REC, HARPNUM, NOAA_AR, TOTUSJH, TOTUSJZ, SAVNCPP, USFLUX, ABSNJZH, TOTPOT, SIZE_ACR, NACR, MEANPOT, SIZE, MEANJZH, SHRGT45, MEANSHR, MEANJZD, MEANALP, MEANGBT, MEANGAM, MEANGBZ, MEANGBH, NPIX')
	f_dataframe = f_dataframe.append(k)

	f_dataframe.to_csv('create_2010_features.csv')
	
	return()

