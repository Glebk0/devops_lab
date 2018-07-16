import os
import distutils.sysconfig
import json
import sys
import platform
import pyaml
from subprocess import check_output


def get_data():
    """
    Form data for output
    :return: dict with data
    """
    data = {'python_ver': platform.python_version(),
            #'python_name': py_names(),
            'python_venv': is_venv(),
            'python_loc': py_location(),
            'pip_loc': pip_location(),
            'python_path': os.environ.get('PYTHONPATH', ''),
            'packages': pip_installed_packages(),
            'site_packages_location':
                distutils.sysconfig.get_python_lib(), }
    return str(data)


def form_data(spec):
    if spec == 'json':
        return json.dumps(get_data())
    elif spec == 'yaml':
        return pyaml.dump(get_data())


def py_location():
    py_data = check_output('which -a python', shell=True)
    py_location = py_data.splitlines()
    return py_location


def pip_location():
    pip_data = check_output('which -a pip', shell=True)
    pip_location = pip_data.splitlines()
    return pip_location


def pip_installed_packages():
    pip_data = check_output('pip freeze', shell=True)
    pip_data_list = pip_data.splitlines()
    return pip_data_list


def is_venv():
    if hasattr(sys, 'real_prefix'):
        return os.environ.get('VIRTUAL_ENV')
    else:
        return 'not_set'
