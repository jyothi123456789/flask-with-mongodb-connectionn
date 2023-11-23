import Flask
import pymongo
client = pymongo.MongoClient('localhost:27017')
mydb = client['Employee']
information=mydb.table1

records = [{
        "Emp NO" : 501,
        "Emp Name":"Chandu",
        "Job":"Associate Software Engineer",
        "Hire Date":"03-07-2023",
        "Dept NO":2,
        "Salary" : 15000,

        "Emp NO" : 503,
        "Emp Name":"Marif",
        "Job":"Associate Software Engineer",
        "Hire Date":"03-07-2023",
        "Dept NO":2,
        "Salary" : 15000,

        "Emp NO" : 502,
        "Emp Name":"Loki",
        "Job":"Associate Software Engineer",
        "Hire Date":"19-0-2023",
        "Dept NO":2,
        "Salary" : 15000,

        "Emp NO" : 504,
        "Emp Name":"Sanjay",
        "Job":"Associate Software Engineer",
        "Hire Date":"19-07-2023",
        "Dept NO":2,
        "Salary" : 15000,

        "Emp NO" : 505,
        "Emp Name":"Sandeep",
        "Job":"Associate Software Engineer",
        "Hire Date":"19-06-2023",
        "Dept NO":2,
        "Salary" : 15000
    }]
information.insert_many(records)

class Employees:
    def __init__(self, name):
        self.name = name
        self.relationships = []

class Organization:
    def __init__(self, name):
        self.name = name

