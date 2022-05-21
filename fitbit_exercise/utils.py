def format_dates(dates):
    """
    Takes a list of dates in the format YYYY-MM-DD and returns a list of dates in the format DD/MM/YYYY
    """
    return [format_date(date) for date in dates]


def format_date(date):
    """
    Takes a date in the format YYYY-MM-DD and returns a date in the format DD/MM/YYYY
    """
    return date[8:10] + "/" + date[5:7] + "/" + date[0:4]
