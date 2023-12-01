from abc import ABC, abstractmethod


# Interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Manager(Workable):
    def work(self):
        return "Manager is managing tasks."


class Developer(Workable):
    def work(self):
        return "Developer is coding."


class Department(ABC):
    @abstractmethod
    def get_department_name(self):
        pass

    @abstractmethod
    def assign_work(self):
        pass


class ITDepartment(Department):
    def __init__(self):
        self.employees = []

    def get_department_name(self):
        return "IT Department"

    def assign_work(self):
        for employee in self.employees:
            print(f"{employee.work()} in {self.get_department_name()}")


class HRDepartment(Department):
    def __init__(self):
        self.employees = []

    def get_department_name(self):
        return "HR Department"

    def assign_work(self):
        for employee in self.employees:
            print(f"{employee.work()} in {self.get_department_name()}")


class Project(ABC):
    @abstractmethod
    def get_project_name(self):
        pass

    @abstractmethod
    def assign_work(self):
        pass


class SoftwareProject(Project):
    def __init__(self):
        self.departments = []

    def get_project_name(self):
        return "Software Project"

    def assign_work(self):
        for department in self.departments:
            department.assign_work()


# Example Usage
it_department = ITDepartment()
hr_department = HRDepartment()

manager = Manager()
developer1 = Developer()
developer2 = Developer()

it_department.employees.append(manager)
it_department.employees.append(developer1)

hr_department.employees.append(developer2)

software_project = SoftwareProject()
software_project.departments.append(it_department)
software_project.departments.append(hr_department)

software_project.assign_work()
