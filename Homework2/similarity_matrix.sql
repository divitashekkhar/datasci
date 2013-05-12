SELECT C.value 
from

(
SELECT 
    A.docid as doc1,
    B.docid as doc2,
    SUM(a.[count] * b.[count] ) AS value
from
    frequency A
    join frequency B on A.term=B.term
where A.docid < B.docid
group by 
    A.docid,
    B.docid

) C

where  C.doc1 = '10080_txt_crude' and C.doc2 = '17035_txt_earn'    
;