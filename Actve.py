
def check_exam_eligibility(marks, attendance_percentage):
    
    minimum_marks = 40
    minimum_attendance = 75
    
    if marks >= minimum_marks and attendance_percentage >= minimum_attendance:
        return "Eligible for the exam"
    elif marks < minimum_marks and attendance_percentage < minimum_attendance:
        return "Not eligible: Marks and attendance are both below the required level"
    elif marks < minimum_marks:
        return "Not eligible: Marks below the required level"
    else:
        return "Not eligible: Attendance below the required level"


marks_obtained = int(input("Enter the student's marks: "))
attendance = float(input("Enter the student's attendance percentage: "))

eligibility_status = check_exam_eligibility(marks_obtained, attendance)
print(eligibility_status)
