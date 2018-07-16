import argparse
import module


def arguments():
    parser = argparse.ArgumentParser(
        description='Get info about python installation in current system',
        prog='py_versions')
    parser.add_argument('--json', '-j', dest='j', action='store_true',
                        help='Export data to json.'),
    parser.add_argument('--yaml', '-y', dest='y', action='store_true',
                        help='Export data to yaml.')
    arg = parser.parse_args().__dict__
    return arg


def write_json():
    """
    Write data to the OUTPUT.json
    :return: data in json format
    """
    with open('out.json', 'w') as file_j:
        data_json = module.form_data('json')
        file_j.write(data_json)
        file_j.close()


def write_yaml():
    """
    Write data to the OUTPUT.yaml
    :return: data in yaml format
    """
    with open('out.yaml', 'w') as file_y:
        data_yaml = module.form_data('yaml')
        file_y.write(data_yaml),
        file_y.close()


def main():
    conf = arguments()
    if conf['j']:
        write_json()
    if conf['y']:
        write_yaml()


if __name__ == '__main__':
    main()
