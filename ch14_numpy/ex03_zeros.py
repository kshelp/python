import numpy as np

print(np.zeros(10))
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

print(np.zeros((3, 4)))
'''
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''

print(np.ones(5))   # [1. 1. 1. 1. 1.]

print(np.ones((3, 5)))
'''
[1. 1. 1. 1. 1.]
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''

print(np.eye(3))
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''