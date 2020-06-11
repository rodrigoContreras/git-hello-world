from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeData


def update():
    try:
        criteria = input("id empleado : ")
        name = input("Nombe empleado : ")
        age = input("Edad empleado : ")
        country = input("Pais empleado : ")
        db.Employees.update_one(
            {"id":criteria},
            {
                "$set":{
                "name" : name,
                "age" : age,
                "country" : country
                }

            }
        )
        print("Records Update Succesfully")
    except ImportError:
        platform_specific_module = None