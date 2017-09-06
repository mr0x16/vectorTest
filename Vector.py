from math import *
#from  decimal import Decimal, getcontext
#getcontext().prec = 30


class Vector(object):

        CANNOT_NORMAILZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
        TOLERANCE = 10e-10
        def __init__(self, coordinates):
            try:
                if not  coordinates:
                    raise ValueError
                self.coordinates = tuple([x for x in coordinates])
                self.dimension = len(coordinates)

            except ValueError:
                raise ValueError('The coordinates must be nonempty')

            except TypeError:
                raise TypeError('The coordinates must be an iterable')

        def __str__(self):
            return 'Vector: {}'.format(self.coordinates)

        def __eq__(self, other_v):
            return self.coordinates == other_v.coordinates

        def plus(self, other_v):
            res_v = [x + y for x, y in zip(self.coordinates, other_v.coordinates)]
            return Vector(res_v)

        def minus(self, other_v):
            res_v = [x - y for x, y in zip(self.coordinates, other_v.coordinates)]
            return Vector(res_v)

        def times_scalar(self, scalar):
            res_v = [scalar * x for x in self.coordinates]
            return Vector(res_v)

        def magnitude(self):
            coordinates_squared = [x**2 for x in self.coordinates]
            return sqrt(sum(coordinates_squared))

        def normalized(self):
            try:
                magnitude = self.magnitude()
                return self.times_scalar(1./magnitude)
            except ZeroDivisionError:
                raise Exception(self.CANNOT_NORMAILZE_ZERO_VECTOR_MSG)

        def dot_product(self, other_v):
            dot_list = [x * y for x, y in zip(self.coordinates, other_v.coordinates)]
            return sum(dot_list)
            pass

        def angle(self, other_v, in_degrees=False):
            try:
                #numerator = self.dot_product(other_v)#分子
                #denominator = self.magnitude()*other_v.magnitude()#分母
                u1 = self.normalized()
                u2 = other_v.normalized()
                angle_in_radians = acos(u1.dot_product(u2))
                if in_degrees:
                    degrees_per_radian = 180./pi
                    return angle_in_radians * degrees_per_radian
                else:
                    return angle_in_radians

            except Exception as e:
                if str(e) == self.CANNOT_NORMAILZE_ZERO_VECTOR_MSG:
                    raise Exception('Cannot compute an angle with the zero vector')
                else:
                    raise e
            pass

        def is_parallel_with(self, other_v):
            #只要有一个向量是零向量，则认为两个向量平行
            if self.magnitude() == 0:
                return True
            elif other_v.magnitude() == 0:
                return True
            elif abs(abs(self.normalized().dot_product(other_v.normalized())) -1) < self.TOLERANCE:
                #标准化之后内积的绝对值和1的差距在方差内的，认为是平行向量
                return True
            else:
                return False
            pass

        def is_orthogonal_with(self, other_v):
            if abs(self.dot_product(other_v)) < self.TOLERANCE:
                #内积在方差内的就认为两个向量垂直
                return True
            else:
                return False
            pass

        def projection_vector_with(self, other_v):
            try:
                uv = other_v.normalized()
                projections_vector = uv.times_scalar((self.dot_product(uv)))
                return projections_vector
            except Exception as e:
                if str(e) == self.CANNOT_NORMAILZE_ZERO_VECTOR_MSG:
                    raise Exception(self.CANNOT_NORMAILZE_ZERO_VECTOR_MSG)
                else:
                    raise e
            pass

        def orthogonal_vector_with(self, other_v):
            try:
                return self.minus(self.projection_vector_with(other_v))
            except Exception as e:
                if str(e) == self.CANNOT_NORMAILZE_ZERO_VECTOR_MSG:
                    raise Exception(self.CANNOT_NORMAILZE_ZERO_VECTOR_MSG)
                else:
                    raise e
            pass

        def cross_product(self, other_v):
            try:
                x_1, y_1, z_1 = self.coordinates
                x_2, y_2, z_2 = other_v.coordinates
                element0 = y_1*z_2 - y_2*z_1
                element1 = x_2*z_1 - x_1*z_2
                element2 = y_1*x_2 - y_2*x_1
                return Vector([element0,element1,element2])
            except ValueError as e:
                msg = str(e)
                if msg == 'need more then 2 values to unpack':
                    self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                    v_embedded_in_R3 = Vector(other_v.coordinates + ('0',))
                    return self_embedded_in_R3.cross_product(v_embedded_in_R3)
                elif (msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack'):
                    raise Exception('the vector have too many dims')
                else:
                    raise e
                pass

        def triangle_area_with(self, other_v):
            try:
                return self.parallelogram_area_with(other_v)/2

            except Exception as e:
                raise e
            pass

        def parallelogram_area_with(self, other_v):
            try:
                cross_product_vector = self.cross_product(other_v)
                return cross_product_vector.magnitude()

            except Exception as e:
                raise e
            pass