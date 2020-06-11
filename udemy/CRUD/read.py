from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeData


def read():
    try:
        empcol = db.Employees.find()
        print("todos los datos \n")
        for emp in empcol:
            print(emp)
    except ImportError:
        platform_specific_module = None