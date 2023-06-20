# CMIP6_Downscaling_with_WRF
This repository contains code and data for downscaled CMIP6 NTCF experiments

# Notes
All the meteorological variables of the MPI-ESM1-2-HAM model were available at a 6-hourly resolution except for surface temperature (ts) which was obtained at a daily resolution. This was the highest available resolution. Therefore, to create consistency with the other variables, surface temperature was modified to a 6-hourly resolution. The modified file was such that for each day, the same surface temperature reading was provided 4 times, that is, after every 6 hours. A similar modification was demonstrated by Bruyère et al. (2015), and it generated scientifically realistic downscaled results. The python scripts have been provided in this folder.

## References
Bruyère, C. L., Monaghan, A. J., Steinhoff, D. F., & Yates, D. (2015). Bias-Corrected CMIP5 CESM Data in WRF/MPAS Intermediate File Format. https://doi.org/10.5065/D6445JJ7
