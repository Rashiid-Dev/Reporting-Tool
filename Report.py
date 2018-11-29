from __future__ import print_function
import psycopg2

conn = psycopg2.connect("dbname=news")

c = conn.cursor()
# candidate is jerk views
# query = "select count(path) from log where path LIKE '%jerk%' and status LIKE '%200%'"
# c.execute(query)

# returns the top 3 articles
query1 = "select count(*) as num from log where status LIKE '%200%' and path != '/' group by path order by num desc limit 3"

# counts all the paths that are articles
query2 = "select replace(path , '/article/', ''), count(*) as num from log where path != '/' group by path order by num desc limit 3"

# creates a view with path altered
view_query = """ create view truepath as
                 select replace(path , '/article/', ''), ip, method, status, time, id from log where path != '/'
             """

# selects truepath
show_view = "select * from truepath"

# joining truepath and articles get the titles
jointrueart = "select * from articles join truepath on articles.slug=truepath.path;"
#"select name,slug from authors join articles on authors.id=articles.author;"


def topthreenum():
    c.execute(query1)
    results = c.fetchall()
    return results


def topthreename():
    c.execute(query2)
    results = c.fetchall()
    return results


def queryview():
	c.execute(view_query)
	results = c.fetchall()
    return results

def showview():
    c.execute(show_view)
    results = c.fetchall()
    return results

def jointhem():
    c.execute(jointrueart)
    results = c.fetchall()
    return results


# prints all results
# print(results[0])

# selects the first value from the results
# print(results[0])


print("\nMost popular articles")
print("_____________________\n")
# print('"Candidate is jerk, alleges rival" - ' + str(topthreenum()[0][0]) + ' views\n')
# print('"Bears love berries, alleges bear" - ' + str(topthreenum()[1][0]) + ' views\n')
# print('"Bad things gone, say good people" - ' + str(topthreenum()[2][0]) + ' views\n')
# print("Query 2 Starting ......")
# print(topthreename())
for a, b in topthreename():
    print(a, "-", b, "views")

# creating views
print(jointhem())


# print(str(topthreename()[a][0]) + " - " + str(topthreename()[a][1]) + " views")

conn.close()

# joins auth and log and select authors name from authors and slugs from articles
# query= "select name,slug from authors join articles on authors.id=articles.author;"

# conn.commit()

# conn.close()
# select title, count(*) as num from articles join log on(select replace(path, '/article/', '') from log) = articles.title group by articles.title order by num

# news=> select count(path) from log where path LIKE '%jerk%';
# count
#--------
# 342102
#(1 row)
# join the path and article and then add the "view" to the end as a string using the count
#
# selects all articles where Markoff is the author
# select * from articles where author in (select id from authors where name LIKE '%Mark%');
#
# removes /article/ from the path and also shows how it was before
# select replace(path , '/article/', ''), path from log where path != '/';
#
# removes /article/ from path and counts it all up and order it descending/ when queried return tuples containt name/count
# select replace(path , '/article/', ''), count(*) as num from log where path != '/' group by path order by num desc;
