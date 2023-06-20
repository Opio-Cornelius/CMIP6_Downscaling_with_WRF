#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:49:21 2023

@author: oronald
"""

import numpy as np
import pandas as pd
import xarray as xr


file1 = xr.open_dataset('/home/oronald/model/boundaries/cmip6/low_ssp370/ts_Eday_MPI-ESM-1-2-HAM_ssp370-lowNTCF_r1i1p1f1_gn_20550101-20551231.nc')

print(file1)
print("===="*70)

# Read-in variable you want to modify
ts = file1['ts']


# Create variables for each day of 2021

" 2055 "

for day in range(1, 32):
    date_string = f"2055-01-{day:02d}T12:00:00.000000000"
    var_name = f"jan_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 32):
    date_string = f"2055-03-{day:02d}T12:00:00.000000000"
    var_name = f"mar_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 31):
    date_string = f"2055-04-{day:02d}T12:00:00.000000000"
    var_name = f"apr_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 32):
    date_string = f"2055-05-{day:02d}T12:00:00.000000000"
    var_name = f"may_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 31):
    date_string = f"2055-06-{day:02d}T12:00:00.000000000"
    var_name = f"june_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 32):
    date_string = f"2055-07-{day:02d}T12:00:00.000000000"
    var_name = f"july_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 32):
    date_string = f"2055-08-{day:02d}T12:00:00.000000000"
    var_name = f"aug_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 31):
    date_string = f"2055-09-{day:02d}T12:00:00.000000000"
    var_name = f"sep_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 32):
    date_string = f"2055-10-{day:02d}T12:00:00.000000000"
    var_name = f"oct_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 31):
    date_string = f"2055-11-{day:02d}T12:00:00.000000000"
    var_name = f"nov_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 32):
    date_string = f"2055-12-{day:02d}T12:00:00.000000000"
    var_name = f"dec_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]

for day in range(1, 29):
    date_string = f"2055-02-{day:02d}T12:00:00.000000000"
    var_name = f"feb_{day}_2055"
    globals()[var_name] = ts.loc[date_string, :, :]





# Create new dataset for 6-hourly ts

ts_6hr_stack = np.stack((jan_1_2055, jan_1_2055, jan_1_2055, jan_1_2055, jan_2_2055, jan_2_2055, jan_2_2055, jan_2_2055,
jan_3_2055, jan_3_2055, jan_3_2055, jan_3_2055, jan_4_2055, jan_4_2055, jan_4_2055, jan_4_2055,
jan_5_2055, jan_5_2055, jan_5_2055, jan_5_2055, jan_6_2055, jan_6_2055, jan_6_2055, jan_6_2055,
jan_7_2055, jan_7_2055, jan_7_2055, jan_7_2055, jan_8_2055, jan_8_2055, jan_8_2055, jan_8_2055,
jan_9_2055, jan_9_2055, jan_9_2055, jan_9_2055, jan_10_2055, jan_10_2055, jan_10_2055, jan_10_2055,
jan_11_2055, jan_11_2055, jan_11_2055, jan_11_2055, jan_12_2055, jan_12_2055, jan_12_2055, jan_12_2055,
jan_13_2055, jan_13_2055, jan_13_2055, jan_13_2055, jan_14_2055, jan_14_2055, jan_14_2055, jan_14_2055,
jan_15_2055, jan_15_2055, jan_15_2055, jan_15_2055, jan_16_2055, jan_16_2055, jan_16_2055, jan_16_2055,
jan_17_2055, jan_17_2055, jan_17_2055, jan_17_2055, jan_18_2055, jan_18_2055, jan_18_2055, jan_18_2055,
jan_19_2055, jan_19_2055, jan_19_2055, jan_19_2055, jan_20_2055, jan_20_2055, jan_20_2055, jan_20_2055,
jan_21_2055, jan_21_2055, jan_21_2055, jan_21_2055, jan_22_2055, jan_22_2055, jan_22_2055, jan_22_2055,
jan_23_2055, jan_23_2055, jan_23_2055, jan_23_2055, jan_24_2055, jan_24_2055, jan_24_2055, jan_24_2055,
jan_25_2055, jan_25_2055, jan_25_2055, jan_25_2055, jan_26_2055, jan_26_2055, jan_26_2055, jan_26_2055,
jan_27_2055, jan_27_2055, jan_27_2055, jan_27_2055, jan_28_2055, jan_28_2055, jan_28_2055, jan_28_2055,
jan_29_2055, jan_29_2055, jan_29_2055, jan_29_2055, jan_30_2055, jan_30_2055, jan_30_2055, jan_30_2055,
jan_31_2055, jan_31_2055, jan_31_2055, jan_31_2055,
feb_1_2055, feb_1_2055, feb_1_2055, feb_1_2055, feb_2_2055, feb_2_2055, feb_2_2055, feb_2_2055,
feb_3_2055, feb_3_2055, feb_3_2055, feb_3_2055, feb_4_2055, feb_4_2055, feb_4_2055, feb_4_2055,
feb_5_2055, feb_5_2055, feb_5_2055, feb_5_2055, feb_6_2055, feb_6_2055, feb_6_2055, feb_6_2055,
feb_7_2055, feb_7_2055, feb_7_2055, feb_7_2055, feb_8_2055, feb_8_2055, feb_8_2055, feb_8_2055,
feb_9_2055, feb_9_2055, feb_9_2055, feb_9_2055, feb_10_2055, feb_10_2055, feb_10_2055, feb_10_2055,
feb_11_2055, feb_11_2055, feb_11_2055, feb_11_2055, feb_12_2055, feb_12_2055, feb_12_2055, feb_12_2055,
feb_13_2055, feb_13_2055, feb_13_2055, feb_13_2055, feb_14_2055, feb_14_2055, feb_14_2055, feb_14_2055,
feb_15_2055, feb_15_2055, feb_15_2055, feb_15_2055, feb_16_2055, feb_16_2055, feb_16_2055, feb_16_2055,
feb_17_2055, feb_17_2055, feb_17_2055, feb_17_2055, feb_18_2055, feb_18_2055, feb_18_2055, feb_18_2055,
feb_19_2055, feb_19_2055, feb_19_2055, feb_19_2055, feb_20_2055, feb_20_2055, feb_20_2055, feb_20_2055,
feb_21_2055, feb_21_2055, feb_21_2055, feb_21_2055, feb_22_2055, feb_22_2055, feb_22_2055, feb_22_2055,
feb_23_2055, feb_23_2055, feb_23_2055, feb_23_2055, feb_24_2055, feb_24_2055, feb_24_2055, feb_24_2055,
feb_25_2055, feb_25_2055, feb_25_2055, feb_25_2055, feb_26_2055, feb_26_2055, feb_26_2055, feb_26_2055,
feb_27_2055, feb_27_2055, feb_27_2055, feb_27_2055, feb_28_2055, feb_28_2055, feb_28_2055, feb_28_2055,
mar_1_2055, mar_1_2055, mar_1_2055, mar_1_2055, mar_2_2055, mar_2_2055, mar_2_2055, mar_2_2055,
mar_3_2055, mar_3_2055, mar_3_2055, mar_3_2055, mar_4_2055, mar_4_2055, mar_4_2055, mar_4_2055,
mar_5_2055, mar_5_2055, mar_5_2055, mar_5_2055, mar_6_2055, mar_6_2055, mar_6_2055, mar_6_2055,
mar_7_2055, mar_7_2055, mar_7_2055, mar_7_2055, mar_8_2055, mar_8_2055, mar_8_2055, mar_8_2055,
mar_9_2055, mar_9_2055, mar_9_2055, mar_9_2055, mar_10_2055, mar_10_2055, mar_10_2055, mar_10_2055,
mar_11_2055, mar_11_2055, mar_11_2055, mar_11_2055, mar_12_2055, mar_12_2055, mar_12_2055, mar_12_2055,
mar_13_2055, mar_13_2055, mar_13_2055, mar_13_2055, mar_14_2055, mar_14_2055, mar_14_2055, mar_14_2055,
mar_15_2055, mar_15_2055, mar_15_2055, mar_15_2055, mar_16_2055, mar_16_2055, mar_16_2055, mar_16_2055,
mar_17_2055, mar_17_2055, mar_17_2055, mar_17_2055, mar_18_2055, mar_18_2055, mar_18_2055, mar_18_2055,
mar_19_2055, mar_19_2055, mar_19_2055, mar_19_2055, mar_20_2055, mar_20_2055, mar_20_2055, mar_20_2055,
mar_21_2055, mar_21_2055, mar_21_2055, mar_21_2055, mar_22_2055, mar_22_2055, mar_22_2055, mar_22_2055,
mar_23_2055, mar_23_2055, mar_23_2055, mar_23_2055, mar_24_2055, mar_24_2055, mar_24_2055, mar_24_2055,
mar_25_2055, mar_25_2055, mar_25_2055, mar_25_2055, mar_26_2055, mar_26_2055, mar_26_2055, mar_26_2055,
mar_27_2055, mar_27_2055, mar_27_2055, mar_27_2055, mar_28_2055, mar_28_2055, mar_28_2055, mar_28_2055,
mar_29_2055, mar_29_2055, mar_29_2055, mar_29_2055, mar_30_2055, mar_30_2055, mar_30_2055, mar_30_2055,
mar_31_2055, mar_31_2055, mar_31_2055, mar_31_2055,
apr_1_2055, apr_1_2055, apr_1_2055, apr_1_2055, apr_2_2055, apr_2_2055, apr_2_2055, apr_2_2055,
apr_3_2055, apr_3_2055, apr_3_2055, apr_3_2055, apr_4_2055, apr_4_2055, apr_4_2055, apr_4_2055,
apr_5_2055, apr_5_2055, apr_5_2055, apr_5_2055, apr_6_2055, apr_6_2055, apr_6_2055, apr_6_2055,
apr_7_2055, apr_7_2055, apr_7_2055, apr_7_2055, apr_8_2055, apr_8_2055, apr_8_2055, apr_8_2055,
apr_9_2055, apr_9_2055, apr_9_2055, apr_9_2055, apr_10_2055, apr_10_2055, apr_10_2055, apr_10_2055,
apr_11_2055, apr_11_2055, apr_11_2055, apr_11_2055, apr_12_2055, apr_12_2055, apr_12_2055, apr_12_2055,
apr_13_2055, apr_13_2055, apr_13_2055, apr_13_2055, apr_14_2055, apr_14_2055, apr_14_2055, apr_14_2055,
apr_15_2055, apr_15_2055, apr_15_2055, apr_15_2055, apr_16_2055, apr_16_2055, apr_16_2055, apr_16_2055,
apr_17_2055, apr_17_2055, apr_17_2055, apr_17_2055, apr_18_2055, apr_18_2055, apr_18_2055, apr_18_2055,
apr_19_2055, apr_19_2055, apr_19_2055, apr_19_2055, apr_20_2055, apr_20_2055, apr_20_2055, apr_20_2055,
apr_21_2055, apr_21_2055, apr_21_2055, apr_21_2055, apr_22_2055, apr_22_2055, apr_22_2055, apr_22_2055,
apr_23_2055, apr_23_2055, apr_23_2055, apr_23_2055, apr_24_2055, apr_24_2055, apr_24_2055, apr_24_2055,
apr_25_2055, apr_25_2055, apr_25_2055, apr_25_2055, apr_26_2055, apr_26_2055, apr_26_2055, apr_26_2055,
apr_27_2055, apr_27_2055, apr_27_2055, apr_27_2055, apr_28_2055, apr_28_2055, apr_28_2055, apr_28_2055,
apr_29_2055, apr_29_2055, apr_29_2055, apr_29_2055, apr_30_2055, apr_30_2055, apr_30_2055, apr_30_2055,
may_1_2055, may_1_2055, may_1_2055, may_1_2055, may_2_2055, may_2_2055, may_2_2055, may_2_2055,
may_3_2055, may_3_2055, may_3_2055, may_3_2055, may_4_2055, may_4_2055, may_4_2055, may_4_2055,
may_5_2055, may_5_2055, may_5_2055, may_5_2055, may_6_2055, may_6_2055, may_6_2055, may_6_2055,
may_7_2055, may_7_2055, may_7_2055, may_7_2055, may_8_2055, may_8_2055, may_8_2055, may_8_2055,
may_9_2055, may_9_2055, may_9_2055, may_9_2055, may_10_2055, may_10_2055, may_10_2055, may_10_2055,
may_11_2055, may_11_2055, may_11_2055, may_11_2055, may_12_2055, may_12_2055, may_12_2055, may_12_2055,
may_13_2055, may_13_2055, may_13_2055, may_13_2055, may_14_2055, may_14_2055, may_14_2055, may_14_2055,
may_15_2055, may_15_2055, may_15_2055, may_15_2055, may_16_2055, may_16_2055, may_16_2055, may_16_2055,
may_17_2055, may_17_2055, may_17_2055, may_17_2055, may_18_2055, may_18_2055, may_18_2055, may_18_2055,
may_19_2055, may_19_2055, may_19_2055, may_19_2055, may_20_2055, may_20_2055, may_20_2055, may_20_2055,
may_21_2055, may_21_2055, may_21_2055, may_21_2055, may_22_2055, may_22_2055, may_22_2055, may_22_2055,
may_23_2055, may_23_2055, may_23_2055, may_23_2055, may_24_2055, may_24_2055, may_24_2055, may_24_2055,
may_25_2055, may_25_2055, may_25_2055, may_25_2055, may_26_2055, may_26_2055, may_26_2055, may_26_2055,
may_27_2055, may_27_2055, may_27_2055, may_27_2055, may_28_2055, may_28_2055, may_28_2055, may_28_2055,
may_29_2055, may_29_2055, may_29_2055, may_29_2055, may_30_2055, may_30_2055, may_30_2055, may_30_2055,
may_31_2055, may_31_2055, may_31_2055, may_31_2055,
june_1_2055, june_1_2055, june_1_2055, june_1_2055, june_2_2055, june_2_2055, june_2_2055, june_2_2055,
june_3_2055, june_3_2055, june_3_2055, june_3_2055, june_4_2055, june_4_2055, june_4_2055, june_4_2055,
june_5_2055, june_5_2055, june_5_2055, june_5_2055, june_6_2055, june_6_2055, june_6_2055, june_6_2055,
june_7_2055, june_7_2055, june_7_2055, june_7_2055, june_8_2055, june_8_2055, june_8_2055, june_8_2055,
june_9_2055, june_9_2055, june_9_2055, june_9_2055, june_10_2055, june_10_2055, june_10_2055, june_10_2055,
june_11_2055, june_11_2055, june_11_2055, june_11_2055, june_12_2055, june_12_2055, june_12_2055, june_12_2055,
june_13_2055, june_13_2055, june_13_2055, june_13_2055, june_14_2055, june_14_2055, june_14_2055, june_14_2055,
june_15_2055, june_15_2055, june_15_2055, june_15_2055, june_16_2055, june_16_2055, june_16_2055, june_16_2055,
june_17_2055, june_17_2055, june_17_2055, june_17_2055, june_18_2055, june_18_2055, june_18_2055, june_18_2055,
june_19_2055, june_19_2055, june_19_2055, june_19_2055, june_20_2055, june_20_2055, june_20_2055, june_20_2055,
june_21_2055, june_21_2055, june_21_2055, june_21_2055, june_22_2055, june_22_2055, june_22_2055, june_22_2055,
june_23_2055, june_23_2055, june_23_2055, june_23_2055, june_24_2055, june_24_2055, june_24_2055, june_24_2055,
june_25_2055, june_25_2055, june_25_2055, june_25_2055, june_26_2055, june_26_2055, june_26_2055, june_26_2055,
june_27_2055, june_27_2055, june_27_2055, june_27_2055, june_28_2055, june_28_2055, june_28_2055, june_28_2055,
june_29_2055, june_29_2055, june_29_2055, june_29_2055, june_30_2055, june_30_2055, june_30_2055, june_30_2055,
july_1_2055, july_1_2055, july_1_2055, july_1_2055, july_2_2055, july_2_2055, july_2_2055, july_2_2055,
july_3_2055, july_3_2055, july_3_2055, july_3_2055, july_4_2055, july_4_2055, july_4_2055, july_4_2055,
july_5_2055, july_5_2055, july_5_2055, july_5_2055, july_6_2055, july_6_2055, july_6_2055, july_6_2055,
july_7_2055, july_7_2055, july_7_2055, july_7_2055, july_8_2055, july_8_2055, july_8_2055, july_8_2055,
july_9_2055, july_9_2055, july_9_2055, july_9_2055, july_10_2055, july_10_2055, july_10_2055, july_10_2055,
july_11_2055, july_11_2055, july_11_2055, july_11_2055, july_12_2055, july_12_2055, july_12_2055, july_12_2055,
july_13_2055, july_13_2055, july_13_2055, july_13_2055, july_14_2055, july_14_2055, july_14_2055, july_14_2055,
july_15_2055, july_15_2055, july_15_2055, july_15_2055, july_16_2055, july_16_2055, july_16_2055, july_16_2055,
july_17_2055, july_17_2055, july_17_2055, july_17_2055, july_18_2055, july_18_2055, july_18_2055, july_18_2055,
july_19_2055, july_19_2055, july_19_2055, july_19_2055, july_20_2055, july_20_2055, july_20_2055, july_20_2055,
july_21_2055, july_21_2055, july_21_2055, july_21_2055, july_22_2055, july_22_2055, july_22_2055, july_22_2055,
july_23_2055, july_23_2055, july_23_2055, july_23_2055, july_24_2055, july_24_2055, july_24_2055, july_24_2055,
july_25_2055, july_25_2055, july_25_2055, july_25_2055, july_26_2055, july_26_2055, july_26_2055, july_26_2055,
july_27_2055, july_27_2055, july_27_2055, july_27_2055, july_28_2055, july_28_2055, july_28_2055, july_28_2055,
july_29_2055, july_29_2055, july_29_2055, july_29_2055, july_30_2055, july_30_2055, july_30_2055, july_30_2055,
july_31_2055, july_31_2055, july_31_2055, july_31_2055,
aug_1_2055, aug_1_2055, aug_1_2055, aug_1_2055, aug_2_2055, aug_2_2055, aug_2_2055, aug_2_2055,
aug_3_2055, aug_3_2055, aug_3_2055, aug_3_2055, aug_4_2055, aug_4_2055, aug_4_2055, aug_4_2055,
aug_5_2055, aug_5_2055, aug_5_2055, aug_5_2055, aug_6_2055, aug_6_2055, aug_6_2055, aug_6_2055,
aug_7_2055, aug_7_2055, aug_7_2055, aug_7_2055, aug_8_2055, aug_8_2055, aug_8_2055, aug_8_2055,
aug_9_2055, aug_9_2055, aug_9_2055, aug_9_2055, aug_10_2055, aug_10_2055, aug_10_2055, aug_10_2055,
aug_11_2055, aug_11_2055, aug_11_2055, aug_11_2055, aug_12_2055, aug_12_2055, aug_12_2055, aug_12_2055,
aug_13_2055, aug_13_2055, aug_13_2055, aug_13_2055, aug_14_2055, aug_14_2055, aug_14_2055, aug_14_2055,
aug_15_2055, aug_15_2055, aug_15_2055, aug_15_2055, aug_16_2055, aug_16_2055, aug_16_2055, aug_16_2055,
aug_17_2055, aug_17_2055, aug_17_2055, aug_17_2055, aug_18_2055, aug_18_2055, aug_18_2055, aug_18_2055,
aug_19_2055, aug_19_2055, aug_19_2055, aug_19_2055, aug_20_2055, aug_20_2055, aug_20_2055, aug_20_2055,
aug_21_2055, aug_21_2055, aug_21_2055, aug_21_2055, aug_22_2055, aug_22_2055, aug_22_2055, aug_22_2055,
aug_23_2055, aug_23_2055, aug_23_2055, aug_23_2055, aug_24_2055, aug_24_2055, aug_24_2055, aug_24_2055,
aug_25_2055, aug_25_2055, aug_25_2055, aug_25_2055, aug_26_2055, aug_26_2055, aug_26_2055, aug_26_2055,
aug_27_2055, aug_27_2055, aug_27_2055, aug_27_2055, aug_28_2055, aug_28_2055, aug_28_2055, aug_28_2055,
aug_29_2055, aug_29_2055, aug_29_2055, aug_29_2055, aug_30_2055, aug_30_2055, aug_30_2055, aug_30_2055,
aug_31_2055, aug_31_2055, aug_31_2055, aug_31_2055,
sep_1_2055, sep_1_2055, sep_1_2055, sep_1_2055, sep_2_2055, sep_2_2055, sep_2_2055, sep_2_2055,
sep_3_2055, sep_3_2055, sep_3_2055, sep_3_2055, sep_4_2055, sep_4_2055, sep_4_2055, sep_4_2055,
sep_5_2055, sep_5_2055, sep_5_2055, sep_5_2055, sep_6_2055, sep_6_2055, sep_6_2055, sep_6_2055,
sep_7_2055, sep_7_2055, sep_7_2055, sep_7_2055, sep_8_2055, sep_8_2055, sep_8_2055, sep_8_2055,
sep_9_2055, sep_9_2055, sep_9_2055, sep_9_2055, sep_10_2055, sep_10_2055, sep_10_2055, sep_10_2055,
sep_11_2055, sep_11_2055, sep_11_2055, sep_11_2055, sep_12_2055, sep_12_2055, sep_12_2055, sep_12_2055,
sep_13_2055, sep_13_2055, sep_13_2055, sep_13_2055, sep_14_2055, sep_14_2055, sep_14_2055, sep_14_2055,
sep_15_2055, sep_15_2055, sep_15_2055, sep_15_2055, sep_16_2055, sep_16_2055, sep_16_2055, sep_16_2055,
sep_17_2055, sep_17_2055, sep_17_2055, sep_17_2055, sep_18_2055, sep_18_2055, sep_18_2055, sep_18_2055,
sep_19_2055, sep_19_2055, sep_19_2055, sep_19_2055, sep_20_2055, sep_20_2055, sep_20_2055, sep_20_2055,
sep_21_2055, sep_21_2055, sep_21_2055, sep_21_2055, sep_22_2055, sep_22_2055, sep_22_2055, sep_22_2055,
sep_23_2055, sep_23_2055, sep_23_2055, sep_23_2055, sep_24_2055, sep_24_2055, sep_24_2055, sep_24_2055,
sep_25_2055, sep_25_2055, sep_25_2055, sep_25_2055, sep_26_2055, sep_26_2055, sep_26_2055, sep_26_2055,
sep_27_2055, sep_27_2055, sep_27_2055, sep_27_2055, sep_28_2055, sep_28_2055, sep_28_2055, sep_28_2055,
sep_29_2055, sep_29_2055, sep_29_2055, sep_29_2055, sep_30_2055, sep_30_2055, sep_30_2055, sep_30_2055,
oct_1_2055, oct_1_2055, oct_1_2055, oct_1_2055, oct_2_2055, oct_2_2055, oct_2_2055, oct_2_2055,
oct_3_2055, oct_3_2055, oct_3_2055, oct_3_2055, oct_4_2055, oct_4_2055, oct_4_2055, oct_4_2055,
oct_5_2055, oct_5_2055, oct_5_2055, oct_5_2055, oct_6_2055, oct_6_2055, oct_6_2055, oct_6_2055,
oct_7_2055, oct_7_2055, oct_7_2055, oct_7_2055, oct_8_2055, oct_8_2055, oct_8_2055, oct_8_2055,
oct_9_2055, oct_9_2055, oct_9_2055, oct_9_2055, oct_10_2055, oct_10_2055, oct_10_2055, oct_10_2055,
oct_11_2055, oct_11_2055, oct_11_2055, oct_11_2055, oct_12_2055, oct_12_2055, oct_12_2055, oct_12_2055,
oct_13_2055, oct_13_2055, oct_13_2055, oct_13_2055, oct_14_2055, oct_14_2055, oct_14_2055, oct_14_2055,
oct_15_2055, oct_15_2055, oct_15_2055, oct_15_2055, oct_16_2055, oct_16_2055, oct_16_2055, oct_16_2055,
oct_17_2055, oct_17_2055, oct_17_2055, oct_17_2055, oct_18_2055, oct_18_2055, oct_18_2055, oct_18_2055,
oct_19_2055, oct_19_2055, oct_19_2055, oct_19_2055, oct_20_2055, oct_20_2055, oct_20_2055, oct_20_2055,
oct_21_2055, oct_21_2055, oct_21_2055, oct_21_2055, oct_22_2055, oct_22_2055, oct_22_2055, oct_22_2055,
oct_23_2055, oct_23_2055, oct_23_2055, oct_23_2055, oct_24_2055, oct_24_2055, oct_24_2055, oct_24_2055,
oct_25_2055, oct_25_2055, oct_25_2055, oct_25_2055, oct_26_2055, oct_26_2055, oct_26_2055, oct_26_2055,
oct_27_2055, oct_27_2055, oct_27_2055, oct_27_2055, oct_28_2055, oct_28_2055, oct_28_2055, oct_28_2055,
oct_29_2055, oct_29_2055, oct_29_2055, oct_29_2055, oct_30_2055, oct_30_2055, oct_30_2055, oct_30_2055,
oct_31_2055, oct_31_2055, oct_31_2055, oct_31_2055,
nov_1_2055, nov_1_2055, nov_1_2055, nov_1_2055, nov_2_2055, nov_2_2055, nov_2_2055, nov_2_2055,
nov_3_2055, nov_3_2055, nov_3_2055, nov_3_2055, nov_4_2055, nov_4_2055, nov_4_2055, nov_4_2055,
nov_5_2055, nov_5_2055, nov_5_2055, nov_5_2055, nov_6_2055, nov_6_2055, nov_6_2055, nov_6_2055,
nov_7_2055, nov_7_2055, nov_7_2055, nov_7_2055, nov_8_2055, nov_8_2055, nov_8_2055, nov_8_2055,
nov_9_2055, nov_9_2055, nov_9_2055, nov_9_2055, nov_10_2055, nov_10_2055, nov_10_2055, nov_10_2055,
nov_11_2055, nov_11_2055, nov_11_2055, nov_11_2055, nov_12_2055, nov_12_2055, nov_12_2055, nov_12_2055,
nov_13_2055, nov_13_2055, nov_13_2055, nov_13_2055, nov_14_2055, nov_14_2055, nov_14_2055, nov_14_2055,
nov_15_2055, nov_15_2055, nov_15_2055, nov_15_2055, nov_16_2055, nov_16_2055, nov_16_2055, nov_16_2055,
nov_17_2055, nov_17_2055, nov_17_2055, nov_17_2055, nov_18_2055, nov_18_2055, nov_18_2055, nov_18_2055,
nov_19_2055, nov_19_2055, nov_19_2055, nov_19_2055, nov_20_2055, nov_20_2055, nov_20_2055, nov_20_2055,
nov_21_2055, nov_21_2055, nov_21_2055, nov_21_2055, nov_22_2055, nov_22_2055, nov_22_2055, nov_22_2055,
nov_23_2055, nov_23_2055, nov_23_2055, nov_23_2055, nov_24_2055, nov_24_2055, nov_24_2055, nov_24_2055,
nov_25_2055, nov_25_2055, nov_25_2055, nov_25_2055, nov_26_2055, nov_26_2055, nov_26_2055, nov_26_2055,
nov_27_2055, nov_27_2055, nov_27_2055, nov_27_2055, nov_28_2055, nov_28_2055, nov_28_2055, nov_28_2055,
nov_29_2055, nov_29_2055, nov_29_2055, nov_29_2055, nov_30_2055, nov_30_2055, nov_30_2055, nov_30_2055,
dec_1_2055, dec_1_2055, dec_1_2055, dec_1_2055, dec_2_2055, dec_2_2055, dec_2_2055, dec_2_2055,
dec_3_2055, dec_3_2055, dec_3_2055, dec_3_2055, dec_4_2055, dec_4_2055, dec_4_2055, dec_4_2055,
dec_5_2055, dec_5_2055, dec_5_2055, dec_5_2055, dec_6_2055, dec_6_2055, dec_6_2055, dec_6_2055,
dec_7_2055, dec_7_2055, dec_7_2055, dec_7_2055, dec_8_2055, dec_8_2055, dec_8_2055, dec_8_2055,
dec_9_2055, dec_9_2055, dec_9_2055, dec_9_2055, dec_10_2055, dec_10_2055, dec_10_2055, dec_10_2055,
dec_11_2055, dec_11_2055, dec_11_2055, dec_11_2055, dec_12_2055, dec_12_2055, dec_12_2055, dec_12_2055,
dec_13_2055, dec_13_2055, dec_13_2055, dec_13_2055, dec_14_2055, dec_14_2055, dec_14_2055, dec_14_2055,
dec_15_2055, dec_15_2055, dec_15_2055, dec_15_2055, dec_16_2055, dec_16_2055, dec_16_2055, dec_16_2055,
dec_17_2055, dec_17_2055, dec_17_2055, dec_17_2055, dec_18_2055, dec_18_2055, dec_18_2055, dec_18_2055,
dec_19_2055, dec_19_2055, dec_19_2055, dec_19_2055, dec_20_2055, dec_20_2055, dec_20_2055, dec_20_2055,
dec_21_2055, dec_21_2055, dec_21_2055, dec_21_2055, dec_22_2055, dec_22_2055, dec_22_2055, dec_22_2055,
dec_23_2055, dec_23_2055, dec_23_2055, dec_23_2055, dec_24_2055, dec_24_2055, dec_24_2055, dec_24_2055,
dec_25_2055, dec_25_2055, dec_25_2055, dec_25_2055, dec_26_2055, dec_26_2055, dec_26_2055, dec_26_2055,
dec_27_2055, dec_27_2055, dec_27_2055, dec_27_2055, dec_28_2055, dec_28_2055, dec_28_2055, dec_28_2055,
dec_29_2055, dec_29_2055, dec_29_2055, dec_29_2055, dec_30_2055, dec_30_2055, dec_30_2055, dec_30_2055,
dec_31_2055, dec_31_2055, dec_31_2055, dec_31_2055))



# Read-in TAS file and get time variable from it
file2 = xr.open_dataset('/home/oronald/model/boundaries/cmip6/low_ssp370/tas_6hrPlevPt_MPI-ESM-1-2-HAM_ssp370-lowNTCF_r1i1p1f1_gn_205501010600-205601010000.nc')
tas = file2['tas']
#print(file2)
#print("===="*70)


modified_ts = xr.Dataset(data_vars=dict(ts=(["time", "lat", "lon"], ts_6hr_stack), 
                                        lat_bnds=(["lat", "bnds"], file2.lat_bnds.data),
                                        lon_bnds=(["lon", "bnds"], file2.lon_bnds.data)),
                         coords=dict(time=(["time"], file2.time.data),
                                     lat=(["lat"], file2.lat.data),
                                     lon=(["lon"], file2.lon.data)), attrs=file1.attrs)

print(modified_ts)

modified_ts.to_netcdf('/home/oronald/model/boundaries/cmip6/low_ssp370/ts_6hrPlevPt_MPI-ESM-1-2-HAM_ssp370-lowNTCF_r1i1p1f1_gn_205501010600-205601010000.nc')

