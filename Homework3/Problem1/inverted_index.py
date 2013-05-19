'''
Create an Inverted index. Given a set of documents, an inverted index is a dictionary 
where each word is associated with a list of the document identifiers in which that word appears.
'''
import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input is a 2 element list: [document_id, text]
    document_id: document identifier formatted as a string
    text: text of the document formatted as a string
    '''
    key = record[0]
    value = record[1]
    
    for word in value.split():
       mr.emit_intermediate(word,key)

def reducer(key, list_of_values):
    '''
    The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.
    '''     
    result = []
    
    #want to remove duplicates
    #might use set(), but got some bug which did not want to solve
    for document_ID in list_of_values:
        if document_ID not in result:
            result.append(document_ID) 
    mr.emit( (key,result) )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)