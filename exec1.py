# -*- coding: utf-8 -*-
import re
from itertools import cycle


test_case_number = 0
positive_integer_pattern = re.compile("^[1-9]+[0-9]*$")

class Node(object):

    def __init__(self, visit=False):
        self.visit = visit


class Matrix(object):

    def __init__(self, rows, columns):
        self.steps = 0
        self.total_steps = columns * rows
        self.list_direction = cycle(['R', 'D', 'L', 'U'])
        self.dict_direction_points = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
        self.direction = next(self.list_direction)
        self.matrix = [[Node() for x in range(columns)] for y in range(rows)]

    def walk(self, row=0, column=0):
        if self.total_steps <= 1:
            pass
        else:
            while self.steps < self.total_steps:
                try:
                    pmatrix = self.matrix[row][column]
                    if not pmatrix.visit:
                        pmatrix.visit = True
                        self.steps += 1
                    else:
                        row = row - self.dict_direction_points[self.direction][0]
                        column = column - self.dict_direction_points[self.direction][1]
                        self.direction = next(self.list_direction)
                except IndexError:
                    row = row - self.dict_direction_points[self.direction][0]
                    column = column - self.dict_direction_points[self.direction][1]
                    self.direction = next(self.list_direction)
                finally:
                    row = row + self.dict_direction_points[self.direction][0]
                    column = column + self.dict_direction_points[self.direction][1]
        return self.direction


class Result(object):

    def __init__(self):
        self.element_list = []

    def append_element(self,element):
        self.element_list.append(element)

    def print_result(self):
        for ele in self.element_list:
            if hasattr(ele,'walk'):
                print(ele.walk())


def build_matrix(msg, plist, value=''):
    while not isinstance(value, int):
        value = input("Enter the {} number:".format(msg))
        if positive_integer_pattern.match(value):
            value = int(value)
    plist.append(value)


def program_data():
    global test_case_number
    test_case_number = input("Enter test case number:")
    if positive_integer_pattern.match(test_case_number):
        test_case_number = int(test_case_number)
        result = Result()
        for i in range(test_case_number):
            print('Case {}'.format(i + 1))
            plist = []
            build_matrix('rows', plist)
            build_matrix('colums', plist)
            result.append_element(Matrix(*plist))
        result.print_result()
    else:
        program_data()


program_data()
