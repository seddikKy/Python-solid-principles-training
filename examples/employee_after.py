from abc import ABC, abstractmethod


class EmployeeInterface(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass
    
    def to_dict(self):
        return ConvertEmployee.to_dict(self)


class EmployeeRoleInterface(EmployeeInterface):
    @abstractmethod
    def role(self):
        pass


class ManagerEmployee(EmployeeRoleInterface):
    def calculate_bonus(self):
        return self.salary * 0.2
    
    def role(self):
        return 'Manager'


class DeveloperEmployee(EmployeeRoleInterface):
    def calculate_bonus(self):
        return self.salary * 0.1
    
    def role(self):
        return 'Developer'


class InternEmployee(EmployeeRoleInterface):
    def calculate_bonus(self):
        return 0
    
    def role(self):
        return 'Intern'
    

class ConvertEmployee:
    @staticmethod
    def to_dict(employee:EmployeeInterface):
        return {
            "name": employee.name,
            "role": employee.role(),
            "salary": employee.salary,
            "bonus": employee.calculate_bonus()
        }


class ProjectInterface(ABC):
    def __init__(self, name, budget, team):
        self.name = name
        self.budget = budget
        self.team = team
    
    @abstractmethod
    def calculate_total(self):
        pass

    def to_dict(self):
        return JsonConverter.to_dict(self)


class WithinBudgetInterface(ProjectInterface):
    @abstractmethod
    def is_within(self):
        pass


class TeamCostProject(WithinBudgetInterface):
    def calculate_total(self):
        total_cost = 0
        for member in self.team:
            total_cost += member.salary
        return total_cost
    
    def is_within(self):
        return self.calculate_total() <= self.budget


class JsonConverter:
    @staticmethod
    def to_dict(project: TeamCostProject):
        return {
            "name": project.name,
            "budget": project.budget,
            "team": [member.to_dict() for member in project.team],
            "within_budget": project.is_within()
        }

    

# Exemple d'utilisation
manager = ManagerEmployee("Alice", 50000)
developer = DeveloperEmployee("Bob", 40000)
intern = InternEmployee("Charlie", 20000)

project_team = [manager, developer, intern]

software_project = TeamCostProject("Software Project", 100000, project_team)

print(software_project.to_dict())