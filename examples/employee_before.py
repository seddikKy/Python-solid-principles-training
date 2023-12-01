class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def calculate_bonus(self):
        if self.role == "Manager":
            return self.salary * 0.2
        elif self.role == "Developer":
            return self.salary * 0.1
        elif self.role == "Intern":
            return 0
        else:
            raise ValueError("Invalid role")

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "salary": self.salary,
            "bonus": self.calculate_bonus()
        }


class Project:
    def __init__(self, name, budget, team):
        self.name = name
        self.budget = budget
        self.team = team

    def calculate_team_cost(self):
        total_cost = 0
        for member in self.team:
            total_cost += member.salary
        return total_cost

    def is_within_budget(self):
        return self.calculate_team_cost() <= self.budget

    def to_dict(self):
        return {
            "name": self.name,
            "budget": self.budget,
            "team": [member.to_dict() for member in self.team],
            "within_budget": self.is_within_budget()
        }


# Exemple d'utilisation
manager = Employee("Alice", "Manager", 50000)
developer = Employee("Bob", "Developer", 40000)
intern = Employee("Charlie", "Intern", 20000)

project_team = [manager, developer, intern]

software_project = Project("Software Project", 100000, project_team)

print(software_project.to_dict())
