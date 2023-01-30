from django.shortcuts import render, redirect

from django.http import HttpResponse

from subprocess import run, PIPE

import sys, os
import xarray as xr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from .forms import ModelForm

from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    return render(request, 'displays/index.html')

#@require_POST
def select_model(request):
    #form = ModelForm(request.POST)
    model    = request.POST.get('model','')
    scenario = request.POST.get('scenario','')
    region   = request.POST.get('region','')
    species  = request.POST.get('species','')

    ds_data = xr.open_dataset('data/emissions_CEDS.nc')

    if (model != 'None') and (scenario != 'None') and (region != 'None') and (species != 'None'):

        if region == 'global':
            ds = ds_data[species].sum(["reg_mask", "sector"], min_count=1)
        else:
            ds = ds_data[species].sel(reg_mask=ds_data.reg_mask_code==region).sum( "sector", min_count=1)

        if scenario == 'all':
            ds.plot.line(x='year')
        else:
            ds.sel(scen=scenario).plot()


        plt.savefig('displays/static/displays/figures/dp_002.png', dpi=200)
        plt.close()
        
        return render(request, 'displays/index.html')
    
    else:
        html = "<html><body>!!!Please select input values.</body></html>" 
        return HttpResponse(html)

    #result = run([sys.executable, "script.py", "2", "4"], shell=False, stdout=PIPE)
    #print(ds_data.dims)

    