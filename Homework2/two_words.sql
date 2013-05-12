Select count(*)
from
(
        (SELECT docid
        from frequency
        where term = "world" ) t1

    join

        (SELECT docid
        from frequency
        where term = "transactions" ) t2
    on  t1.docid=t2.docid  
)   ;