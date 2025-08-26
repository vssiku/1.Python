class multipleFunctions():
    def Subfields():
        my_list = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        return(my_list)
    def oddEven(n):
        if n%2==1:
            result='Odd Number'
        else:
            result='Even Number'
        return result      
    def check_eligibility(gender_a1,age_a2):
        if gender_a1.lower()=='male' and age_a2 >=21:
            res='ELIGIBLE'
        elif gender_a1.lower()=='male' and age_a2 <21:
            res='NOT ELIGIBLE'
        elif gender_a1.lower()=='female' and age_a2 >=18:
            res='ELIGIBLE'
        elif gender_a1.lower()=='female' and age_a2 <18:
            res='NOT ELIGIBLE'
        else: res='WRONG INPUT'
        return res
    def func_percentage(s1,s2,s3,s4,s5):
        sum=s1+s2+s3+s4+s5
        per=float(sum/5)
        return per
    def area_tri(h,b):
        return((h*b)/2)
    def peri_tri(h1,h2,b):
        return(h1+h2+b)   
    def bmi():
        bmi=int(input("Enter the BMI Index:"))
        if bmi < 18.5:
            print("UnderWeight")
        elif bmi <=24.9:
            print("Healthy Weight")
        elif bmi <=29.9:
            print("Overweight")
        elif bmi <=34.9:
            print("Class 1 obesity")
        elif bmi <=39.9:
            print("Class 2 obesity")
        else:
            print("Class 3 obesity")