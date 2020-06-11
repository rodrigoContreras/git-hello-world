from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeData


def delete():
    try:
        criteria = input("Ingrese id empleado : ")
        db.Employees.delete_many({"id": criteria})
        print("Delete Succesfull \n")
        
    except ImportError:
        platform_specific_module = None