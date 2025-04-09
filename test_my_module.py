from my_module import Solution


def test_twoSum():
    solution = Solution()
    result = solution.twoSum([1, 3, 5], 8)
    assert result == [1, 2]