def grading(score):
    try:
        if 1.0 <= score <= 0.0:
            if score >= 0.9:
                grade = "A"
            elif score >= 0.8:
                grade = "B"
            elif score >= 0.7:
                grade = "C"
            elif score >= 0.6:
                grade = "D"
            else:
                grade = "F"
            return(grade)
        else:
            return("Bad score")
    except:
        return("Bad score")

print(grading(10))