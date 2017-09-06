from decimal import Decimal, getcontext
from Vector import *

getcontext().prec = 30

class Line(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'NO nonzero element found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = [0]*self.dimension
            normal_vector = Vector(all_zeros)
            pass
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = constant_term

        self.set_basepoint()
        # self
        pass

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n.coordinates)
            initial_coefficient = n.coordinates[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)
            pass
        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
                pass
            else:
                raise e
            pass
        pass

    def __str__(self):
        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)
                pass

            output = ''
            if coefficient < 0:
                output += '-'
                pass
            if coefficient > 0 and not is_initial_term:
                output += '+'
                pass

            if not is_initial_term:
                output += ' '
                pass

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))
                pass
            return output
            pass

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n.coordinates)
            terms = [write_coefficient(n.coordinates[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1) for i in range(self.dimension) if round(n.coordinates[i], num_decimal_places) != 0]
            output = ' '.join(terms)
            pass
        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
                pass
            else:
                raise e
            pass

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
            pass
        output += ' = {}'.format(constant)

        return output

    def is_parallel_with(self, other_l):
        if self.normal_vector.normalized().is_parallel_with(other_l.normal_vector.normalized()):
            if self.is_same_with(other_l):
                return True
                pass
            else:
                print('%s and %s are parallel' % (self, other_l))
                return True
        else:
            return False
        pass

    def is_same_with(self, other_l):
        link_vector = self.basepoint.minus(other_l.basepoint)
        if link_vector.is_orthogonal_with(self.normal_vector):
            print('%s and %s are same' % (self, other_l))
            return True
        else:
            return False
        pass

    def intersection_with(self,other_l):
        if self.is_parallel_with(other_l):
            print('there are no intersection bewtten %s and %s' % (self, other_l))
            return None
        else:
            if self.dimension == 2 and other_l.dimension == 2:
                A = self.normal_vector.coordinates[0]
                B = self.normal_vector.coordinates[1]
                C = other_l.normal_vector.coordinates[0]
                D = other_l.normal_vector.coordinates[1]
                alpha = A*D - B*C
                k1 = self.constant_term
                k2 = other_l.constant_term
                x = (D*k1 - B*k2)/alpha
                y = (A*k2 - C*k1)/alpha
                intersection = Vector([x, y])
                print('intersection is %s' % intersection)
                return intersection
                pass
            pass


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not Decimal_EXT(item).is_near_zero():
                return k
            pass
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)
        pass

class Decimal_EXT(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps