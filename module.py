import json
import psutil


def cpu_load():
    """get cpu_load information

    :return: cpu_load_var is variable that stores avg load percent over 5 min
    """
    cpu_load_var = psutil.cpu_percent(interval=5, percpu=False)
    return cpu_load_var


def virt_mem_status():
    """get virtual memory overall information

    :return:virt_mem_var is variable that stores vm information
    """
    virt_mem_var = psutil.virtual_memory()
    return virt_mem_var


def swp_mem_status():
    """get swap memory overall information

    :return: swp_mem_var is variable that stores swap memory information
    """
    swp_mem_var = psutil.swap_memory()
    return swp_mem_var


def io():
    """get disk io information

    :return: io_count_var is variable that stores disk io information
    """
    io_count_var = psutil.disk_io_counters()
    return io_count_var


def net_stat():
    """get network information

    :return: net_stat_var is variable that stores network interface information
    """
    net_stat_var = psutil.net_if_stats()
    return net_stat_var


def get_system_info(data_format):
    """get system information and dump it in json format or in text format

    :param data_format: data_format is variable that stores format in which
    data will be exported, it comes from config.yaml
    :return: returns system data to be written in log file in needed format
    """
    if data_format == 'json':
        data = dict()
        data['cpu_load'] = cpu_load()
        data['virt_mem_status'] = virt_mem_status()
        data['swp_mem_status'] = swp_mem_status()
        data['disk_io'] = io()
        data['net_stat'] = net_stat()
        return json.dumps(data)
    else:
        return ('CPU load                 : {0}%\n'
                'Memory statistics        : {1}%\n'
                'Virtual memory statistics: {2}%\n'
                'Disk IO statistics       : {3}%\n'
                'Network statistics       : {4}%\n'
                .format(cpu_load(),
                        virt_mem_status(),
                        swp_mem_status(),
                        io(),
                        net_stat()))
