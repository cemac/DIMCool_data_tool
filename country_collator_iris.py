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
import iris
from glob import glob

from errlib import dirverify, ArgumentsError
from argparse import ArgumentParser

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

    if not dirverify(datadir,"output"):
        raise ArgumentsError("Could not verify output directory")

    if not dirverify(os.path.join(datadir,'ind_rcp'),"output"):
        raise ArgumentsError("Could not verify input directory")

    country = datadir.split('/')[-1]

    retdata=[datadir,country]

    return retdata


def fieldlists(dataloc):

    contents=[i for i in os.listdir(dataloc) if not os.path.isdir(os.path.join(dataloc,i))]

    fields=[i.split('_') for i in contents]

    in_crops=list(set([e[0] for e in fields]))
    in_models=list(set([e[1] for e in fields]))
    in_rcps=list(set([e[2].split('.')[0] for e in fields]))

    in_crops.sort()
    in_models.sort()
    in_rcps.sort()

    return (in_crops,in_models,in_rcps)

def catdata(catlist,outfil,durflg=0):

    if durflg == 1:
        cubes=iris.load(catlist, ['plant_date','yield','biomass','t_rad_abs', 'rlai_2', 'evtrans1'])
    else:
        cubes=iris.load(catlist)

    iris.util.equalise_attributes(cubes)

    cubes2 = cubes.concatenate()

    if durflg == 1:
        durcube = iris.load_cube(catlist[0],'dur')
        tochange = [cube for cube in cubes2 if cube.var_name == 't_rad_abs'][0]
        tochange.rename(durcube.name())
        tochange.units=durcube.units
        tochange.long_name=durcube.long_name
        tochange.var_name=durcube.var_name

    (path, file) = os.path.split(outfil)
    if not os.path.exists(path):
        os.makedirs(path)

    iris.fileformats.netcdf.save(cubes2, outfil)

    cubes = None
    cubes2 = None

def combinedata(outpath,country):

    print ("Collecting and merging data for {}".format(country), flush=True)

    rootloc = outpath
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

    (in_crops,in_models,in_rcps) = fieldlists(dataloc)

    for crop in in_crops:
        for rcp in in_rcps:
            catlist=glob(os.path.join(dataloc,"{}_*_{}.nc".format(crop,rcp)))
            catlist.sort()
            catdata(catlist,os.path.join(modelloc,"{}_{}_{}.nc".format(country,crop,rcp)), durflg=1)

            print ("Combined models for crop {} and rcp {}".format(crop,rcp), flush=True)

        print ("Completed consolidation over models for all rcps for crop {}".format(crop), flush=True)

    print("Completed consolidation for all crops in country {}".format(country), flush=True)

def main():

    [outpath,country]=readargs()

    combinedata(outpath,country)


if __name__=="__main__":
    main()
