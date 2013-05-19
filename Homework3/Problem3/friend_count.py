
'''
MapReduce algorithm to count he number of friends each person has
'''

import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input is a 2 element list: [personA, personB]
        personA: Name of a person formatted as a string
        personB: Name of one of personA 's friends formatted as a string
    This implies that personB is a friend of personA, but it does not imply that personA is a friend of personB
    '''
    person = record[0]
    mr.emit_intermediate( person, 1)

def reducer(person, list_of_values):
    '''
    The output should be a (person,  friend count) tuple.
    person is a string and friend count is an integer describing the number of friends person has.
    '''        
    mr.emit( ( person, len(list_of_values)) )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
