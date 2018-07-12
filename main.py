import datetime
import module
import time
import yaml


with open('config.yaml', 'r') as config:
    config_file = yaml.load(config)

interval = config_file['interval']
data_format = config_file["output"]
iterator = 0


def main():
    """main function writes system information in log file

    :return: returns log.txt with system information
    """
    time_format = datetime.datetime.fromtimestamp(time.time())\
        .strftime('%d.%m.%Y %H:%M:%S')

    logging = open('log.txt', "a+")
    logging.write('\nSNAPSHOT {0}: {1}\n{2}\n'.format(
        iterator,
        time_format,
        module.get_system_info(data_format)))

    logging.close()


if __name__ == '__main__':
    while True:
        main()
        iterator += 1
        time.sleep(interval)
