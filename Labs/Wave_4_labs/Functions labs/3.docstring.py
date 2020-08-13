def readable_timedelta(days):
    # insert your docstring here
    """Returns a string of the number of week(s) and day(s) in the given days.

    Args:
        days (int): number of days to convert
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
