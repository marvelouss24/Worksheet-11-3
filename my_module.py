import matplotlib.pylab as plt
import numpy as np
import random

def generate_plot(function, start, end):
    x_values = np.linspace(start, end, 50)
    y_values = function(x_values)

    plt.plot(x_values, y_values)
    plt.show()

class Chooser:
    def __init__(self, list = [1, 2, 3, 4, 5, 6]):
        self.list = list
        self.value = self.list[random.randint(0, len(self.list) - 1)]
    
    def get_value(self):
        return self.value
    
    def select(self):
        self.value = self.list[random.randint(0, len(self.list) - 1)]
        return self.value

#answer to Two Sum from leetcode
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def divide(a, b):
    return a / b