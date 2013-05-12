REM Problems in initial order

sqlite3 reuters.db < select.sql 	> select.txt
sqlite3 reuters.db < select_project.sql > select_project.txt
sqlite3 reuters.db < union.sql 		> union.txt
sqlite3 reuters.db < count.sql 		> count.txt
sqlite3 reuters.db < big_documents.sql 	> big_document.txt
sqlite3 reuters.db < two_words.sql 	> two_words.txt

PAUSE

sqlite3 matrix.db  < mulptiply.sql 	> multiply.txt

sqlite3 reuters.db < similarity_matrix.sql 	> similarity_matrix.txt

sqlite3 reuters.db < keyword_search.sql	> keyword_search.txt

PAUSE