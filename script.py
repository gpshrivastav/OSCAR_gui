import sys
import xarray as xr
import matplotlib.pyplot as plt

input = sys.argv

model    = None
scenario = None
region   = None
species  = None

ds_data = xr.open_dataset('data/emissions_CEDS.nc')

if region == 'global':
    ds_data[species].sel(scen=scenario).sum(["reg_mask", "sector"], min_count=1).plot()
else:
    ds_data[species].sel(reg_mask=ds_data.reg_mask_code==region, scen=scenario).sum( "sector", min_count=1).plot()
plt.savefig('displays/static/displays/figures/dp_002.png', dpi=200)
plt.close()



#var = "E_"+var
#
#ds_data = xr.open_dataset('data/emissions_CEDS.nc')
#
#if reg_mask == 'global':
#    ds_data[var].sum(["reg_mask", "sector"], min_count=1).plot()
#
#else:
#    ds_data[var].sum( "sector", min_count=1).plot()
#
#plt.savefig('check.png', dpi=200)
#
##plt.savefig('displays/figures/dp_002.png', dpi=200)
