def date_format(num):
    month, date, year = num.split("/")
    str = "{}-{}-{}".format(year, month, date)
    return str