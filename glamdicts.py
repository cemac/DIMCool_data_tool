#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glam Dicts Library

Created on Mon 6th Sept 2021

@author: chmcsy
"""

countries={
        "malawi":0,
        "safrica":1,
        "tanzania":2,
        "zambia":3
        }
crops={
      "maize":2,
      "potato":0,
      "soybean":3,
      "groundnut":1,
      "cassava":4,
      "rice":5,
      "sorghum":6,
      "millet":7,
      "sugarcane":8,
      "sweetpot":9,
      "wheat":10
      }
models={
       "bcc-csm1-1":0,
       "bcc-csm1-1-m":1,
       "BNU-ESM":2,
       "CanESM2":3,
       "CNRM-CM5":4,
       "CSIRO-Mk3-6-0":5,
       "GFDL-CM3":6,
       "GFDL-ESM2G":7,
       "GFDL-ESM2M":8,
       "IPSL-CM5A-LR":9,
       "IPSL-CM5A-MR":10,
       "MIROC5":11,
       "MIROC-ESM":12,
       "MIROC-ESM-CHEM":13,
       "MPI-ESM-LR":14,
       "MPI-ESM-MR":15,
       "MRI-CGCM3":16,
       "NorESM1-M":17
       }
rcps={
     "rcp26":0,
     "rcp85":2
     }

prod_lst=["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1"]
irr_lst=["0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1","2"]

column={'V1': 'Year',
        'V2': 'Latitude',
        'V3': 'Longitude',
        'V4': 'Planting date',
        'V5': 'Final crop stage (ISTG)',
        'V6': 'Mean root length density by volume',
        'V7': 'LAI (specifically RLAI (2))',
        'V8': 'Yield',
        'V9': 'Biomass',
        'V10': 'Empty (irrigated fraction; SLA)',
        'V11': 'Harvest index',
        'V12': 'Cumulative rain',
        'V13': 'Solar radiation',
        'V14': 'Total soil water',
        'V15': 'Transpiration',
        'V16': 'Evapotranspiration_1',
        'V17': 'Potential evapotranspiration (limited by soil transport, LAI and energy)',
        'V18': 'Soil water stress factor',
        'V19': 'Evapotranspiration_2',
        'V20': 'Runoff',
        'V21': 'Cumulative runoff',
        'V22': 'Potential (root-limited) uptake',
        'V23': 'Cumulative potential uptake',
        'V24': 'Drainage',
        'V25': 'Cumulative drainage',
        'V26': 'Potential (energy-limited) transpiration',
        'V27': 'Cumulative potential transpiration',
        'V28': 'Cumulative evaporation',
        'V29': 'Cumulative potential evaporation',
        'V30': 'Cumulative transpiration',
        'V31': 'Root length density by area',
        'V32': 'Root Length Density by Area / LAI',
        'V33': 'Rainfall',
        'V34': 'Change in soil moisture',
        'V35': 'Absorbed radiation',
        'V36': 'Duration',
        'V37': 'Mean vapour pressure deficit',
        'V38': 'Tot net radiation',
        'V39': 'Total percentage of pods setting (TOTPP)',
        'V40': 'Total percentage of pods setting considering temperature only (TOTPP_HIT)',
        'V41': 'Total percentage of pods setting considering water stress only (TOTPP_WAT)',
        'V42': 'Mean temperature during the crop season (planting to harvest).',
        'V43': 'Factor DHDT is reduced by due to heat stress when HTS=1 or 2 (HT_FAC)',
        'V44': 'TOTWHARVDEP',
        'V45': 'STORED_WATER',
        'V46': 'Panicle initiation date (DOY - Sorghum only)',
        'V47': 'Flowering date (DOY - Sorghum only)',
        'V48': 'Total supplementary irrigation added to VOLSW (1) if using SUP irrigation'
        'V49': 'Maximum value of Leaf Area Index',
        }
var_nm={'V1' : 'year',
        'V2' : 'latitude',
        'V3' : 'longitude',
        'V4' : 'plant_date',
        'V5' : 'istg_final',
        'V6' : 'rlv_mean',
        'V7' : 'rlai_2',
        'V8' : 'yield',
        'V9' : 'biomass',
        'V10': 'sla',
        'V11': 'harv_index',
        'V12': 'tot_rain',
        'V13': 'srad_final',
        'V14': 'soil_wat',
        'V15': 'trans',
        'V16': 'evtrans1',
        'V17': 'pot_evtrans',
        'V18': 'soil_wat_fac',
        'V19': 'evtrans2',
        'V20': 'runoff',
        'V21': 'tot_runoff',
        'V22': 'pot_uptake',
        'V23': 'tot_pot_uptake',
        'V24': 'drainage',
        'V25': 'tot_drainage',
        'V26': 'pot_trans',
        'V27': 'tot_pot_trans',
        'V28': 'tot_evap',
        'V29': 'tot_pot_ev',
        'V30': 'tot_trans',
        'V31': 'rla',
        'V32': 'rla_over_lai',
        'V33': 'rain_final',
        'V34': 'd_soil_moist',
        'V35': 't_rad_abs',
        'V36': 'dur',
        'V37': 'mean_vap_pres_def',
        'V38': 'Tot_net_rad',
        'V39': 'tot_per_pod',
        'V40': 'tot_per_pod_hit',
        'V41': 'tot_per_pod_wat',
        'V42': 'mean_temp',
        'V43': 'dhdt_fac',
        'V44': 'totwharvdep',
        'V45': 'stor_wat',
        'V46': 'pan_init_date',
        'V47': 'flowr_date',
        'V48': 'tot_irr_sup'
        'V49': 'lai_max',
        }
var_units={'V1' : 'year',
           'V2' : 'degrees_north',
           'V3' : 'degrees_east',
           'V4' : 'days',
           'V5' : '1',
           'V6' : 'cm/cm^3',
           'V7' : 'm^2/m^2',
           'V8' : 'kg/ha',
           'V9' : 'kg/ha',
           'V10': '1',
           'V11': '1',
           'V12': 'cm',
           'V13': 'MJ/m^2',
           'V14': 'cm',
           'V15': 'cm',
           'V16': 'cm',
           'V17': 'cm',
           'V18': '1',
           'V19': 'cm',
           'V20': 'cm',
           'V21': 'cm',
           'V22': 'cm',
           'V23': 'cm',
           'V24': 'cm',
           'V25': 'cm',
           'V26': 'cm',
           'V27': 'cm',
           'V28': 'cm',
           'V29': 'cm',
           'V30': 'cm',
           'V31': 'cm/cm^2',
           'V32': 'cm/cm^2',
           'V33': 'cm',
           'V34': 'cm',
           'V35': 'MJ/m^2',
           'V36': 'days',
           'V37': 'kPa',
           'V38': 'MJ/m^2',
           'V39': '%',
           'V40': '%',
           'V41': '%',
           'V42': 'celsius',
           'V43': '1',
           'V44': 'cm',
           'V45': 'cm',
           'V46': 'day',
           'V47': 'day',
           'V48': 'cm'
           'V49': 'm^2/m^2',
           }
