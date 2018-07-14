import argparse
import calendar
from datetime import datetime
import getpass
import requests


def arguments():
    """function describes usage of arguments

    :return: returns json file and list of arguments
    """
    parser = argparse.ArgumentParser(description='Script is meant to get'
                                                 'PR statistics and other'
                                                 ' information.'
                                                 'Call command with '
                                                 '-H for help')
    parser.add_argument('--version', '-v', action='version',
                        version='%(prog)s 1.0', help='Get information about '
                                                     'software version.')
    parser.add_argument('--user', '-u', dest='u', required='true',
                        help='User whose stats are gathered (required).')
    parser.add_argument('--repo', '-r', dest='r', required='true',
                        help='Repository to work with (required).')
    parser.add_argument('--opened', '-o', dest='o', action='store_true',
                        help='User who opened pull request.')
    parser.add_argument('--stat', '-s', dest='s', action='store_true',
                        help='Show merged closed statistics.')
    parser.add_argument('--week', '-w', dest='w', action='store_true',
                        help='Day of the week PR was created.')
    parser.add_argument('--days-opened', '-do', dest='do',
                        action='store_true',
                        help='Number of days PR is opened')
    parser.add_argument('--day', '-d', dest='d', action='store_true',
                        help='Date when PR was created.')

    arg = parser.parse_args().__dict__
    arg['login'] = input('Enter github login: ')
    arg['password'] = getpass.getpass(prompt='Enter password: ', stream=None)

    url = 'https://api.github.com/repos/' + arg['u'] + '/' + \
          arg['r'] + '/pulls?page=1&per_page=100'
    r = requests.get(url, auth=(arg['login'], arg['password']))
    r = r.json()
    return arg, r


def stat_merged_closed(r):
    """function to get number of merged and closed PR

    :param r: json data to parse
    :return: String with numbers of merged/closed PR
    """
    merged_var = 0
    closed_var = 0
    for pr in range(len(r)):
        if r[pr]["merged at"]:
            closed_var += 1
        if r[pr]["closed at"]:
            merged_var += 1
    print('%s pull requests were merged. %s pull requests were closed.'
          % (merged_var, closed_var))
    if merged_var:
        if closed_var:
            ratio = merged_var / float(closed_var)
            print('Ratio is %s' % ratio)


def pr_opened_weekday(r):
    """function to get weekday PR was created

    :param r: json data to parse
    :return: String with PR title and creation weekday
    """
    for pr in r:
        title = pr['title']
        day = pr['created_at'][:10]
        day = datetime.strptime(day, '%Y-%m-%d').date()
        weekday = calendar.day_name[day.weekday()]
        print('PR "%s" was created on %s' % (title, weekday))


def pr_opened_date(r):
    """function to get date PR was created

    :param r: json data to parse
    :return: String with PR title and creation date
    """
    for pr in r:
        title = pr['title']
        day = pr['created_at'][:10]
        date = datetime.strptime(day, '%Y-%m-%d').date()
        print('PR "%s" was created on %s' % (title, date))


def pr_opened_by(r):
    """Function to get login of user who created PR

    :param r: json data to parse
    :return: String with login information, id and title of PR
    """
    for pr in r:
        title = pr['title']
        pr_id = pr['id']
        user = pr['user']['login']
        print('PR %s with id %s was opened by %s' % (title, pr_id, user))


def pr_opened_days(r):
    """Function to get number of days PR is opened

    :param r: Json data to parse
    :return: String with title and number of days of PR
    """
    for pr in r:
        title = pr['title']
        day = pr['created_at'][:10]
        day = datetime.strptime(day, '%Y-%m-%d').date()
        days = (datetime.now().date() - day).days
        print('PR %s exists for %s days already!' % (title, days))
