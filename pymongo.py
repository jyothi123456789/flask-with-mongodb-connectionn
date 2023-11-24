import Flask_MongoDB
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

client = PyMongo.MongoClient('mongodb+srv://naveenchandgadde:ChanduG97@flask.0zcjxbr.mongodb.net/')
mydb = client['Employee']
information = mydb.table1

# Define Employee class
class Employee:
    def __init__(self, emp_no, emp_name, job_role, hire_date, dept_no, salary):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.job_role = job_role
        self.hire_date = hire_date
        self.dept_no = dept_no
        self.salary = salary

# Define resource for CRUD operations
class EmployeeResource(Resource):
    def get(self, emp_no):
        # Retrieve employee information by employee number
        emp_data = information.find_one({"Emp NO": emp_no})
        if emp_data:
            return jsonify(emp_data)
        else:
            return jsonify({"message": "Employee not found"}), 404

    def post(self):
        # Create a new employee record
        data = request.get_json()
        new_employee = Employee(
            data["Emp NO"],
            data["Emp Name"],
            data["Job"],
            data["Hire Date"],
            data["Dept NO"],
            data["Salary"]
        )
        records = [{
            "Emp NO": new_employee.emp_no,
            "Emp Name": new_employee.emp_name,
            "Job": new_employee.job_role,
            "Hire Date": new_employee.hire_date,
            "Dept NO": new_employee.dept_no,
            "Salary": new_employee.salary
        }]
        information.insert_many(records)
        return jsonify({"message": "Employee added successfully"})

#     def put(self, emp_no):
#         # Update employee information
#         data = request.get_json()
#         information.update_one({"Emp NO": emp_no}, {"$set": data})
#         return jsonify({"message": "Employee updated successfully"})

#     def delete(self, emp_no):
#         # Delete employee record
#         information.delete_one({"Emp NO": emp_no})
#         return jsonify({"message": "Employee deleted successfully"})

# # Add resource to API with endpoint
# api.add_resource(EmployeeResource, '/employee/<int:emp_no>')

# if __name__ == '__main__':
#     app.run(debug=True)
