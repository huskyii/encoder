__author__ = 'jiang'


def add_pre_zero(code, diff):
    """a helper method that add pre-zero to code

    arguments:
        code    code that needs to add pre-zero
        diff    number of how many zero should be added

    return
        code with correct length
    """
    tmp = ''
    for c in code :
        tmp += c
        if c == 'b':
            for i in range(diff):
                tmp += '0'
    return tmp


def is_parameter_legal(signals):
    if isinstance(signals,list) and sum(signals) == 1:
        return True
    return False