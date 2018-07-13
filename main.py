import requests
import argparse
import json
import module
from argparse import ArgumentParser
from getpass import getpass

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
parser.add_argument("-n", action="module.glotka()")

args = parser.parse_args()


def showtop20():
    print('running showtop20')

def listapps():
    print('running listapps')

