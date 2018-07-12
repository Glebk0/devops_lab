import json
import psutil


class Monitor(object):

    def __init__(self, data_format):
        """gathering all necessary system information amd defining data format

        :param data_format: data_format is variable that stores format in which
        data will be exported, it comes from config.yaml
        """
        self.data_format = data_format
        self.cpu_load = psutil.cpu_percent(interval=5, percpu=False)
        self.virt_mem_status = psutil.virtual_memory()
        self.swp_mem_status = psutil.swap_memory()
        self.io = psutil.disk_io_counters()
        self.net_stat = psutil.net_if_stats()

    def get_system_info(self):
        """dump system information gathered in file in json format or in text format

        :param data_format: data_format is variable that stores format in which
        data will be exported, it comes from config.yaml
        :return: returns system data to be written in log file in needed format
        """
        if self.data_format == 'json':
            data = dict()
            data['cpu_load'] = self.cpu_load
            data['virt_mem_status'] = self.virt_mem_status
            data['swp_mem_status'] = self.swp_mem_status
            data['disk_io'] = self.io
            data['net_stat'] = self.net_stat
            return json.dumps(data)
        else:
            return ('CPU load                 : {0}%\n'
                    'Memory statistics        : {1}%\n'
                    'Virtual memory statistics: {2}%\n'
                    'Disk IO statistics       : {3}%\n'
                    'Network statistics       : {4}%\n'
                    .format(self.cpu_load,
                            self.virt_mem_status,
                            self.swp_mem_status,
                            self.io,
                            self.net_stat))
