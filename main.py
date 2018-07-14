import module


def main():
    conf, request = module.arguments()
    if conf['s']:
        module.stat_merged_closed(request)
    if conf['o']:
        module.pr_opened_by(request)
    if conf['w']:
        module.pr_opened_weekday(request)
    if conf['d']:
        module.pr_opened_date(request)
    if conf['do']:
        module.pr_opened_days(request)


if __name__ == '__main__':
    main()
