#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Error Library

Created on Thu Jan 30 15:01:49 2020

@author: chmcsy
"""

from sys import stderr, exit
from os import path, makedirs

class ArgumentsError(Exception):
    '''
    Exception raised when there is an error detected in the argument list.
    '''
    def __init__(self, msg):
        stderr.write('[FATAL ERROR] : %s' % msg )
        exit(9)

class FatalError(Exception):
    '''
    Exception raised when there is an error detected in the argument list.
    '''
    def __init__(self, msg):
        stderr.write('[FATAL ERROR] : %s' % msg )
        exit(9)

class FileError(Exception):
    '''
    Exception raised when contents of files are not as expected
    '''
    def __init__(self,msg):
        stderr.write('[FILE ERROR] : %s' % msg )
        exit(9)

class NonFatal(Exception):
    '''
    Exception raised for non-fatal errors
    '''
    def __init__(self,msg):
        stderr.write('[WARNING] : %s\n\nContinuing...\n' % msg )

def dirverify(iopath, inout="input"):

    if not (inout=="output" or inout == "input"):
        print("Incorrect use of dirverify function - second argument must be either \'input\' or \'output\'")
        return False

    if not isinstance(iopath,str):
        print("Data running directory is not a string!\n")
        return False

    if not path.exists(iopath):
        if inout == "output":
            print('Directory for output does not exist\n')
            try:
                makedirs(iopath)
            except:
                print("Unable to create output folder")
                return False
            else:
                print ("Folder {} was created".format(iopath))
        else:
            print('Directory for input does not exist\n')
            return False

    if iopath and not path.isdir(iopath):
        	print('Data '+inout+' location is not a directory\n')
            return False

    return True
