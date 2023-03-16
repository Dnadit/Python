""" 문제: 학생 정보를 관리하는 프로그램을 만드세요.
학생(Student) 클래스
    인스턴스 변수: 이름(name), 학번(student_id), 학년(year), 전공(major), 평균 성적(avg_score)
    메서드: get_info() - 학생의 정보를 문자열로 반환

학생들을 관리하는 클래스(StudentManager)
    인스턴스 변수: 학생들(student_list)
    메서드:
    add_student(student): 학생을 리스트에 추가하는 메서드
    remove_student(student_id): 학번을 이용해 학생을 리스트에서 제거하는 메서드
    find_student(student_id): 학번을 이용해 학생을 찾는 메서드
    show_all_students(): 모든 학생의 정보를 출력하는 메서드
"""
 
class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score
    
    def get_info(self):
        return f"이름:{self.name}, 학번:{self.student_id}, 학년:{self.year}, 전공:{self.major}, 평균 성적:{self.avg_score},"
    
class StudentManager:
    def __init__(self):        
        self.student_list = []
        
    def add_student(self, student):
        self.student_list.append(student)
        
    def remove_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                return
        print(f"학번이 {student_id}인 학생은 없습니다.")
                
    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                print(student.get_info() + "학생은 있습니다.")
                return                      
        print(f"학번이 {student_id}인 학생은 없습니다.")
                
    
    def show_all_students(self):
        for student in self.student_list:
            print(student.get_info())

student1 = Student('홍길동', '20230001', 2, '컴퓨터공학', 90.5)
student2 = Student('김철수', '20230002', 2, '컴퓨터공학', 80.5)
student3 = Student('이영희', '20230003', 2, '컴퓨터공학', 70.5)

student_manager = StudentManager()
student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)

student_manager.remove_student('20230001')

student_manager.find_student('20230003')

student_manager.show_all_students()