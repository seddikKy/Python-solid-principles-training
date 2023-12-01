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



class EnterpriseEntity(ABC):
    def __init__(self):
        self.employees = []

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def assign_work(self):
        pass




class ITDepartment(EnterpriseEntity):
    
    def get_name(self):
        return "IT Department"

    def assign_work(self):
        for employee in self.employees:
            print(f"{employee.work()} in {self.get_name()}")


class HRDepartment(EnterpriseEntity):
   
    def get_name(self):
        return "HR Department"

    def assign_work(self):
        for employee in self.employees:
            print(f"{employee.work()} in {self.get_name()}")



class SoftwareProject(EnterpriseEntity):
    def __init__(self):
        self.departments = []

    def get_name(self):
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
