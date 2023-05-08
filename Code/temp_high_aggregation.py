# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:34:53 2023

@author: opio
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr


# Import data files as monthly means

" SSP3-7.0 "

high_jan_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_1_jan.npy')
high_feb_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_2_feb.npy')
high_mar_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_3_mar.npy')
high_apr_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_4_apr.npy')
high_may_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_5_may.npy')
high_june_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_6_june.npy')
high_july_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_7_july.npy')
high_aug_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_8_aug.npy')
high_sep_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_9_sep.npy')
high_oct_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_10_oct.npy')
high_nov_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_11_nov.npy')
high_dec_2021 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2021/high_2021_12_dec.npy')


high_jan_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_1_jan.npy')
high_feb_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_2_feb.npy')
high_mar_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_3_mar.npy')
high_apr_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_4_apr.npy')
high_may_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_5_may.npy')
high_june_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_6_june.npy')
high_july_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_7_july.npy')
high_aug_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_8_aug.npy')
high_sep_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_9_sep.npy')
high_oct_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_10_oct.npy')
high_nov_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_11_nov.npy')
high_dec_2022 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2022/high_2022_12_dec.npy')


high_jan_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_1_jan.npy')
high_feb_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_2_feb.npy')
high_mar_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_3_mar.npy')
high_apr_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_4_apr.npy')
high_may_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_5_may.npy')
high_june_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_6_june.npy')
high_july_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_7_july.npy')
high_aug_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_8_aug.npy')
high_sep_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_9_sep.npy')
high_oct_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_10_oct.npy')
high_nov_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_11_nov.npy')
high_dec_2023 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2023/high_2023_12_dec.npy')


high_jan_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_1_jan.npy')
high_feb_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_2_feb.npy')
high_mar_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_3_mar.npy')
high_apr_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_4_apr.npy')
high_may_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_5_may.npy')
high_june_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_6_june.npy')
high_july_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_7_july.npy')
high_aug_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_8_aug.npy')
high_sep_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_9_sep.npy')
high_oct_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_10_oct.npy')
high_nov_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_11_nov.npy')
high_dec_2024 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2024/high_2024_12_dec.npy')


high_jan_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_1_jan.npy')
high_feb_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_2_feb.npy')
high_mar_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_3_mar.npy')
high_apr_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_4_apr.npy')
high_may_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_5_may.npy')
high_june_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_6_june.npy')
high_july_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_7_july.npy')
high_aug_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_8_aug.npy')
high_sep_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_9_sep.npy')
high_oct_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_10_oct.npy')
high_nov_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_11_nov.npy')
high_dec_2025 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2025/high_2025_12_dec.npy')


high_jan_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_1_jan.npy')
high_feb_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_2_feb.npy')
high_mar_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_3_mar.npy')
high_apr_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_4_apr.npy')
high_may_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_5_may.npy')
high_june_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_6_june.npy')
high_july_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_7_july.npy')
high_aug_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_8_aug.npy')
high_sep_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_9_sep.npy')
high_oct_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_10_oct.npy')
high_nov_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_11_nov.npy')
high_dec_2026 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2026/high_2026_12_dec.npy')


high_jan_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_1_jan.npy')
high_feb_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_2_feb.npy')
high_mar_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_3_mar.npy')
high_apr_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_4_apr.npy')
high_may_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_5_may.npy')
high_june_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_6_june.npy')
high_july_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_7_july.npy')
high_aug_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_8_aug.npy')
high_sep_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_9_sep.npy')
high_oct_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_10_oct.npy')
high_nov_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_11_nov.npy')
high_dec_2027 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2027/high_2027_12_dec.npy')


high_jan_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_1_jan.npy')
high_feb_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_2_feb.npy')
high_mar_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_3_mar.npy')
high_apr_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_4_apr.npy')
high_may_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_5_may.npy')
high_june_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_6_june.npy')
high_july_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_7_july.npy')
high_aug_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_8_aug.npy')
high_sep_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_9_sep.npy')
high_oct_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_10_oct.npy')
high_nov_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_11_nov.npy')
high_dec_2028 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2028/high_2028_12_dec.npy')


high_jan_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_1_jan.npy')
high_feb_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_2_feb.npy')
high_mar_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_3_mar.npy')
high_apr_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_4_apr.npy')
high_may_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_5_may.npy')
high_june_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_6_june.npy')
high_july_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_7_july.npy')
high_aug_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_8_aug.npy')
high_sep_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_9_sep.npy')
high_oct_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_10_oct.npy')
high_nov_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_11_nov.npy')
high_dec_2029 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2029/high_2029_12_dec.npy')


high_jan_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_1_jan.npy')
high_feb_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_2_feb.npy')
high_mar_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_3_mar.npy')
high_apr_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_4_apr.npy')
high_may_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_5_may.npy')
high_june_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_6_june.npy')
high_july_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_7_july.npy')
high_aug_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_8_aug.npy')
high_sep_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_9_sep.npy')
high_oct_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_10_oct.npy')
high_nov_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_11_nov.npy')
high_dec_2030 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2030/high_2030_12_dec.npy')


high_jan_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_1_jan.npy')
high_feb_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_2_feb.npy')
high_mar_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_3_mar.npy')
high_apr_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_4_apr.npy')
high_may_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_5_may.npy')
high_june_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_6_june.npy')
high_july_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_7_july.npy')
high_aug_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_8_aug.npy')
high_sep_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_9_sep.npy')
high_oct_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_10_oct.npy')
high_nov_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_11_nov.npy')
high_dec_2031 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2031/high_2031_12_dec.npy')


high_jan_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_1_jan.npy')
high_feb_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_2_feb.npy')
high_mar_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_3_mar.npy')
high_apr_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_4_apr.npy')
high_may_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_5_may.npy')
high_june_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_6_june.npy')
high_july_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_7_july.npy')
high_aug_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_8_aug.npy')
high_sep_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_9_sep.npy')
high_oct_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_10_oct.npy')
high_nov_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_11_nov.npy')
high_dec_2032 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2032/high_2032_12_dec.npy')


high_jan_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_1_jan.npy')
high_feb_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_2_feb.npy')
high_mar_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_3_mar.npy')
high_apr_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_4_apr.npy')
high_may_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_5_may.npy')
high_june_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_6_june.npy')
high_july_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_7_july.npy')
high_aug_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_8_aug.npy')
high_sep_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_9_sep.npy')
high_oct_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_10_oct.npy')
high_nov_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_11_nov.npy')
high_dec_2033 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2033/high_2033_12_dec.npy')


high_jan_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_1_jan.npy')
high_feb_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_2_feb.npy')
high_mar_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_3_mar.npy')
high_apr_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_4_apr.npy')
high_may_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_5_may.npy')
high_june_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_6_june.npy')
high_july_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_7_july.npy')
high_aug_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_8_aug.npy')
high_sep_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_9_sep.npy')
high_oct_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_10_oct.npy')
high_nov_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_11_nov.npy')
high_dec_2034 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2034/high_2034_12_dec.npy')


high_jan_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_1_jan.npy')
high_feb_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_2_feb.npy')
high_mar_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_3_mar.npy')
high_apr_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_4_apr.npy')
high_may_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_5_may.npy')
high_june_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_6_june.npy')
high_july_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_7_july.npy')
high_aug_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_8_aug.npy')
high_sep_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_9_sep.npy')
high_oct_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_10_oct.npy')
high_nov_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_11_nov.npy')
high_dec_2035 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2035/high_2035_12_dec.npy')


high_jan_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_1_jan.npy')
high_feb_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_2_feb.npy')
high_mar_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_3_mar.npy')
high_apr_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_4_apr.npy')
high_may_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_5_may.npy')
high_june_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_6_june.npy')
high_july_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_7_july.npy')
high_aug_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_8_aug.npy')
high_sep_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_9_sep.npy')
high_oct_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_10_oct.npy')
high_nov_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_11_nov.npy')
high_dec_2036 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2036/high_2036_12_dec.npy')


high_jan_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_1_jan.npy')
high_feb_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_2_feb.npy')
high_mar_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_3_mar.npy')
high_apr_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_4_apr.npy')
high_may_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_5_may.npy')
high_june_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_6_june.npy')
high_july_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_7_july.npy')
high_aug_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_8_aug.npy')
high_sep_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_9_sep.npy')
high_oct_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_10_oct.npy')
high_nov_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_11_nov.npy')
high_dec_2037 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2037/high_2037_12_dec.npy')


high_jan_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_1_jan.npy')
high_feb_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_2_feb.npy')
high_mar_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_3_mar.npy')
high_apr_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_4_apr.npy')
high_may_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_5_may.npy')
high_june_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_6_june.npy')
high_july_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_7_july.npy')
high_aug_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_8_aug.npy')
high_sep_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_9_sep.npy')
high_oct_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_10_oct.npy')
high_nov_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_11_nov.npy')
high_dec_2038 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2038/high_2038_12_dec.npy')


high_jan_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_1_jan.npy')
high_feb_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_2_feb.npy')
high_mar_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_3_mar.npy')
high_apr_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_4_apr.npy')
high_may_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_5_may.npy')
high_june_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_6_june.npy')
high_july_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_7_july.npy')
high_aug_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_8_aug.npy')
high_sep_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_9_sep.npy')
high_oct_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_10_oct.npy')
high_nov_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_11_nov.npy')
high_dec_2039 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2039/high_2039_12_dec.npy')


high_jan_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_1_jan.npy')
high_feb_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_2_feb.npy')
high_mar_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_3_mar.npy')
high_apr_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_4_apr.npy')
high_may_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_5_may.npy')
high_june_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_6_june.npy')
high_july_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_7_july.npy')
high_aug_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_8_aug.npy')
high_sep_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_9_sep.npy')
high_oct_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_10_oct.npy')
high_nov_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_11_nov.npy')
high_dec_2040 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2040/high_2040_12_dec.npy')


high_jan_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_1_jan.npy')
high_feb_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_2_feb.npy')
high_mar_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_3_mar.npy')
high_apr_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_4_apr.npy')
high_may_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_5_may.npy')
high_june_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_6_june.npy')
high_july_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_7_july.npy')
high_aug_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_8_aug.npy')
high_sep_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_9_sep.npy')
high_oct_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_10_oct.npy')
high_nov_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_11_nov.npy')
high_dec_2041 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2041/high_2041_12_dec.npy')


high_jan_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_1_jan.npy')
high_feb_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_2_feb.npy')
high_mar_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_3_mar.npy')
high_apr_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_4_apr.npy')
high_may_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_5_may.npy')
high_june_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_6_june.npy')
high_july_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_7_july.npy')
high_aug_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_8_aug.npy')
high_sep_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_9_sep.npy')
high_oct_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_10_oct.npy')
high_nov_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_11_nov.npy')
high_dec_2042 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2042/high_2042_12_dec.npy')


high_jan_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_1_jan.npy')
high_feb_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_2_feb.npy')
high_mar_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_3_mar.npy')
high_apr_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_4_apr.npy')
high_may_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_5_may.npy')
high_june_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_6_june.npy')
high_july_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_7_july.npy')
high_aug_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_8_aug.npy')
high_sep_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_9_sep.npy')
high_oct_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_10_oct.npy')
high_nov_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_11_nov.npy')
high_dec_2043 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2043/high_2043_12_dec.npy')


high_jan_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_1_jan.npy')
high_feb_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_2_feb.npy')
high_mar_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_3_mar.npy')
high_apr_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_4_apr.npy')
high_may_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_5_may.npy')
high_june_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_6_june.npy')
high_july_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_7_july.npy')
high_aug_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_8_aug.npy')
high_sep_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_9_sep.npy')
high_oct_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_10_oct.npy')
high_nov_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_11_nov.npy')
high_dec_2044 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2044/high_2044_12_dec.npy')


high_jan_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_1_jan.npy')
high_feb_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_2_feb.npy')
high_mar_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_3_mar.npy')
high_apr_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_4_apr.npy')
high_may_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_5_may.npy')
high_june_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_6_june.npy')
high_july_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_7_july.npy')
high_aug_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_8_aug.npy')
high_sep_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_9_sep.npy')
high_oct_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_10_oct.npy')
high_nov_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_11_nov.npy')
high_dec_2045 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2045/high_2045_12_dec.npy')


high_jan_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_1_jan.npy')
high_feb_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_2_feb.npy')
high_mar_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_3_mar.npy')
high_apr_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_4_apr.npy')
high_may_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_5_may.npy')
high_june_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_6_june.npy')
high_july_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_7_july.npy')
high_aug_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_8_aug.npy')
high_sep_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_9_sep.npy')
high_oct_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_10_oct.npy')
high_nov_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_11_nov.npy')
high_dec_2046 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2046/high_2046_12_dec.npy')


high_jan_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_1_jan.npy')
high_feb_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_2_feb.npy')
high_mar_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_3_mar.npy')
high_apr_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_4_apr.npy')
high_may_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_5_may.npy')
high_june_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_6_june.npy')
high_july_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_7_july.npy')
high_aug_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_8_aug.npy')
high_sep_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_9_sep.npy')
high_oct_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_10_oct.npy')
high_nov_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_11_nov.npy')
high_dec_2047 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2047/high_2047_12_dec.npy')


high_jan_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_1_jan.npy')
high_feb_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_2_feb.npy')
high_mar_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_3_mar.npy')
high_apr_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_4_apr.npy')
high_may_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_5_may.npy')
high_june_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_6_june.npy')
high_july_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_7_july.npy')
high_aug_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_8_aug.npy')
high_sep_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_9_sep.npy')
high_oct_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_10_oct.npy')
high_nov_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_11_nov.npy')
high_dec_2048 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2048/high_2048_12_dec.npy')


high_jan_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_1_jan.npy')
high_feb_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_2_feb.npy')
high_mar_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_3_mar.npy')
high_apr_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_4_apr.npy')
high_may_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_5_may.npy')
high_june_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_6_june.npy')
high_july_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_7_july.npy')
high_aug_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_8_aug.npy')
high_sep_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_9_sep.npy')
high_oct_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_10_oct.npy')
high_nov_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_11_nov.npy')
high_dec_2049 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2049/high_2049_12_dec.npy')


high_jan_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_1_jan.npy')
high_feb_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_2_feb.npy')
high_mar_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_3_mar.npy')
high_apr_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_4_apr.npy')
high_may_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_5_may.npy')
high_june_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_6_june.npy')
high_july_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_7_july.npy')
high_aug_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_8_aug.npy')
high_sep_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_9_sep.npy')
high_oct_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_10_oct.npy')
high_nov_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_11_nov.npy')
high_dec_2050 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2050/high_2050_12_dec.npy')


high_jan_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_1_jan.npy')
high_feb_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_2_feb.npy')
high_mar_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_3_mar.npy')
high_apr_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_4_apr.npy')
high_may_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_5_may.npy')
high_june_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_6_june.npy')
high_july_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_7_july.npy')
high_aug_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_8_aug.npy')
high_sep_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_9_sep.npy')
high_oct_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_10_oct.npy')
high_nov_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_11_nov.npy')
high_dec_2051 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2051/high_2051_12_dec.npy')


high_jan_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_1_jan.npy')
high_feb_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_2_feb.npy')
high_mar_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_3_mar.npy')
high_apr_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_4_apr.npy')
high_may_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_5_may.npy')
high_june_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_6_june.npy')
high_july_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_7_july.npy')
high_aug_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_8_aug.npy')
high_sep_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_9_sep.npy')
high_oct_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_10_oct.npy')
high_nov_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_11_nov.npy')
high_dec_2052 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2052/high_2052_12_dec.npy')


high_jan_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_1_jan.npy')
high_feb_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_2_feb.npy')
high_mar_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_3_mar.npy')
high_apr_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_4_apr.npy')
high_may_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_5_may.npy')
high_june_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_6_june.npy')
high_july_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_7_july.npy')
high_aug_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_8_aug.npy')
high_sep_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_9_sep.npy')
high_oct_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_10_oct.npy')
high_nov_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_11_nov.npy')
high_dec_2053 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2053/high_2053_12_dec.npy')


high_jan_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_1_jan.npy')
high_feb_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_2_feb.npy')
high_mar_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_3_mar.npy')
high_apr_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_4_apr.npy')
high_may_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_5_may.npy')
high_june_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_6_june.npy')
high_july_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_7_july.npy')
high_aug_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_8_aug.npy')
high_sep_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_9_sep.npy')
high_oct_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_10_oct.npy')
high_nov_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_11_nov.npy')
high_dec_2054 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2054/high_2054_12_dec.npy')


high_jan_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_1_jan.npy')
high_feb_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_2_feb.npy')
high_mar_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_3_mar.npy')
high_apr_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_4_apr.npy')
high_may_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_5_may.npy')
high_june_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_6_june.npy')
high_july_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_7_july.npy')
high_aug_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_8_aug.npy')
high_sep_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_9_sep.npy')
high_oct_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_10_oct.npy')
high_nov_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_11_nov.npy')
high_dec_2055 = np.load('C:/python_work/phd/paper5/real_work/phase2/temp_high/2055/high_2055_12_dec.npy')



high_temp = np.stack((high_jan_2021, high_feb_2021, high_mar_2021, high_apr_2021, high_may_2021, high_june_2021,
                      high_july_2021, high_aug_2021, high_sep_2021, high_oct_2021, high_nov_2021, high_dec_2021,
                      high_jan_2022, high_feb_2022, high_mar_2022, high_apr_2022, high_may_2022, high_june_2022,
                      high_july_2022, high_aug_2022, high_sep_2022, high_oct_2022, high_nov_2022, high_dec_2022,
                      high_jan_2023, high_feb_2023, high_mar_2023, high_apr_2023, high_may_2023, high_june_2023,
                      high_july_2023, high_aug_2023, high_sep_2023, high_oct_2023, high_nov_2023, high_dec_2023,
                      high_jan_2024, high_feb_2024, high_mar_2024, high_apr_2024, high_may_2024, high_june_2024,
                      high_july_2024, high_aug_2024, high_sep_2024, high_oct_2024, high_nov_2024, high_dec_2024,
                      high_jan_2025, high_feb_2025, high_mar_2025, high_apr_2025, high_may_2025, high_june_2025,
                      high_july_2025, high_aug_2025, high_sep_2025, high_oct_2025, high_nov_2025, high_dec_2025,
                      high_jan_2026, high_feb_2026, high_mar_2026, high_apr_2026, high_may_2026, high_june_2026,
                      high_july_2026, high_aug_2026, high_sep_2026, high_oct_2026, high_nov_2026, high_dec_2026,
                      high_jan_2027, high_feb_2027, high_mar_2027, high_apr_2027, high_may_2027, high_june_2027,
                      high_july_2027, high_aug_2027, high_sep_2027, high_oct_2027, high_nov_2027, high_dec_2027,
                      high_jan_2028, high_feb_2028, high_mar_2028, high_apr_2028, high_may_2028, high_june_2028,
                      high_july_2028, high_aug_2028, high_sep_2028, high_oct_2028, high_nov_2028, high_dec_2028,
                      high_jan_2029, high_feb_2029, high_mar_2029, high_apr_2029, high_may_2029, high_june_2029,
                      high_july_2029, high_aug_2029, high_sep_2029, high_oct_2029, high_nov_2029, high_dec_2029,
                      high_jan_2030, high_feb_2030, high_mar_2030, high_apr_2030, high_may_2030, high_june_2030,
                      high_july_2030, high_aug_2030, high_sep_2030, high_oct_2030, high_nov_2030, high_dec_2030,
                      high_jan_2031, high_feb_2031, high_mar_2031, high_apr_2031, high_may_2031, high_june_2031,
                      high_july_2031, high_aug_2031, high_sep_2031, high_oct_2031, high_nov_2031, high_dec_2031,
                      high_jan_2032, high_feb_2032, high_mar_2032, high_apr_2032, high_may_2032, high_june_2032,
                      high_july_2032, high_aug_2032, high_sep_2032, high_oct_2032, high_nov_2032, high_dec_2032,
                      high_jan_2033, high_feb_2033, high_mar_2033, high_apr_2033, high_may_2033, high_june_2033,
                      high_july_2033, high_aug_2033, high_sep_2033, high_oct_2033, high_nov_2033, high_dec_2033,
                      high_jan_2034, high_feb_2034, high_mar_2034, high_apr_2034, high_may_2034, high_june_2034,
                      high_july_2034, high_aug_2034, high_sep_2034, high_oct_2034, high_nov_2034, high_dec_2034,
                      high_jan_2035, high_feb_2035, high_mar_2035, high_apr_2035, high_may_2035, high_june_2035,
                      high_july_2035, high_aug_2035, high_sep_2035, high_oct_2035, high_nov_2035, high_dec_2035,
                      high_jan_2036, high_feb_2036, high_mar_2036, high_apr_2036, high_may_2036, high_june_2036,
                      high_july_2036, high_aug_2036, high_sep_2036, high_oct_2036, high_nov_2036, high_dec_2036,
                      high_jan_2037, high_feb_2037, high_mar_2037, high_apr_2037, high_may_2037, high_june_2037,
                      high_july_2037, high_aug_2037, high_sep_2037, high_oct_2037, high_nov_2037, high_dec_2037,
                      high_jan_2038, high_feb_2038, high_mar_2038, high_apr_2038, high_may_2038, high_june_2038,
                      high_july_2038, high_aug_2038, high_sep_2038, high_oct_2038, high_nov_2038, high_dec_2038,
                      high_jan_2039, high_feb_2039, high_mar_2039, high_apr_2039, high_may_2039, high_june_2039,
                      high_july_2039, high_aug_2039, high_sep_2039, high_oct_2039, high_nov_2039, high_dec_2039,
                      high_jan_2040, high_feb_2040, high_mar_2040, high_apr_2040, high_may_2040, high_june_2040,
                      high_july_2040, high_aug_2040, high_sep_2040, high_oct_2040, high_nov_2040, high_dec_2040,
                      high_jan_2041, high_feb_2041, high_mar_2041, high_apr_2041, high_may_2041, high_june_2041,
                      high_july_2041, high_aug_2041, high_sep_2041, high_oct_2041, high_nov_2041, high_dec_2041,
                      high_jan_2042, high_feb_2042, high_mar_2042, high_apr_2042, high_may_2042, high_june_2042,
                      high_july_2042, high_aug_2042, high_sep_2042, high_oct_2042, high_nov_2042, high_dec_2042,
                      high_jan_2043, high_feb_2043, high_mar_2043, high_apr_2043, high_may_2043, high_june_2043,
                      high_july_2043, high_aug_2043, high_sep_2043, high_oct_2043, high_nov_2043, high_dec_2043,
                      high_jan_2044, high_feb_2044, high_mar_2044, high_apr_2044, high_may_2044, high_june_2044,
                      high_july_2044, high_aug_2044, high_sep_2044, high_oct_2044, high_nov_2044, high_dec_2044,
                      high_jan_2045, high_feb_2045, high_mar_2045, high_apr_2045, high_may_2045, high_june_2045,
                      high_july_2045, high_aug_2045, high_sep_2045, high_oct_2045, high_nov_2045, high_dec_2045,
                      high_jan_2046, high_feb_2046, high_mar_2046, high_apr_2046, high_may_2046, high_june_2046,
                      high_july_2046, high_aug_2046, high_sep_2046, high_oct_2046, high_nov_2046, high_dec_2046,
                      high_jan_2047, high_feb_2047, high_mar_2047, high_apr_2047, high_may_2047, high_june_2047,
                      high_july_2047, high_aug_2047, high_sep_2047, high_oct_2047, high_nov_2047, high_dec_2047,
                      high_jan_2048, high_feb_2048, high_mar_2048, high_apr_2048, high_may_2048, high_june_2048,
                      high_july_2048, high_aug_2048, high_sep_2048, high_oct_2048, high_nov_2048, high_dec_2048,
                      high_jan_2049, high_feb_2049, high_mar_2049, high_apr_2049, high_may_2049, high_june_2049,
                      high_july_2049, high_aug_2049, high_sep_2049, high_oct_2049, high_nov_2049, high_dec_2049,
                      high_jan_2050, high_feb_2050, high_mar_2050, high_apr_2050, high_may_2050, high_june_2050,
                      high_july_2050, high_aug_2050, high_sep_2050, high_oct_2050, high_nov_2050, high_dec_2050,
                      high_jan_2051, high_feb_2051, high_mar_2051, high_apr_2051, high_may_2051, high_june_2051,
                      high_july_2051, high_aug_2051, high_sep_2051, high_oct_2051, high_nov_2051, high_dec_2051,
                      high_jan_2052, high_feb_2052, high_mar_2052, high_apr_2052, high_may_2052, high_june_2052,
                      high_july_2052, high_aug_2052, high_sep_2052, high_oct_2052, high_nov_2052, high_dec_2052,
                      high_jan_2053, high_feb_2053, high_mar_2053, high_apr_2053, high_may_2053, high_june_2053,
                      high_july_2053, high_aug_2053, high_sep_2053, high_oct_2053, high_nov_2053, high_dec_2053,
                      high_jan_2054, high_feb_2054, high_mar_2054, high_apr_2054, high_may_2054, high_june_2054,
                      high_july_2054, high_aug_2054, high_sep_2054, high_oct_2054, high_nov_2054, high_dec_2054,
                      high_jan_2055, high_feb_2055, high_mar_2055, high_apr_2055, high_may_2055, high_june_2055,
                      high_july_2055, high_aug_2055, high_sep_2055, high_oct_2055, high_nov_2055, high_dec_2055))


created_time = np.arange(np.datetime64("2021-01-01"), np.datetime64("2056-01-01"),
                         np.timedelta64(1, 'M'), dtype='datetime64[M]').astype('datetime64[D]')

final_temp_file = xr.Dataset(data_vars=dict(temp_ssp370=(['time', 'lat', 'lon'], high_temp)),
                             coords=({'lat': (['lat'], np.arange(-13.000000,7.000000, 0.21)),
                                                  'lon': (['lon'], np.arange(27.500000,43.500000, 0.20)),
                                                  'time': created_time}))

final_temp_file.to_netcdf('C:/python_work/phd/paper5/real_work/phase2/temp_ssp370.nc')