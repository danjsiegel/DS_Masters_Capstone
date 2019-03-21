import sys

def argumentExists(index):
    '''This function takes argv positions and attempts to return them.
	In the event that an argument is out of bounds of the array, it will return a null string and prevent the program from crashing.
	Arguments are argv positions
	'''
    try:
        sys.argv[index]
    except IndexError:
        return None
    else:
        return sys.argv[index]

def make_nice_name(headerToFix):
    '''
    :param headerToFix: Raw header
    :return: Header in lowercase, removing special characters, and whitespace
    '''
    headerToFix = headerToFix.lower()
    headerToFix = headerToFix.strip('\n').strip('?').rstrip().lstrip()
    headerToFix = headerToFix.replace('/','_').replace(' ', '_')
    return headerToFix

def to_bool(stringToMakeBool):
    '''
    :param stringToMakeBool: Potential boolean value
    :return: True, False or None
    '''
    stringToMakeBool=stringToMakeBool.lower()
    if stringToMakeBool == "yes":
        return True
    elif stringToMakeBool == "no":
        return False
    else:
        return None
