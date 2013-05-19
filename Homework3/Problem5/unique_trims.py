'''
Write a MapReduce query to remove the last 10 characters
from each string of nucleotides, then remove any duplicates generated.
'''

import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input is a 2 element list: [sequence id, nucleotides]
        sequence id: Unique identifier formatted as a string
        nucleotides: Sequence of nucleotides formatted as a string
    '''
    mr.emit_intermediate( )

def reducer(key, list_of_values):
    '''
    The output should be the unique trimmed nucleotide strings.
    '''        
    mr.emit( )

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
