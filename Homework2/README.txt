HOMEWORK 2 Simple in data-base analytics



The goal is to run  som sql queries to db and submit results

In order to do the task I use sqlite client from command line

sqlite3 [database_file.db] < [problem_name.sql] > [problem_name.txt]

sqlite3 - you can download from http://www.sqlite.org/download.html  >> precompiled binaries for windows

[database_file] - I work reuters.db which I do not upload due to its size. Database has the following schema:

CREATE TABLE Frequency (
docid VARCHAR(255),
term VARCHAR(255),
count int,
PRIMARY KEY(docid, term));

[problem_name.sql] - I name it the same way as original problem it solved with sql extensions, result i put in file with txt extension [problem_name.txt]