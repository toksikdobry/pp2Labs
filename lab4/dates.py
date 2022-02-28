import datetime
def substractFiveDays():
    d = list(map(int, input().split()))
    date = datetime.date(d[0], d[1], d[2])
    newDate = date - datetime.timedelta(5)
    print(newDate)

def yesTodTom():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(1)
    tomorrow = today + datetime.timedelta(1)
    print(yesterday, today, tomorrow)

def dropMicroSeconds():
    d = list(map(int, input().split()))
    date = datetime.datetime(d[0], d[1], d[2], d[3], d[4], d[5], d[6]).replace(microsecond=0)
    print(date)

def difInSec():
    a = list(map(int, input().split()))
    firstDate = datetime.datetime(a[0], a[1], a[2])
    b = list(map(int, input().split()))
    secondDate = datetime.datetime(b[0], b[1], b[2])
    dif = secondDate - firstDate
    print(dif.days * 24 * 3600)

#substractFiveDays()
#yesTodTom()
#dropMicroSeconds()
#difInSec()
