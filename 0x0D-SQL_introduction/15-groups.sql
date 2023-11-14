-- a script that lists the number of records with the
-- same score in the table second_table of the database hbtn_0c_0
SELECT score, COUNT(*)
	FROM hbtn_0c_0.second_table
	ORDER BY score DESC;
