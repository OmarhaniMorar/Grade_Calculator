#Operations detection system
university_number = str(input("Enter University number: "))
#Input number of courses and validate
num_of_courses = 0
while num_of_courses < 3:
    num_of_courses = int(input("Enter number of courses (At least 3 subjects) : "))

mark_results = 0
count = num_of_courses

for i in range(num_of_courses):
    course_mark = int(input(f"Enter Course {i+1} mark: "))
    if course_mark > 100 or course_mark < 0:
        print("Invalid mark")
        continue
    mark_results += course_mark
    num_of_courses -= 1

average = mark_results / count

def university_status(avg):
    if 0 <= avg < 50:
        return "Failed"
    elif 50 <= avg < 70:
        return "good"
    elif 70 <= avg < 85:
        return "Very Good"
    elif 85 <= avg <= 100:
        return "Excellent"
    else:
        return "Invalid mark"
    
print(f"University number: {university_number}")
print(f"Average mark: {average}")
print(f"University status: {university_status(average)}")

