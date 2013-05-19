'''
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value.
Design a MapReduce algorithm to compute matrix multiplication: A x B
'''

import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input to the map function will be matrix row records formatted as lists.
    Each list will have the format [matrix, i, j, value] where matrix is a string and i, j, and value are integers.
    The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values:
        'a' indicates that the record is from matrix A
        'b' indicates that the record is from matrix B
    '''
    mr.emit_intermediate( )

def reducer(key, list_of_values):
    '''
    The output from the reduce function will also be matrix row records formatted as tuples.
    Each tuple will have the format (i, j, value) where each element is an integer.
    '''        
    mr.emit()

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
