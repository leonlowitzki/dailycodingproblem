import collections


def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
                                    for funcargs in funcarglist])


# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def add_up_to_k(arr, k):
    if not isinstance(arr, collections.abc.Sequence) or not isinstance(k, (int, float, complex)):
        return None
    possible_solutions = set()
    for num in arr:
        if num + num == k or num in possible_solutions:
            return True
        possible_solutions.add(k - num)
    return False


class TestProblem1:
    params = {
        'test_add_up_to_k': [dict(arr=[10, 15, 3, 7], k=17, expected=True),
                             dict(arr=[10, 15, 3], k=17, expected=False),
                             dict(arr=[1], k=2, expected=True),
                             dict(arr=[-1], k=-2, expected=True),
                             dict(arr=[-1, -10], k=-11, expected=True),
                             dict(arr=[], k=0, expected=False),
                             dict(arr=None, k=0, expected=None),
                             dict(arr=[1], k=None, expected=None),
                             dict(arr=None, k=None, expected=None)]
    }

    def test_add_up_to_k(self, arr, k, expected):
        actual = add_up_to_k(arr, k)
        assert actual == expected
