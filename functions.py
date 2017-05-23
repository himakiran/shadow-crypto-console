import sys


def find_between(inputStr, firstSubstr, lastSubstr):
    start, end = (-1, -1)

    try:
        start = inputStr.index(firstSubstr) + len(firstSubstr)
    except ValueError:
        print '    ValueError: ',
        print "firstSubstr=%s  -  " % firstSubstr,
        print sys.exc_info()[1]

    try:
        end = inputStr.index(lastSubstr, start)
    except ValueError:
        print '    ValueError: ',
        print "lastSubstr=%s  -  " % lastSubstr,
        print sys.exc_info()[1]

    return inputStr[start:end]


__author__ = 'Shadow | shadowsgovernment.com'
