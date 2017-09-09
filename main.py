from Vector import *
from line import *
# vector_pair1_1 = Vector([-7.579,-7.88])
# vector_pair1_2 = Vector([22.737, 23.64])
# print(vector_pair1_1.is_parallel_with(vector_pair1_2))
# print(vector_pair1_1.is_orthogonal_with(vector_pair1_2))
#
# vector_pair2_1 = Vector([-2.029, 9.97, 4.172])
# vector_pair2_2 = Vector([-9.231, -6.639, -7.245])
# print(vector_pair2_1.is_parallel_with(vector_pair2_2))
# print(vector_pair2_1.is_orthogonal_with(vector_pair2_2))
#
# vector_pair3_1 = Vector([-2.328, -7.284, -1.214])
# vector_pair3_2 = Vector([-1.821, 1.072, -2.94])
# print(vector_pair3_1.is_parallel_with(vector_pair3_2))
# print(vector_pair3_1.is_orthogonal_with(vector_pair3_2))
#
# vector_pair4_1 = Vector([2.118, 4.827])
# vector_pair4_2 = Vector([0,0])
# print(vector_pair4_1.is_parallel_with(vector_pair4_2))
# print(vector_pair4_1.is_orthogonal_with(vector_pair4_2))
#
# vector_pair5_1 = Vector([3.039, 1.879])
# vector_pair5_2 = Vector([0.825, 2.036])
# print(vector_pair5_1.projection_vector_with(vector_pair5_2))
#
# vector_pair6_1 = Vector([-9.88, -3.264, -8.159])
# vector_pair6_2 = Vector([-2.155, -9.353, -9.473])
# print(vector_pair6_1.orthogonal_vector_with(vector_pair6_2))
#
# vector_pair7_1 = Vector([3.009, -6.172, 3.692, -2.51])
# vector_pair7_2 = Vector([6.404, -9.144, 2.759, 8.718])
# print(vector_pair7_1.projection_vector_with(vector_pair7_2))
# print(vector_pair7_1.orthogonal_vector_with(vector_pair7_2))
#
# vector_pair8_1 = Vector([8.462, 7.893, -8.187])
# vector_pair8_2 = Vector([6.984, -5.975, 4.778])
# print(vector_pair8_1.cross_product(vector_pair8_2))
#
# vector_pair9_1 = Vector([-8.987, -9.838, 5.031])
# vector_pair9_2 = Vector([-4.268, -1.861, -8.866])
# print(vector_pair9_1.parallelogram_area_with(vector_pair9_2))
#
# vector_pair10_1 = Vector([1.5, 9.547, 3.691])
# vector_pair10_2 = Vector([-6.007, 0.124, 5.772])
# print(vector_pair10_1.triangle_area_with(vector_pair10_2))
print('#1')
normal_vector1_1 = Vector([4.046, 2.836])
constant_1_1 = 1.21
line_1_1 = Line(normal_vector1_1,constant_1_1)
normal_vector1_2 = Vector([10.115, 7.09])
constant_1_2 = 3.025
line_1_2 = Line(normal_vector1_2, constant_1_2)
line_1_1.intersection_with(line_1_2)

print('\n#2')
normal_vector2_1 = Vector([7.204, 3.182])
constant_2_1 = 8.68
line_2_1 = Line(normal_vector2_1,constant_2_1)
normal_vector2_2 = Vector([8.172, 4.114])
constant_2_2 = 9.883
line_2_2 = Line(normal_vector2_2, constant_2_2)
line_2_1.intersection_with(line_2_2)

#第三部分
print('\n#3')
normal_vector3_1 = Vector([1.182, 5.562])
constant_3_1 = 6.744
line_3_1 = Line(normal_vector3_1,constant_3_1)
normal_vector3_2 = Vector([1.773, 8.343])
constant_3_2 = 9.525
line_3_2 = Line(normal_vector3_2, constant_3_2)
line_3_1.intersection_with(line_3_2)