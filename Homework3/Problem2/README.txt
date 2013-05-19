Implement a relational join as a MapReduce query


Consider the query:


SELECT * 

FROM Orders, LineItem 

WHERE Order.order_id = LineItem.order_id


Your MapReduce query should produce the same information as this SQL query.  You can consider the two input tables, Order and LineItem, as one big concatenated bag of records which gets fed into the map function record by record. 