'''

'''

import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    '''
    mr.emit_intermediate( )

def reducer(person, list_of_values):
    '''
    '''        
    mr.emit(  )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
