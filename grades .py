#tudents grades
students_name = input("enter the name of the student: ")
marks = int(input("enter the marks of the studdent: "))
if not 0 <= marks <= 100 :
    print("invalid marks! enter between 0 to 100 : ")
elif marks >= 70:
    grade = "A"
elif marks >= 60 :
    grade = "B" 
elif marks >= 50 :
    grade = "C"
elif marks >= 40 :
    grade = "D" 
else:
    grade = "fail"

if 0 <= marks <= 100 :
    print("\n----STUDENT RESULTS----")
    print(f"Name :{students_name}")
print(f"Marks :{marks}")
print(f"Grade :{grade}")

if marks >= 70 :
    print("wooow!good boy")

















