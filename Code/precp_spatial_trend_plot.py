# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:33:30 2023

@author: opio
"""
# Import libraries
import matplotlib.pyplot as plt
from matplotlib import colors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import matplotlib as mpl
from matplotlib.colors import ListedColormap
none_map = ListedColormap(['none'])
import warnings
warnings.filterwarnings('ignore')


# Import files

" SSP3-7.0 "

# Annual files
file_annual1_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_trend_annual.nc')
file_annual2_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_pval_annual.nc')
trend_annual_high = file_annual1_high['trend']/3.5
pval_annual_high = file_annual2_high['p_val']

# DJF files
file_djf1_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_trend_djf.nc')
file_djf2_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_pval_djf.nc')
trend_djf_high = file_djf1_high['trend']/3.5
pval_djf_high = file_djf2_high['p_val']

# MAM files
file_mam1_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_trend_mam.nc')
file_mam2_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_pval_mam.nc')
trend_mam_high = file_mam1_high['trend']/3.5
pval_mam_high = file_mam2_high['p_val']

# JJA files
file_jja1_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_trend_jja.nc')
file_jja2_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_pval_jja.nc')
trend_jja_high = file_jja1_high['trend']/3.5
pval_jja_high = file_jja2_high['p_val']

# SON files
file_son1_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_trend_son.nc')
file_son2_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_high/precp_high_pval_son.nc')
trend_son_high = file_son1_high['trend']/3.5
pval_son_high = file_son2_high['p_val']



" SSP3-7.0_lowNTCF "

# Annual files
file_annual1_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_trend_annual.nc')
file_annual2_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_pval_annual.nc')
trend_annual_low = file_annual1_low['trend']/3.5
pval_annual_low = file_annual2_low['p_val']

# DJF files
file_djf1_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_trend_djf.nc')
file_djf2_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_pval_djf.nc')
trend_djf_low = file_djf1_low['trend']/3.5
pval_djf_low = file_djf2_low['p_val']

# MAM files
file_mam1_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_trend_mam.nc')
file_mam2_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_pval_mam.nc')
trend_mam_low = file_mam1_low['trend']/3.5
pval_mam_low = file_mam2_low['p_val']

# JJA files
file_jja1_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_trend_jja.nc')
file_jja2_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_pval_jja.nc')
trend_jja_low = file_jja1_low['trend']/3.5
pval_jja_low = file_jja2_low['p_val']

# SON files
file_son1_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_trend_son.nc')
file_son2_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval/precp_low_pval_son.nc')
trend_son_low = file_son1_low['trend']/3.5
pval_son_low = file_son2_low['p_val']



" NTCF mitigation "

# Annual files
file_annual1_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_trend_annual.nc')
file_annual2_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_pval_annual.nc')
trend_annual_mitigation = file_annual1_mitigation['trend']/3.5
pval_annual_mitigation = file_annual2_mitigation['p_val']

# DJF files
file_djf1_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_trend_djf.nc')
file_djf2_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_pval_djf.nc')
trend_djf_mitigation = file_djf1_mitigation['trend']/3.5
pval_djf_mitigation = file_djf2_mitigation['p_val']

# MAM files
file_mam1_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_trend_mam.nc')
file_mam2_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_pval_mam.nc')
trend_mam_mitigation = file_mam1_mitigation['trend']/3.5
pval_mam_mitigation = file_mam2_mitigation['p_val']

# JJA files
file_jja1_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_trend_jja.nc')
file_jja2_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_pval_jja.nc')
trend_jja_mitigation = file_jja1_mitigation['trend']/3.5
pval_jja_mitigation = file_jja2_mitigation['p_val']

# SON files
file_son1_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_trend_son.nc')
file_son2_mitigation = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/trends_and_pval_mitigation/precp_mitigation_pval_son.nc')
trend_son_mitigation = file_son1_mitigation['trend']/3.5
pval_son_mitigation = file_son2_mitigation['p_val']






# Create condition to plot only significant values

" SSP3-7.0 "
condition_annual_high = (pval_annual_high < 0.05)
condition_djf_high = (pval_djf_high < 0.05)
condition_mam_high = (pval_mam_high < 0.05)
condition_jja_high = (pval_jja_high < 0.05)
condition_son_high = (pval_son_high < 0.05)

significant_annual_high = pval_annual_high.where(condition_annual_high)
significant_djf_high = pval_djf_high.where(condition_djf_high)
significant_mam_high = pval_mam_high.where(condition_mam_high)
significant_jja_high = pval_jja_high.where(condition_jja_high)
significant_son_high = pval_son_high.where(condition_son_high)



" SSP3-7.0_lowNTCF "

condition_annual_low = (pval_annual_low < 0.05)
condition_djf_low = (pval_djf_low < 0.05)
condition_mam_low = (pval_mam_low < 0.05)
condition_jja_low = (pval_jja_low < 0.05)
condition_son_low = (pval_son_low < 0.05)

significant_annual_low = pval_annual_low.where(condition_annual_low)
significant_djf_low = pval_djf_low.where(condition_djf_low)
significant_mam_low = pval_mam_low.where(condition_mam_low)
significant_jja_low = pval_jja_low.where(condition_jja_low)
significant_son_low = pval_son_low.where(condition_son_low)



" NTCF mitigation "
condition_annual_mitigation = (pval_annual_mitigation < 0.05)
condition_djf_mitigation = (pval_djf_mitigation < 0.05)
condition_mam_mitigation = (pval_mam_mitigation < 0.05)
condition_jja_mitigation = (pval_jja_mitigation < 0.05)
condition_son_mitigation = (pval_son_mitigation < 0.05)

significant_annual_mitigation = pval_annual_mitigation.where(condition_annual_mitigation)
significant_djf_mitigation = pval_djf_mitigation.where(condition_djf_mitigation)
significant_mam_mitigation = pval_mam_mitigation.where(condition_mam_mitigation)
significant_jja_mitigation = pval_jja_mitigation.where(condition_jja_mitigation)
significant_son_mitigation = pval_son_mitigation.where(condition_son_mitigation)




# Plotting
fig=plt.figure(figsize=(12, 20), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.08, wspace=0)

divnorm = colors.TwoSlopeNorm(vmin=-1.57, vcenter=0, vmax=1.57)

" SSP3-7.0 "
ax = plt.subplot(5,3,1, projection=ccrs.PlateCarree())
plt.pcolormesh(file_annual1_high['lon'], file_annual1_high['lat'], trend_annual_high, cmap='BrBG', norm=divnorm)
ax.pcolor(file_annual2_high['lon'], file_annual2_high['lat'], significant_annual_high, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax.add_feature(cfeature.BORDERS, linewidth=1.2)
ax.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.title('SSP3-7.0')
plt.text(0.14, 0.79, 'ANNUAL', rotation='vertical',
         transform=plt.gcf().transFigure)


ax1 = plt.subplot(5,3,4, projection=ccrs.PlateCarree())
plt.pcolormesh(file_djf1_high['lon'], file_djf1_high['lat'], trend_djf_high, cmap='BrBG', norm=divnorm)
ax1.pcolor(file_djf2_high['lon'], file_djf2_high['lat'], significant_djf_high, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax1.coastlines(resolution='10m', color='black', linewidth=0.9)
ax1.add_feature(cfeature.BORDERS, linewidth=1.2)
ax1.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.text(0.14, 0.65, 'DJF', rotation='vertical',
         transform=plt.gcf().transFigure)

ax2 = plt.subplot(5,3,7, projection=ccrs.PlateCarree())
plt.pcolormesh(file_mam1_high['lon'], file_mam1_high['lat'], trend_mam_high, cmap='BrBG', norm=divnorm)
ax2.pcolor(file_mam2_high['lon'], file_mam2_high['lat'], significant_mam_high, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax2.coastlines(resolution='10m', color='black', linewidth=0.9)
ax2.add_feature(cfeature.BORDERS, linewidth=1.2)
ax2.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.text(0.14, 0.49, 'MAM', rotation='vertical',
         transform=plt.gcf().transFigure)

ax3 = plt.subplot(5,3,10, projection=ccrs.PlateCarree())
plt.pcolormesh(file_jja1_high['lon'], file_jja1_high['lat'], trend_jja_high, cmap='BrBG', norm=divnorm)
ax3.pcolor(file_jja2_high['lon'], file_jja2_high['lat'], significant_jja_high, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax3.coastlines(resolution='10m', color='black', linewidth=0.9)
ax3.add_feature(cfeature.BORDERS, linewidth=1.2)
ax3.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.text(0.14, 0.34, 'JJA', rotation='vertical',
         transform=plt.gcf().transFigure)

ax4 = plt.subplot(5,3,13, projection=ccrs.PlateCarree())
plt.pcolormesh(file_son1_high['lon'], file_son1_high['lat'], trend_son_high, cmap='BrBG', norm=divnorm)
ax4.pcolor(file_son2_high['lon'], file_son2_high['lat'], significant_son_high, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax4.coastlines(resolution='10m', color='black', linewidth=0.9)
ax4.add_feature(cfeature.BORDERS, linewidth=1.2)
ax4.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.text(0.14, 0.19, 'SON', rotation='vertical',
         transform=plt.gcf().transFigure)



" SSP3-7.0_lowNTCF "
ax5 = plt.subplot(5,3,2, projection=ccrs.PlateCarree())
plt.pcolormesh(file_annual1_low['lon'], file_annual1_low['lat'], trend_annual_low, cmap='BrBG', norm=divnorm)
ax5.pcolor(file_annual2_low['lon'], file_annual2_low['lat'], significant_annual_low, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax5.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax5.add_feature(cfeature.BORDERS, linewidth=1.2)
ax5.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.title('SSP3-7.0_lowNTCF')


ax6 = plt.subplot(5,3,5, projection=ccrs.PlateCarree())
plt.pcolormesh(file_djf1_low['lon'], file_djf1_low['lat'], trend_djf_low, cmap='BrBG', norm=divnorm)
ax6.pcolor(file_djf2_low['lon'], file_djf2_low['lat'], significant_djf_low, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax6.coastlines(resolution='10m', color='black', linewidth=0.9)
ax6.add_feature(cfeature.BORDERS, linewidth=1.2)
ax6.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)

ax7 = plt.subplot(5,3,8, projection=ccrs.PlateCarree())
plt.pcolormesh(file_mam1_low['lon'], file_mam1_low['lat'], trend_mam_low, cmap='BrBG', norm=divnorm)
ax7.pcolor(file_mam2_low['lon'], file_mam2_low['lat'], significant_mam_low, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax7.coastlines(resolution='10m', color='black', linewidth=0.9)
ax7.add_feature(cfeature.BORDERS, linewidth=1.2)
ax7.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)

ax8 = plt.subplot(5,3,11, projection=ccrs.PlateCarree())
plt.pcolormesh(file_jja1_low['lon'], file_jja1_low['lat'], trend_jja_low, cmap='BrBG', norm=divnorm)
ax8.pcolor(file_jja2_low['lon'], file_jja2_low['lat'], significant_jja_low, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax8.coastlines(resolution='10m', color='black', linewidth=0.9)
ax8.add_feature(cfeature.BORDERS, linewidth=1.2)
ax8.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)

ax9 = plt.subplot(5,3,14, projection=ccrs.PlateCarree())
plt.pcolormesh(file_son1_low['lon'], file_son1_low['lat'], trend_son_low, cmap='BrBG', norm=divnorm)
ax9.pcolor(file_son2_low['lon'], file_son2_low['lat'], significant_son_low, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax9.coastlines(resolution='10m', color='black', linewidth=0.9)
ax9.add_feature(cfeature.BORDERS, linewidth=1.2)
ax9.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)



" NTCF mitigation "
ax10 = plt.subplot(5,3,3, projection=ccrs.PlateCarree())
plt.pcolormesh(file_annual1_mitigation['lon'], file_annual1_mitigation['lat'], trend_annual_mitigation, cmap='BrBG', norm=divnorm)
ax10.pcolor(file_annual2_mitigation['lon'], file_annual2_mitigation['lat'], significant_annual_mitigation, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax10.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax10.add_feature(cfeature.BORDERS, linewidth=1.2)
ax10.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
plt.title('NTCF mitigation')


ax11 = plt.subplot(5,3,6, projection=ccrs.PlateCarree())
plt.pcolormesh(file_djf1_mitigation['lon'], file_djf1_mitigation['lat'], trend_djf_mitigation, cmap='BrBG', norm=divnorm)
ax11.pcolor(file_djf2_mitigation['lon'], file_djf2_mitigation['lat'], significant_djf_mitigation, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax11.coastlines(resolution='10m', color='black', linewidth=0.9)
ax11.add_feature(cfeature.BORDERS, linewidth=1.2)
ax11.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)

ax12 = plt.subplot(5,3,9, projection=ccrs.PlateCarree())
plt.pcolormesh(file_mam1_mitigation['lon'], file_mam1_mitigation['lat'], trend_mam_mitigation, cmap='BrBG', norm=divnorm)
ax12.pcolor(file_mam2_mitigation['lon'], file_mam2_mitigation['lat'], significant_mam_mitigation, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax12.coastlines(resolution='10m', color='black', linewidth=0.9)
ax12.add_feature(cfeature.BORDERS, linewidth=1.2)
ax12.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)

ax13 = plt.subplot(5,3,12, projection=ccrs.PlateCarree())
plt.pcolormesh(file_jja1_mitigation['lon'], file_jja1_mitigation['lat'], trend_jja_mitigation, cmap='BrBG', norm=divnorm)
ax13.pcolor(file_jja2_mitigation['lon'], file_jja2_mitigation['lat'], significant_jja_mitigation, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax13.coastlines(resolution='10m', color='black', linewidth=0.9)
ax13.add_feature(cfeature.BORDERS, linewidth=1.2)
ax13.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)

ax14 = plt.subplot(5,3,15, projection=ccrs.PlateCarree())
last_plot = plt.pcolormesh(file_son1_mitigation['lon'], file_son1_mitigation['lat'], trend_son_mitigation, cmap='BrBG', norm=divnorm)
ax14.pcolor(file_son2_mitigation['lon'], file_son2_mitigation['lat'], significant_son_mitigation, hatch='...', 
          cmap=none_map, edgecolor='black', lw=0, zorder=4)
ax14.coastlines(resolution='10m', color='black', linewidth=0.9)
ax14.add_feature(cfeature.BORDERS, linewidth=1.2)
ax14.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.ylim(-12.8, 6.8)
plt.xlim(28, 43)
cb_axes = plt.gcf().add_axes([0.89, 0.2, 0.013, 0.6])
cb = plt.colorbar(last_plot, cb_axes,
                   label="Sen's slope (mm $\mathregular{month^{-1}}$ $\mathregular{decade^{-1}}$)", 
                   orientation='vertical')
plt.show()