class Employee():
    def __init__(self, firstName, lastName, employeeID):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
    
    def Greeting(self):
        print(f"Hi, my name is {self.firstName} {self.lastName}")
    def getEmployeeID(self):
        return self.employeeID

class Manager(Employee):
    def __init__(self, firstName, lastName, employeeID, managedDepartment):
        super().__init__(firstName, lastName, employeeID)
        self.managedDepartment = managedDepartment
    
    def assignDepartment(self,departmentName):
        self.managedDepartment = departmentName
    def getDepartment(self):
        return self.managedDepartment

class Developer(Employee):
    def __init__(self, firstName, lastName, employeeID, assignedProject):
        super().__init__(firstName, lastName, employeeID)
        self.assignedProject = assignedProject
    
    def reAssignToNextProject(self,projectName):
        self.assignedProject = projectName
    def getCurrentProjectAssignment(self):
        return self.assignedProject

class Intern(Employee):
    def __init__(self, firstName, lastName, employeeID):
        super().__init__(firstName, lastName, employeeID)
        self.assistingProjects = []

    def assistOnProject(self,Project):
        self.assistingProjects.append(Project)
    def getAssistingProjects(self):
        return self.assistingProjects
    def removeFromProject(self,Project):
        self.assistingProjects.remove(Project)

def main():
    # Developer Object
    dev = Developer("Andrew", "Chen", 112233, "Calorie counter App")
    dev.Greeting()
    print(f"My Current Project: {dev.getCurrentProjectAssignment()}")
    dev.reAssignToNextProject("To Do List App")
    print(f"My Current Project: {dev.getCurrentProjectAssignment()}")

    # Manager Object
    manager = Manager("John", "Doe", 112243, "Product Development")
    manager.Greeting()
    print(f"Current Dept: {manager.getDepartment()}")
    manager.assignDepartment("Product Design")
    print(f"Reassigned to: {manager.getDepartment()}")

    # Intern Object
    newIntern = Intern("Sally", "Jean", 142533)
    newIntern.Greeting()
    newIntern.assistOnProject('Calorie counter App')
    newIntern.assistOnProject('To Do List App')
    print(newIntern.getAssistingProjects())
    newIntern.removeFromProject('To Do List App')
    print(newIntern.getAssistingProjects())

main()