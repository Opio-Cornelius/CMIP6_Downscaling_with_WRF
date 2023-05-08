# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 04:42:11 2023

@author: opio
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import pymannkendall as mk
import matplotlib as mpl


# Read-in regionl file
file_region = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/precp_NTCF_mitigation.nc')

# Selection of countries

# Uganda
file_ug = file_region.sel(lat = slice(-1.5, 4.3), lon = slice(29.5, 35))

# Kenya
file_ke = file_region.sel(lat = slice(-4.6, 5), lon = slice(33.7, 42))

# Tanzania
file_tz = file_region.sel(lat = slice(-11.8, -1.1), lon = slice(30, 40))

# Rwanda
file_rw = file_region.sel(lat = slice(-2.8, -1.01), lon = slice(28.8, 30.9))

# Burundi
file_br = file_region.sel(lat = slice(-4.5, -2.3), lon = slice(28.9, 30.8))

# Plot to verify selected region
#fig = plt.figure(figsize=(8,4))#, dpi=500)
#ax = plt.subplot(projection=ccrs.PlateCarree())
#plt.pcolormesh(file_ug['lon'], file_ug['lat'], file_ug['precp_mitigation'][0,:,:], cmap='ocean_r')
#ax.coastlines(resolution='10m', color='black', linewidth=0.9)
#ax.add_feature(cfeature.BORDERS, linewidth=1.2)
#plt.show()


" Uganda "
# Calculate annual mean
precp_mit_annual_ug = file_ug['precp_mitigation'].groupby('time.year').mean('time')
annual_series_ug = precp_mit_annual_ug.mean(axis=1).mean(axis=1)/3.5

# Calculate season_ugal means
season_ug = file_ug['precp_mitigation'].groupby('time.season')

precp_djf_ug = season_ug['DJF'].groupby('time.year').mean('time')
djf_series_ug = precp_djf_ug.mean(axis=1).mean(axis=1)/3.5

precp_mam_ug = season_ug['MAM'].groupby('time.year').mean('time')
mam_series_ug = precp_mam_ug.mean(axis=1).mean(axis=1)/3.5

precp_jja_ug = season_ug['JJA'].groupby('time.year').mean('time')
jja_series_ug = precp_jja_ug.mean(axis=1).mean(axis=1)/3.5

precp_son_ug = season_ug['SON'].groupby('time.year').mean('time')
son_series_ug = precp_son_ug.mean(axis=1).mean(axis=1)/3.5



" Kenya "
# Calculate annual mean
precp_mit_annual_ke = file_ke['precp_mitigation'].groupby('time.year').mean('time')
annual_series_ke = precp_mit_annual_ke.mean(axis=1).mean(axis=1)/3.5

# Calculate season_keal means
season_ke = file_ke['precp_mitigation'].groupby('time.season')

precp_djf_ke = season_ke['DJF'].groupby('time.year').mean('time')
djf_series_ke = precp_djf_ke.mean(axis=1).mean(axis=1)/3.5

precp_mam_ke = season_ke['MAM'].groupby('time.year').mean('time')
mam_series_ke = precp_mam_ke.mean(axis=1).mean(axis=1)/3.5

precp_jja_ke = season_ke['JJA'].groupby('time.year').mean('time')
jja_series_ke = precp_jja_ke.mean(axis=1).mean(axis=1)/3.5

precp_son_ke = season_ke['SON'].groupby('time.year').mean('time')
son_series_ke = precp_son_ke.mean(axis=1).mean(axis=1)/3.5



" Tanzania "
# Calculate annual mean
precp_mit_annual_tz = file_tz['precp_mitigation'].groupby('time.year').mean('time')
annual_series_tz = precp_mit_annual_tz.mean(axis=1).mean(axis=1)/3.5

# Calculate season_tzal means
season_tz = file_tz['precp_mitigation'].groupby('time.season')

precp_djf_tz = season_tz['DJF'].groupby('time.year').mean('time')
djf_series_tz = precp_djf_tz.mean(axis=1).mean(axis=1)/3.5

precp_mam_tz = season_tz['MAM'].groupby('time.year').mean('time')
mam_series_tz = precp_mam_tz.mean(axis=1).mean(axis=1)/3.5

precp_jja_tz = season_tz['JJA'].groupby('time.year').mean('time')
jja_series_tz = precp_jja_tz.mean(axis=1).mean(axis=1)/3.5

precp_son_tz = season_tz['SON'].groupby('time.year').mean('time')
son_series_tz = precp_son_tz.mean(axis=1).mean(axis=1)/3.5



" Rwanda "
# Calculate annual mean
precp_mit_annual_rw = file_rw['precp_mitigation'].groupby('time.year').mean('time')
annual_series_rw = precp_mit_annual_rw.mean(axis=1).mean(axis=1)/3.5

# Calculate season_rwal means
season_rw = file_rw['precp_mitigation'].groupby('time.season')

precp_djf_rw = season_rw['DJF'].groupby('time.year').mean('time')
djf_series_rw = precp_djf_rw.mean(axis=1).mean(axis=1)/3.5

precp_mam_rw = season_rw['MAM'].groupby('time.year').mean('time')
mam_series_rw = precp_mam_rw.mean(axis=1).mean(axis=1)/3.5

precp_jja_rw = season_rw['JJA'].groupby('time.year').mean('time')
jja_series_rw = precp_jja_rw.mean(axis=1).mean(axis=1)/3.5

precp_son_rw = season_rw['SON'].groupby('time.year').mean('time')
son_series_rw = precp_son_rw.mean(axis=1).mean(axis=1)/3.5



" Burundi "
# Calculate annual mean
precp_mit_annual_br = file_br['precp_mitigation'].groupby('time.year').mean('time')
annual_series_br = precp_mit_annual_br.mean(axis=1).mean(axis=1)/3.5

# Calculate season_bral means
season_br = file_br['precp_mitigation'].groupby('time.season')

precp_djf_br = season_br['DJF'].groupby('time.year').mean('time')
djf_series_br = precp_djf_br.mean(axis=1).mean(axis=1)/3.5

precp_mam_br = season_br['MAM'].groupby('time.year').mean('time')
mam_series_br = precp_mam_br.mean(axis=1).mean(axis=1)/3.5

precp_jja_br = season_br['JJA'].groupby('time.year').mean('time')
jja_series_br = precp_jja_br.mean(axis=1).mean(axis=1)/3.5

precp_son_br = season_br['SON'].groupby('time.year').mean('time')
son_series_br = precp_son_br.mean(axis=1).mean(axis=1)/3.5



# Plot
fig = plt.subplots(figsize=(14, 12), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.4, wspace=0.25)

ax = plt.subplot(3,2,1)
plt.plot(precp_mit_annual_ug['year'], djf_series_ug, label='DJF', color='orange')
plt.plot(precp_mit_annual_ug['year'], mam_series_ug, label='MAM', color='blue')
plt.plot(precp_mit_annual_ug['year'], jja_series_ug, label='JJA', color='crimson')
plt.plot(precp_mit_annual_ug['year'], son_series_ug, label='SON', color='green')
plt.plot(precp_mit_annual_ug['year'], annual_series_ug, label='Annual', color='black', linewidth=4)
#plt.legend(ncol=4, frameon=False)
plt.ylim(-30, 30)
plt.title('Uganda')
plt.ylabel('Precipitation (mm $\mathregular{month^{-1}}$)')


ax = plt.subplot(3,2,2)
plt.plot(precp_mit_annual_ke['year'], djf_series_ke, label='DJF', color='orange')
plt.plot(precp_mit_annual_ke['year'], mam_series_ke, label='MAM', color='blue')
plt.plot(precp_mit_annual_ke['year'], jja_series_ke, label='JJA', color='crimson')
plt.plot(precp_mit_annual_ke['year'], son_series_ke, label='SON', color='green')
plt.plot(precp_mit_annual_ke['year'], annual_series_ke, label='Annual', color='black', linewidth=4)
#plt.legend(ncol=4, frameon=False)
plt.ylim(-30, 30)
plt.title('Kenya')
plt.ylabel('Precipitation (mm $\mathregular{month^{-1}}$)')


ax = plt.subplot(3,2,3)
plt.plot(precp_mit_annual_tz['year'], djf_series_tz, label='DJF', color='orange')
plt.plot(precp_mit_annual_tz['year'], mam_series_tz, label='MAM', color='blue')
plt.plot(precp_mit_annual_tz['year'], jja_series_tz, label='JJA', color='crimson')
plt.plot(precp_mit_annual_tz['year'], son_series_tz, label='SON', color='green')
plt.plot(precp_mit_annual_tz['year'], annual_series_tz, label='Annual', color='black', linewidth=4)
#plt.legend(ncol=4, frameon=False)
plt.ylim(-30, 30)
plt.title('Tanzania')
plt.ylabel('Precipitation (mm $\mathregular{month^{-1}}$)')



ax = plt.subplot(3,2,4)
plt.plot(precp_mit_annual_rw['year'], djf_series_rw, label='DJF', color='orange')
plt.plot(precp_mit_annual_rw['year'], mam_series_rw, label='MAM', color='blue')
plt.plot(precp_mit_annual_rw['year'], jja_series_rw, label='JJA', color='crimson')
plt.plot(precp_mit_annual_rw['year'], son_series_rw, label='SON', color='green')
plt.plot(precp_mit_annual_rw['year'], annual_series_rw, label='Annual', color='black', linewidth=4)
#plt.legend(ncol=4, frameon=False)
plt.ylim(-30, 30)
plt.title('Rwanda')
plt.ylabel('Precipitation (mm $\mathregular{month^{-1}}$)')



ax = plt.subplot(3,2,5)
h1=plt.plot(precp_mit_annual_br['year'], djf_series_br, label='DJF', color='orange')
h2=plt.plot(precp_mit_annual_br['year'], mam_series_br, label='MAM', color='blue')
h3=plt.plot(precp_mit_annual_br['year'], jja_series_br, label='JJA', color='crimson')
h4=plt.plot(precp_mit_annual_br['year'], son_series_br, label='SON', color='green')
h5=plt.plot(precp_mit_annual_br['year'], annual_series_br, label='Annual', color='black', linewidth=4)
#plt.legend(ncol=4, frameon=False)
plt.ylim(-30, 30)
plt.title('Burundi')
plt.ylabel('Precipitation (mm $\mathregular{month^{-1}}$)')
labels = ['DJF', 'MAM', 'JJA', 'SON', 'Annual']
plt.legend([h1, h2, h3, h4, h5], labels=labels, loc='upper left', 
           bbox_to_anchor=(1.22, 1.04), ncol=2)


# Perform Mann-Kendall trend test
#mk.original_test(annual_series)
#mk.original_test(djf_series)
#mk.original_test(mam_series)
#mk.original_test(jja_series)
#mk.original_test(son_series)
