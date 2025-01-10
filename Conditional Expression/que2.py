marks1 = int(input("Enter English marks: "))
marks2=  int(input("Enter Marathi marks: "))
marks3 = int(input("Enter Hindi marks: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("PASS", total_percentage)

else:
    print("FAIL",total_percentage)
