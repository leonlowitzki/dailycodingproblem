def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
                                    for funcargs in funcarglist])


# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def product_of_all_except_i(arr):
    result = []
    length = len(arr)
    for i in range(length):
        product = 1
        for j in range(length):
            if j != i:
                product *= arr[j]
        result.append(product)
    return result


class TestProblem2:
    params = {
        'test_product_of_all_except_i': [dict(arr=[1, 2, 3, 4, 5], expected=[120, 60, 40, 30, 24]),
                                         dict(arr=[3, 2, 1], expected=[2, 3, 6]),
                                         dict(arr=[], expected=[]),
                                         dict(arr=[-3, -2, -1], expected=[2, 3, 6]),
                                         dict(arr=[-1, -2, -3, -4], expected=[-24, -12, -8, -6]),
                                         ]}

    def test_product_of_all_except_i(self, arr, expected):
        actual = product_of_all_except_i(arr)
        assert actual == expected
