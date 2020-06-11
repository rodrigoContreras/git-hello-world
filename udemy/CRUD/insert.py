from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeData


def insert():
    try:
        employeid = input("id empleado : ")
        employename = input("Nombe empleado : ")
        employeage = input("Edad empleado : ")
        employecountry = input("Pais empleado : ")
        db.Employees.insert_one(
            {
                "id" : employeid,
                "name" : employename,
                "age" : employeage,
                "country" : employecountry
            }
        )
        print("Insert Data Succesfully")
    except ImportError:
        platform_specific_module = None





