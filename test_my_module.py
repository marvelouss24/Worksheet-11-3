from my_module import Solution
from my_module import divide

def test_twoSum():
    solution = Solution()
    result = solution.twoSum([1, 3, 5], 8)
    assert result == [1, 2]

def test_divide():
    result = divide(10, 2)
    assert result == 5
    