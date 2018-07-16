#!/usr/local/bin/python
import os
import distutils.sysconfig
import json
import sys
import platform
import pyaml
from subprocess import check_output
import subprocess


def get_data():
    """gathers data for output

    :return: dict data
    """
    data = {'python_ver': platform.python_version(),
            'python_name': subprocess.check_output(["pyenv", "versions"]),
            'python_venv': is_venv(),
            'python_loc': py_location(),
            'pip_loc': pip_location(),
            'python_path': os.environ.get('PYTHONPATH', ''),
            'packages': pip_installed_packages(),
            'site_packages_location':
                distutils.sysconfig.get_python_lib(), }
    return str(data)


def form_data(spec):
    """load data in json or yaml

    :param spec: file format
    :return: dumps dependent on parameter
    """
    if spec == 'json':
        return json.dumps(get_data())
    elif spec == 'yaml':
        return pyaml.dump(get_data())

def py_names():
    a


def py_location():
    """gathers python location

    :return: py_location variable that stores location information
    """
    py_data = check_output('which -a python', shell=True)
    py_location = py_data.splitlines()
    return py_location


def pip_location():
    """gathers pip location

    :return:pip_location variable with information about pip location
    """
    pip_data = check_output('which -a pip', shell=True)
    pip_location = pip_data.splitlines()
    return pip_location


def pip_installed_packages():
    """gathers list of pip installed packages

    :return: pip_data_list variable with packages information
    """
    pip_data = check_output('pip freeze', shell=True)
    pip_data_list = pip_data.splitlines()
    return pip_data_list


def is_venv():
    """gathers venv location info

    :return: venv information
    """
    if hasattr(sys, 'real_prefix'):
        return os.environ.get('VIRTUAL_ENV')
    else:
        return 'not_set'
