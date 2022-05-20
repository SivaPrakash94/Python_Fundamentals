'Goal:  Master basic classes and instances'

class Worker:

    status = 'works for a living'  

class Contractor(Worker):

    serviced_company = 'Cisco'

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f'Contractor {self.name} is a {self.gender} servicing {self.serviced_company}'

class Employee(Worker):

    location = 'San Jose'

    def __init__(self, name, gender, location=None):
        self.name = name
        self.gender = gender
        if location is not None:
            self.location = location

    def __str__(self):
        return f'Employee {self.name} is a {self.gender} working from {self.location}'

if __name__ == '__main__':

    raymond = Contractor('Raymond Hettinger', 'male')  # --> Contractor.initialize(raymond, 'Raymond Hettinger', 'male')
    daniel = Contractor('Daniel Miz', 'male')
    siva = Employee('Siva Prakash', 'male')
    anna = Employee('Anna Sakharova', 'female', 'Ottawa')

    team = [siva, raymond, daniel, anna]
    for person in team:
        print(person)

