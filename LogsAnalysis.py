#!/usr/bin/env python3
import psycopg2

dataBase = psycopg2.connect("dbname=news")
cursor = dataBase.cursor()


def print_top_articles():
    query = """SELECT title, COUNT(path) AS views FROM log JOIN articles ON
            '/article/' || articles.slug = log.path WHERE log.status = '200 OK'
            GROUP BY title ORDER BY views DESC LIMIT 3;"""
    cursor.execute(query)
    articleViews = cursor.fetchall()

    print("Top Three Articles with Most Views")
    for article in articleViews:
        print ("Article Title: " + article[0] +
               " Number of Views: " + str(int(article[1])))
    print("")


def print_top_euthors():
    query = """SELECT authors.name, views FROM authors, (SELECT author,
               COUNT(path) AS views FROM log, articles WHERE '/article/' ||
               articles.slug = log.path AND log.status = '200 OK' GROUP BY
               author ORDER BY views DESC) AS subq WHERE authors.id =
               subq.author ORDER BY views DESC;"""
    cursor.execute(query)
    authorViews = cursor.fetchall()

    print("Most Popular Authors List")
    for author in authorViews:
        print ("Author Name: " + author[0] +
               " Number of Views: " + str(int(author[1])))
    print("")


def print_errors_over_one_percent():
    query = """SELECT subq1.day, TRUNC(((CAST(errors AS DECIMAL) /
    cast(queries AS DECIMAL)) * 100), 2) AS percenterrors FROM (SELECT
    log.time::DATE AS day, COUNT(*) AS queries FROM log GROUP BY day
    ORDER BY queries DESC) AS subq1 LEFT JOIN (SELECT log.time::DATE
        AS day, COUNT(*) AS errors FROM log WHERE status = '404 NOT FOUND'
        GROUP BY day ORDER BY errors DESC) AS subq2 ON subq1.day = subq2.day
        WHERE ((CAST(errors AS DECIMAL) / CAST(queries AS DECIMAL)) * 100)
        > 1 ORDER BY percenterrors DESC;"""
    cursor.execute(query)
    errorRequests = cursor.fetchall()

    print("Days More Than 1% of Requests Lead To Errors")
    for errorRequest in errorRequests:
        print ("Day: " + str(errorRequest[0]) +
               " Percent Error Requests: " + str(float(errorRequest[1])) + "%")
    print("")


if (__name__ == '__main__'):
    print_top_articles()
    print_top_euthors()
    print_errors_over_one_percent()
    dataBase.close()
