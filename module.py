import json
import psutil


def cpu_load():
    """get cpu_load information
    :return:
    """
    cpu_load_var = psutil.cpu_percent(interval=5, percpu=False)
    return cpu_load_var


def virt_mem_status():
    """get virtual memory overall information
    :return:
    """
    virt_mem_var = psutil.virtual_memory()
    return virt_mem_var


def swp_mem_status():
    swp_mem_var = psutil.swap_memory()
    return swp_mem_var


def io():
    io_count_var = psutil.disk_io_counters()
    return io_count_var


def net_stat():
    net_stat_var = psutil.net_if_stats()
    return net_stat_var


def get_system_info(data_format):

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
