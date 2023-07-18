from departments import Department


class Hospital:

    def __init__(self, name, address, phone, website):
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website
        self.department = []

    def add_department(self, name_of_department):
        self.department.append(name_of_department)