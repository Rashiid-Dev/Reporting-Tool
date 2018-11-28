from __future__ import print_function
import psycopg2

conn = psycopg2.connect("dbname=news")

c = conn.cursor()
# candidate is jerk views
#query = "select count(path) from log where path LIKE '%jerk%' and status LIKE '%200%'"
# c.execute(query)

# returns the top 3 articles
query1 = "select count(*) as num from log where status LIKE '%200%' and path != '/' group by path order by num desc limit 3"
c.execute(query1)


results = c.fetchall()

# prints all results
# print(results[0])

# selects the first value from the results
# print(results[0])

print('"Candidate is jerk, alleges rival" - ' + str(results[0][0]) + ' views')

conn.close()

# joins auth and log and select authors name from authors and slugs from articles
#query= "select name,slug from authors join articles on authors.id=articles.author;"

# conn.commit()

# conn.close()


# news=> select count(path) from log where path LIKE '%jerk%';
# count
#--------
# 342102
#(1 row)
# join the path and article and then add the view to the end as a string using the count
#
#selects all articles where Markoff is the author
#select * from articles where author in (select id from authors where name LIKE '%Mark%');
#
#removes /article/ from the path and also shows how it was before
#select replace(path , '/article/', ''), path from log;
#
#
#
