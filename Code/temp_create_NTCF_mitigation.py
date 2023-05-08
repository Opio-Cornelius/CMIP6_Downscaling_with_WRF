# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:51:11 2023

@author: opio
"""

import xarray as xr

# Import files
file_high = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/temp_ssp370.nc')
file_low = xr.open_dataset('C:/python_work/phd/paper5/real_work/phase2/temp_ssp370_lowNTCF.nc')

temp_NTCF_mitigation = file_low['temp_ssp370_lowNTCF'] - file_high['temp_ssp370']


mitigation_file = xr.Dataset(data_vars=dict(temp_mitigation=(['time', 'lat', 'lon'], temp_NTCF_mitigation.data)),
                             coords=({'lat': (['lat'], temp_NTCF_mitigation.lat.data),
                                                  'lon': (['lon'], temp_NTCF_mitigation.lon.data),
                                                  'time': temp_NTCF_mitigation.time.data}))


mitigation_file.to_netcdf('C:/python_work/phd/paper5/real_work/phase2/temp_NTCF_mitigation.nc')