import datetime
from dateutil.relativedelta import relativedelta

def formatDate(dateValue):
    zeroTime = datetime.time(0,0,0)
    formattedDateTime = datetime.datetime.combine(dateValue,zeroTime)
    return formattedDateTime

def getFormattedYesterday(timeElement):
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    
    if timeElement:
        yesterday = formatDate(today - one_day)
    else:
        yesterday = today - one_day
    
    return yesterday

def getEnbwDateRange():
    today = datetime.date.today()
    one_month = relativedelta(months=+1)
    last_monthDate = today - one_month
    first_day_last_month = last_monthDate + relativedelta(day=1)
    first_day_last_month = formatDate(first_day_last_month)
    today = formatDate(today)
    return first_day_last_month,today
