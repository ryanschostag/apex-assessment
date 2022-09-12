"""
Python3 assessment for Apex Systems, for clients: Charter Communications, Centene Corporation

    INSTRUCTIONS:
    
    - Provide solutions to the following problems in this same file below.
    - Solution must be complete and executable.
    - Code should be written in Python 3 and must adhere to PEP-8 standards.
    - Put emphasis on handling edge cases.
    - Well commented code earns brownie points.

Candidate: Ryan Schostag
"""
import re
import time
import logging
import logging.config


LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '[[%(asctime)s [%(levelname)s] PID:%(process)d %(filename)s:%(funcName)s:%(lineno)d]] %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False
        },
        'assessment': { 
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('assessment')


def timer(func, *args, **kwargs):
    def _timed(*args, **kwargs):
        start_time = time.time()
        returned_value = func(*args, **kwargs)
        run_time = time.time() - start_time
        logger.debug(f'{func} took {run_time:.7f} seconds')
        return returned_value
    return _timed


@timer
def solution_for_problem_one(n:int, *args, **kwargs) -> list:
    """
    PROBLEM 1:

    Given an integer "n", return an array "a" of length "n+1" such that for each "i" (0<=i<=n), a[i] is the number of 1's in the binary representation of "i".
    
    @n
      <int> 
    
    @returns
      <list> of integer values representing the count of 1's the binary expression of each iteration number
    
    @raises
      <TypeError>
    """
    a = []
    if not isinstance(n, int):
        raise TypeError(f'Unexpected type received: Expected <int>, but received {type(n)}')

    for i in range(0, n+1):
        i_binary = f'{i:b}'  # binary sting representation of i
        ones_count = i_binary.count('1')
        a.append(ones_count)
        logger.debug(f'Processed: {i} => {i_binary} => {ones_count}')

    return a


@timer
def solution_for_problem_two(a:str, z:str, *args, **kwargs) -> bool:
    """
    PROBLEM 2:

    Given two strings "a" and "z", return TRUE if "a" is subsequence of "z", or FALSE otherwise.

    Subsequence Definition:
        String "a" is subsequence of String "z" if the characters in String "a" appear in the same order (contiguous or otherwise) in String "z".

        NOTE: An empty string is a subsequence of every string.

    @a
      <str>
    
    @z
      <str>
    
    @returns
      <bool> "result" is False by default, Logs an error message if the inputs are not of type <str>
    
    @raises
      <TypeError>
    """
    if not isinstance(a, str) or not isinstance(z, str):
        raise TypeError(f'Unexpected type received: Please ensure both values for a ({type(a)}) and z ({type(z)}) are both of type <str>')
    
    pattern = '.*'.join(list(a))
    is_substring = bool(re.search(pattern, z))
    logger.info(f'a({a}) is a substring of z({z}): {is_substring}')
    return is_substring


def no_pytest():
    """
    Run tests this way if pytest is unavailable; 
    otherwise, run `pip install pytest` and run `pytest test_assessment.py`
    There are more tests available when running the tests in test_assessments.py 
    through pytest 
    """
    test_settings = [ 
        {
            'function': solution_for_problem_one,
            'input': (5,),
            'expect': [0,1,1,2,1,2]
        },
        {
            'function': solution_for_problem_one,
            'input': (11,),
            'expect': [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3]
        },
        {
            'function': solution_for_problem_one,
            'input': (17,),
            'expect': [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]
        },
        {
            'function': solution_for_problem_two,
            'input': ('ace', 'abcde'),
            'expect': True
        },
        {
            'function': solution_for_problem_two,
            'input': ('aec', 'abcde'),
            'expect': False
        },
        {
            'function': solution_for_problem_two,
            'input': ('abfg', 'abcdefgh'),
            'expect': True
        },
        {
            'function': solution_for_problem_two,
            'input': ('howlnso', 'ilikehowlingatnightbecauseimawerewolfwithinsomnia'),
            'expect': True
        },
    ]
    for settings in test_settings:
        inputs = settings.get('input')
        function = settings.get('function')
        assert function(*inputs) == settings.get('expect')
    return True


if __name__ == "__main__":
    logger.info(f'Initialized assessment')

    result = no_pytest()
    if result is True:
        return_code = 0  # success
    else:
        return_code = 1  # fail

    logger.info(f'Completed assessment with return code {return_code}')

    

