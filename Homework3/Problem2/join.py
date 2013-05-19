'''
Implement a relational join as a MapReduce query
'''
import MapReduce
import sys

TABLE_1_NAME = 'order'
TABLE_2_NAME = 'line_item'

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input will be database records formatted as lists of Strings.
    The first item(index 0) in each record is a string that identifies which table the record originates from. This field has two possible values:
        line_item indicates that the record is a line item.
        order indicates that the record is an order.
    The second element(index 1) in each record is the order_id.
    '''
    table_name = record[0]
    order_id = record[1]
    table_fields = record[2:]
    
    mr.emit_intermediate( order_id, [ table_name, table_fields] )

def reducer(key, list_of_values):
    '''
    The output should be a joined record.
    '''
    table1 = [table[1] for table in list_of_values if table[0] == TABLE_1_NAME ]
    table2 = [table[1] for table in list_of_values if table[0] == TABLE_2_NAME ]

    for record1 in table1:
        for record2 in table2:
            res = []

            res.append(TABLE_1_NAME)
            res.append(key)
            res.extend(record1)
            res.append(TABLE_2_NAME)
            res.append(key)
            res.extend(record2)           

            mr.emit( res )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
