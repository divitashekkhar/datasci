SELECT c.value 
from

(SELECT 
    a.row_num,
    b.col_num,
    SUM(a.value * b.value ) AS value
from
    a
    join b on a.col_num=b.row_num
group by 
    a.row_num,
    b.col_num
) c

where c.row_num =2 and c.col_num=3      ;
