class student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age = age
        self.grade = grade

    def moy(self):
        return sum(self.grade)/len(self.grade)

    def resul(self):
        if self.moy() > 10:
            return "Pass"
        else: 
            return "Failed"


student1=student("insaf", 24, [2, 5, 14])
print(student1.name)
print(student1.resul())