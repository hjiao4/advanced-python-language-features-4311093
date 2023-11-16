# Example file for Advanced Python: Language Features by Joe Marini
# Use special methods to compare objects to each other


class Employee():
    def __init__(self, fname, lname, level, years_service):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = years_service

    # TODO: implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        if self.level == other.level:
            return self.seniority == other.seniority
        return self.level == other.level


# define some employees
dept = []
dept.append(Employee("Tim", "Sims", 5, 9))
dept.append(Employee("John", "Doe", 4, 12))
dept.append(Employee("Jane", "Smith", 6, 6))
dept.append(Employee("Rebecca", "Robinson", 5, 13))
dept.append(Employee("Tyler", "Durden", 5, 12))

# TODO: Who's more senior?

# TODO: sort the items
for emp in dept:
    print(emp.lname)

print("+++++")

emps = sorted(dept)
for emp in emps:
    print(emp.lname)
