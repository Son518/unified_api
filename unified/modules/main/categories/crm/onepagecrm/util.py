from datetime import datetime, timezone

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def date_format_to_epoch(date):
    ''' convert date format to epoch'''

    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").timestamp()
     