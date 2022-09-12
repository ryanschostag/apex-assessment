"""
Test module for assessment.py
"""
from multiprocessing.util import abstract_sockets_supported
import pytest
import assessment


@pytest.mark.parametrize('test_integer, raises_error, correct_answer', [
    (5, False, [0,1,1,2,1,2]),
    (11, False, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3]),
    (17, False, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]),
    ('five', True, [])
])
def test_solution_one(test_integer, raises_error, correct_answer):
    if raises_error is True:
        with pytest.raises(TypeError):
            assert assessment.solution_for_problem_one(test_integer)
    else:
        assert assessment.solution_for_problem_one(test_integer) == correct_answer


@pytest.mark.parametrize('test_string_a, test_string_b, raises_error, correct_answer', [
    ('ace', 'abcde', False, True),
    ('aec', 'abcde', False, False),
    ('abfg', 'abcdefgh', False, True),
    ('howlnso', 'ilikehowlingatnightbecauseimawerewolfwithinsomnia', False, True),
    (12378, 'abcde', True, None),
])
def test_solution_two(test_string_a, test_string_b, raises_error, correct_answer):
    if raises_error:
        with pytest.raises(TypeError):
            assessment.solution_for_problem_two(test_string_a, test_string_b)
    else:
        assert assessment.solution_for_problem_two(test_string_a, test_string_b) == correct_answer
