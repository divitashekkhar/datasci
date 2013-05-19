'''
Implement a relational join as a MapReduce query
'''
import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input will be database records formatted as lists of Strings.
    '''
    mr.emit_intermediate()

def reducer(key, list_of_values):
    '''
    The output should be a joined record.
    '''     
    mr.emit( (key,result) )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
