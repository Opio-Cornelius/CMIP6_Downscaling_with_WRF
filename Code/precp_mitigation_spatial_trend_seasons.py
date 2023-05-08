# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:29:13 2023

@author: opio
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
none_map = ListedColormap(['none'])
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import pymannkendall as mk
import matplotlib as mpl


# Read-in file
file = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/precp_NTCF_mitigation.nc')


# Calculate seasonal means
season = file['precp_mitigation'].groupby('time.season')
#precp_djf = season['DJF'].groupby('time.year').mean('time')
#precp_mam = season['MAM'].groupby('time.year').mean('time')
#precp_jja = season['JJA'].groupby('time.year').mean('time')
precp_son = season['SON'].groupby('time.year').mean('time')


# Define dimensions for the MK trend calculation
slope_val = np.zeros((len(precp_son.lat.values), len(precp_son.lon.values)))
p_value = np.zeros((len(precp_son.lat.values), len(precp_son.lon.values)))

# Perform MK trend test for son mean
for i in np.arange(len(precp_son.lat.values)):
    for j in np.arange(len(precp_son.lon.values)):
        try:
            slope_val[i,j] = mk.original_test(precp_son[:,i,j]).slope
            p_value[i,j] = mk.original_test(precp_son[:,i,j]).p
        except:
            slope_val[i,j] = np.nan
            p_value[i,j] = np.nan



## Define data as xarray dataset and save the files
output1=xr.DataArray(slope_val, dims=('lat', 'lon'), 
                     coords={'lat':precp_son.lat, 'lon':precp_son.lon}, 
                     attrs=dict(description="slope", units="mm month-1"),)
trnd = output1.rename("trend")

trnd.to_netcdf('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_trend_son.nc')



output2=xr.DataArray(p_value, dims=('lat', 'lon'),
                     coords={'lat':precp_son.lat, 'lon':precp_son.lon}, 
                     attrs=dict(description="significance",),)
pval = output2.rename("p_val")

pval.to_netcdf('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_pval_son.nc')

# Create condition to plot only significant values
cond = (pval < 0.05)
sig_reg = pval.where(cond)



# Plot
fig = plt.subplots(figsize=(8, 6))
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.linewidth'] = 1
ax = plt.subplot(projection=ccrs.PlateCarree())
plt.contourf(precp_son['lon'], precp_son['lat'], trnd, cmap='BrBG')#, vmin=-4.2, vmax=4.2)
#plt.pcolormesh(precp_annual['lon'], precp_annual['lat'], trnd, cmap='BrBG', vmin=-4.2, vmax=4.2)
ax.pcolor(precp_son['lon'], precp_son['lat'], sig_reg, hatch='...', cmap=none_map,
          edgecolor='black', lw=0, zorder=4)
ax.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax.add_feature(cfeature.BORDERS, linewidth=1.2)
ax.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.colorbar(label='Trend (mm/month)')
plt.show()