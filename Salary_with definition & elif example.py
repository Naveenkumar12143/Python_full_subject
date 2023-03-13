__author__ = "Narendra Boyina"
# Small program dedicated to my 1st batch students in MP techno solutions


def Salary(EmpId, Expe, sal, Level, Rating):

    if (Expe == 1 and Level == "c1" and Rating == "superstar"):
        print(EmpId, " Hike is 25%,Salary after increment", ((.25 * sal) + sal))
    elif (Expe == 1 and Level == "c1" and Rating == "star"):
        print(EmpId," Hike is 20%,Salary after increment", ((.20 * sal) + sal))
    elif (Expe == 1 and Level == "c1" and Rating == "pillor"):
        print(EmpId," Hike is 15%,Salary after increment", ((.15 * sal) + sal))
    elif (Expe == 1 and Level == "c1" and Rating == "below expectations"):
        print(EmpId," Hike is 9%,Salary after increment", ((.10 * sal) + sal))
    elif(Expe==1 and Level=="c1" and Rating=="nominal"):
        print(EmpId,'Hike is 3%,salary after increment',((.003*sal)+sal))

    elif (Expe == 2 or 3 and Level == "c2" and Rating == "superstar"):
        print(EmpId," Hike is 18%,Salary after increment", ((.18 * sal) + sal))
    elif (Expe == 2 or 3 and Level == "c2" and Rating == "star"):
        print(EmpId," Hike is 15%,Salary after increment", ((.15 * sal) + sal))
    elif (Expe == 2 or 3 and Level == "c2" and Rating == "pillor"):
        print(" Hike is 10%,Salary after increment", ((.10 * sal) + sal))
    elif (Expe == 2 or 3 and Level == "c2" and Rating == "below expectations"):
        print(" Hike is 8%,Salary after increment", ((.08 * sal) + sal))

    elif (Expe == 4 or 5 or 6 and Level == "c3" and Rating == "superstar"):
        print(" Hike is 15%,Salary after increment", ((.15 * sal) + sal))
    elif (Expe == 4 or 5 or 6 and Level == "c3" and Rating == "star"):
        print("Hike is 12%,Salary after increment", ((.12 * sal) + sal))
    elif (Expe == (4 or 5 or 6) and Level == "c3" and Rating == "pillor"):
        print(" Hike is 8%,Salary after increment", ((.08 * sal) + sal))
    elif (Expe == (4 or 5 or 6) and Level == "c3" and Rating == "below expectations"):
        print(" Hike is 6%,Salary after increment", ((.06 * sal) + sal))

    elif (Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "superstar"):
        print(" Hike is 13%,Salary after increment", ((.13 * sal) + sal))
    elif (Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "star"):
        print(" Hike is 9%,Salary after increment", ((.09 * sal) + sal))
    elif (Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "pillor"):
        print(" Hike is 7%,Salary after increment", ((.07 * sal) + sal))
    elif (Expe == (7 or 8 or 9) and Level == ("c4" or "c5") and Rating == "below expectations"):
        print(" Hike is 5%,Salary after increment", ((.05 * sal) + sal))

    elif (Expe >= 10 and Level == ("c6" or "c7") and Rating == "superstar"):
        print(" Hike is 10%,Salary after increment", ((.10 * sal) + sal))
    elif (Expe >= 10 and Level == ("c6" or "c7") and Rating == "star"):
        print(" Hike is 7%,Salary after increment", ((.07 * sal) + sal))
    elif (Expe >= 10 and Level == ("c6" or "c7") and Rating == "pillor"):
        print(" Hike is 5%,Salary after increment", ((.05 * sal) + sal))
    elif Expe >= 10 and Level == ("c6" or "c7") and Rating == "below expectations":
        print(" Hike is 3%,Salary after increment", ((.03 * sal) + sal))
    else:
        print("given values are not match")

# a = int(input("Enter employee Exp :"))
# b = int(input("Enter employee Salary :"))


# Salary("HM0002162", 2, 25000, "c2", "star")
Salary("HM0002162", 3, 35000, "c2", "pillor")
# Salary("HM0002162", 7, 92000, "c2", "star")

# b = input("Enter employee ID :")
# print(b)