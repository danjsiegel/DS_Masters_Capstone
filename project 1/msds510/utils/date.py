import datetime

def getmonth(monthtoparse):
    '''
    :param monthtoparse: month in which avenger joined
    :return: the numerical reference of the month, or 1
    '''
    monthdict = {'Jan': 1, 'Feb': 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    for key in monthdict:
        if key in monthtoparse:
            return monthdict[key]
    return 1
def datediffcalculator(joinDate):
    '''
    :param joinDate: Date to calculate time elapsed since
    :return: Time elapsed since joinDate
    '''
    try:
        today = datetime.datetime.now().date()
        joinDate
        difference = today - joinDate
        return difference
    except:
        return None

def getDJ(inMonth, inYear):
    '''
    :param inMonth: If month available
    :param inYear: Year Avenger Returned
    :return: DateTime for first of the month of the year they joined, or first of the year
    '''
    try:
        returnYear = datetime.date(int(inYear), getmonth(inMonth), 1)
    except:
        returnYear = datetime.date(int(inYear), 1, 1)
        return returnYear
    else:
        return returnYear

def to_int(stringToMakeInt):
    '''
    :param stringToMakeInt: String Input
    :return: Int representation of the string
    '''
    return int(stringToMakeInt)
