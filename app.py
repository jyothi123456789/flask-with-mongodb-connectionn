from flask import Flask, jsonify, request

app = Flask(__name__)

# Object 1: Organization, College, Community, etc.
class Object1:
    def __init__(self, name):
        self.name = name
        self.relationships = []

# Object 2: Employee, Books, Events, etc.
class Object2:
    def __init__(self, name):
        self.name = name

# RBAC Roles
class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

# Create instances of Object1
organization1 = Object1("Organization 1")
organization2 = Object1("Organization 2")

# Create instances of Object2
employee1 = Object2("Employee 1")
employee2 = Object2("Employee 2")

# Assign relationships
organization1.relationships.append(employee1)
organization2.relationships.append(employee2)

# Create RBAC roles
role1 = Role("Role 1", ["create", "read"])
role2 = Role("Role 2", ["create", "read", "update", "delete"])

# Assign RBAC roles to objects
object1_roles = {organization1: [role1], organization2: [role1]}
object2_roles = {employee1: [role2], employee2: [role2]}

# Flask API routes

# Get information about Object1
@app.route('/object1/<name>', methods=['GET'])
def get_object1(name):
    obj = next((obj for obj in [organization1, organization2] if obj.name == name), None)
    if obj:
        return jsonify({"name": obj.name, "relationships": [r.name for r in obj.relationships]})
    else:
        return jsonify({"error": "Object1 not found"}), 404

# Get information about Object2
@app.route('/object2/<name>', methods=['GET'])
def get_object2(name):
    obj = next((obj for obj in [employee1, employee2] if obj.name == name), None)
    if obj:
        return jsonify({"name": obj.name})
    else:
        return jsonify({"error": "Object2 not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
