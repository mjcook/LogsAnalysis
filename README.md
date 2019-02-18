# Project Title

Log Analysis from a News Database

In Python, psycopg2 is used to query a PostgreSQL database for a fictional news website.
The news database contains articles, authors, and logs which the psycopg2 queries.
Using Python3 to query the database, the following three results are generated:

1. Top Three Articles with Most Views
2. Most Popular Authors List
3. Days More Than 1% of Requests Lead To Errors

## Getting Started

What you need to do before running the python code LogAnalysis.py pulling from the news database

### Prerequisites

What things you need to install to run the LogAnalysis.py

- A unix-style terminal such as Git Bash
    - http://www.git-scm.com

- Linux-based virtual machine (VM) this will give the postgreSQL database and support software
    - https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
    - https://www.vagrantup.com/downloads.html

- Vagrant File will provide the virtual machine in order to run the generate the news database and run the python script
    -  https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile

- Newsdata.zip will provide the newsdata.sql file in order to generate the news database
    - https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

- Python 3 to run the code
    - https://www.python.org/downloads/


### Installing

Download the python library to connect to the news database

1) Open a terminal such as git bash
2) Run the following command: pip install psycopg2
3) Navigate to the directory where the Vagrant File has been installed to
4) Run the following command: vagrant up
5) Once done, run the folloiwng comand: vagrant ssh
6) Change directory to the /vagrant folder
7) Extract the newsdata.sql from the Newsdata.zip folder
8) Move the newsdata.sql file to the /vagrant folder in your terminal window
9) Move the LogsAnalysis.py file to the /vagrant folder in your terminal window
10) Run the following command in your terminal window: ls
11) Make sure the output displays that the newsdata.sql file is there along with the LogsAnalysis.py file
12) Execute the following command in order to generate the news database: psql -d news -f newsdata.sql

## Running the test

Inside of the terminal in the vagrant subdirectory, execute the following command: python LogsAnalysis.py (or python3 LogsAnalysis.py)

### Break down into test

The following output should be generated

```
Top Three Articles with Most Views
Article Title: Candidate is jerk, alleges rival Number of Views: 338647
Article Title: Bears love berries, alleges bear Number of Views: 253801
Article Title: Bad things gone, say good people Number of Views: 170098

Most Popular Authors List
Author Name: Ursula La Multa Number of Views: 507594
Author Name: Rudolf von Treppenwitz Number of Views: 423457
Author Name: Anonymous Contributor Number of Views: 170098
Author Name: Markoff Chaney Number of Views: 84557

Days More Than 1% of Requests Lead To Errors
Day: 2016-07-17 Percent Error Requests: 2.26%
```

This output shows the output from the three SQL queries

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Versioning

Version 1.0

## Authors

- **Mitchell Cook**
