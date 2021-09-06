#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iFEED Data consolidation tool Level 2

Name: country_collator.py

Usage: python country_collator.py -d <dir>

Description:
    Combine all data for a each country in the iFEED project. This script should only be run after
    the year_collator.py script has been successfully run on all crops/models/rcps for a country.

Arguments:
    dir   : Location of the folder in which the data should be held in netCDF format.
            It is assumed that the data is in netCDF format and that the data has been
            produced using the year collator - ie all data for a single rcp is contained
            in a single file.

Restrictions:
    The input data should be in a directory called 'ind_rcp' within the directory given as argument.
    Assumption that folder structure and file naming convention are as output by year collator,
    ie:

        nc_outs/<country>/ind_rcps/<crop>_<model>_<rcp>.nc


Created June 2021

@author: Christopher Symonds, CEMAC, University of Leeds
"""

import os
from errlib import *
from argparse import ArgumentParser
from glob import glob
from nco import Nco

nco=Nco()

def readargs():
    '''
    Read input arguments if run as separate program
    '''

    parser = ArgumentParser(description=(
        'Combine the first level consolidated netCDF files for a particular climate scheme into'
        ' a single NetCDF file per country.'
        ))

    parser.add_argument('--dir', '-d',
                        type=str,
                        help='Path to country-level directory for nc files',
                        default='.')

    args = parser.parse_args()

    if args.dir=='.':
        datadir=os.getcwd()
    else:
        datadir=args.dir

    if not dirverify(outpath,"output"):
        raise ArgumentsError("Could not verify output directory")

    if not dirverify(os.path.join(outpath,'ind_rcp'),"output"):
        raise ArgumentsError("Could not verify input directory")

    country = outpath.split('/')[-1]

    retdata=[outpath,country]

    return retdata

def catdata(catlist,outfil,dim):

    nco.ncks(input=catlist[0], output="{}_recdim.nc".format(catlist[0][:-3]), options=['-O','-h', '--mk_rec_dmn '+dim])

    catlist.insert(1,"{}_recdim.nc".format(catlist[0][:-3]))
    newfile=outfil+'.nc'
    (path, file) = os.path.split(newfile)
    if not os.path.exists(path):
        os.makedirs(path)
    nco.ncrcat(input=catlist[1:], output=newfile)


def combinedata(outpath,country):

    print ("Collecting and merging data for {}".format(country))

    rootloc = os.path.join(outpath,country)
    dataloc = os.path.join(rootloc,'ind_rcp')
    modelloc = os.path.join(rootloc,'ind_mod')
    croploc = os.path.join(rootloc,'ind_crop')

    try:
        os.makedirs(modelloc)
    except FileExistsError:
        pass

    try:
        os.makedirs(croploc)
    except FileExistsError:
        pass

    for crop in crops.keys():
        for model in models.keys():
            catlst1=glob(os.path.join(dataloc,"{}_{}_*.nc".format(crop,model)))
            catlst1.sort()
            catdata(catlist1,os.path.join(modelloc,"{}_{}.nc".format(crop,model)),"rcp")

        catlst2=glob(os.path.join(modelloc,"{}_*.nc".format(crop)))
        catlst2.sort()
        catdata(catlist2,os.path.join(croploc,"{}_{}.nc".format(crop)),"model")

    catlst3=glob(os.path.join(croploc,"*.nc"))
    catlst3.sort()
    catdata(catlst3,os.path.join(rootloc,country+".nc"),"crop")

    nco.ncks(input=os.path.join(rootloc,country+".nc"), output="{}_recdim.nc".format(os.path.join(rootloc,country+".nc")), options=['-O','-h', '--mk_rec_dmn time'])


def main():

    [outpath,country]=readargs()

    combinedata(outpath,country)


if __name__=="__main__":
    main()