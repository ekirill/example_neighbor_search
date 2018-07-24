# -*- coding: utf-8 -*-


def OK_RESULT(data=None):

    result = {
        'status': 'OK',
    }
    if data:
        result['data'] = data

    return result


def FAIL_RESULT(errors):
    result = {
        'status': 'FAIL',
        'errors': errors
    }

    return result
