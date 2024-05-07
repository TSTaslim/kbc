
# #name varification
# while True:
#     name= input("Enter Your Name:")
#     if name.isalpha():
#         print(name,", you are entering Kaun Banega carore-Pati")
#         break
#     else:
#         print("Name can't have DIgits")
# #age verification
# while True:
#     age = int(input("Enter age:"))
#     if age.isdigit():
#         if (age>"15"):
#             print(f"{name} ,you are is alligible to play kbc\n loading questions... ")
#             break
#         else:
#             print("minor")
#             break
#     else:
#         print("fuck u")

questions= [
    ["Question 1: What language is used to make Mine-Craft", "Python","java","C#","PhP",2],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1],
    ["Question 1: What is the biggest C library", "Microsoft","Apple","Nvidia","HP",1]

]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 250000, 500000, 1000000]

money = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"1.{question[1]}     2.{question[2]}")
    print(f"3.{question[3]}     4.{question[4]}")
    print("To quit Press 0...")
    reply = int(input("Enter your answer (1-4)" ))
    if reply == 0:
        money = levels[i-1]
        break
    elif reply == question[-1]:
        print(f"Answer is correct! Your balanve is: {levels[i]}")
        if i == 4:
           money = 10000
           print(f"You Have won {money} Rs in kaun banega krorep-Pati!!!")
        elif i == 9:
            money == 320000
            print(f"You Have won {money} Rs in kaun banega krorep-Pati!!!")
        elif i == 14:
            money = 1000000
            print(f"You Have won {money} Rs in kaun banega krorep-Pati!!!")
           
    else:
        print("Wrong Answer!")
        break