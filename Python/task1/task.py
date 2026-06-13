sname = str(input("Enter Stydent Name :"))
sm_mark = int(input("Enter Stydent Math mark :"))
ss_mark = int(input("Enter Stydent Science mark :"))
se_mark = int(input("Enter Stydent English mark :"))
print("Student Name:",sname)
print("Total Marks:",sm_mark+ss_mark+se_mark)
print("per",(sm_mark+ss_mark+se_mark)/3)
if (sm_mark+ss_mark+se_mark)/3 >= 35:
    print("Result: Pass")
else:
    print("Fail")