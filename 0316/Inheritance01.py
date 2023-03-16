""" 예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고 부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가? 
이용할 수 없다면 그 이유는? 
이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?
 """
 
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))
        
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
        
    def set_name(self, name):
        self.__name = name

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)
        
t = Teacher(35, 'Kim', 'highschool')
t.introMe()
t.set_name('Lee')
t.introMe()
t.showSchool()
