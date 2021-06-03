import ROOT, os
from ROOT import TCanvas, TGraph, TLegend, TPad
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

fileName = "mm-cs-data.csv"
if not os.path.isfile(fileName):
   print("file not found")

def getLinePlot(df, ax, x1, y1, param_dict):
   param_dict['kind'] = 'line' 
   out = df.plot(x=x1, y=y1, ax=ax, **param_dict)
   return out


def setAxes(ax):
   ax.set_xlabel('Center-of-Mass Energy [TeV]')
   ax.set_xlim(0, 32)
   ax.set_ylabel(r'$\sigma(\mu^{+}\mu^{-}\,\to\,$X) [pb]')
   ax.set_yscale('log')
   ax.set_title('')
   ax.grid(True)
   
   box = ax.get_position()
   ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
   ax.legend(bbox_to_anchor=(1,.9))

   
df = pd.read_csv(fileName, encoding="utf-8")

channels = {'aa':  {'color':'red',    'label':r'$\gamma\gamma$', 'lmark':'.'},
            'ff':  {'color':'blue',   'label':r'$\mathcal{ff}$', 'lmark':'p'},
            'mmh': {'color':'orange', 'label':r'$\mu\mu$'+'h'  , 'lmark':'v'},
            'mmhh':{'color':'green',  'label':r'$\mu\mu$'+'hh' , 'lmark':'^'},
            'mmz': {'color':'purple', 'label':r'$\mu\mu$'+'Z'  , 'lmark':'<'},
            'zh':  {'color':'brown',  'label':'Zh'             , 'lmark':'>'},
            'zz':  {'color':'pink',   'label':'ZZ'             , 'lmark':'s'},
            'vva': {'color':'gray',   'label':'VV'+r'$\gamma$' , 'lmark':'P'},
            'vvh': {'color':'olive',  'label':'VVh'            , 'lmark':'p'},
            'vvhh':{'color':'cyan',   'label':'VVhh'           , 'lmark':'*'},
            'vvz': {'color':'yellow', 'label':'VVZ'            , 'lmark':'h'},
            'ww':  {'color':'magenta','label':'WW'             , 'lmark':'+'},
            'za':  {'color':'C0',     'label':'Z'+r'$\gamma$'  , 'lmark':'x'}
            }


df_channels = {}

for ch in channels:
  df_channels[ch] = df[df['FS'] == ch]

fig, ax = plt.subplots()

for key in channels:
  getLinePlot(df_channels[key], ax, 'Ecm', 'CS', 
            {'color':channels[key]['color'], 
	     'label':channels[key]['label'],
	     'marker':channels[key]['lmark']})

setAxes(ax)

plt.savefig('EcmVsCS.png')
