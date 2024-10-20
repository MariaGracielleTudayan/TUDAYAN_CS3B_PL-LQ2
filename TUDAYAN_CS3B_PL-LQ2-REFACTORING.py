"""
Student Name: Maria Gracielle Tudayan
Course, Year, and Section: BSCS 3B
Quiz No.: Q2- Refactoring
"""

#Store student info in a disctionary
student = {
    "studentName": "Lewis Fonse",
    "studentAddress": "City of Candon, Ilocos Sur",
    "studentFavNum1": 25,     #Decalre the value as 25 as an Integer
    "studentAge": 25 ,    #Declare the value as 25 as an Integer
    "studentAllowance": float(500) #Declare the value as 500 as an float with typecasting  
}

#Store classmate info in a dictionaary
classmate = {
    "classmateName": "Andrea Andres",
    "classmateAddress": "City of Vigan, Ilocos Sur",
    "classmateFavNum1": "18",      #Declare the value as 18 as an string
    "classmateAge": "21",     #Declare the value 21 as an string
    "classmateAllowance": "700"      #Declare the vallue as 700 as an string
}

namelength = [len(student["studentName"]), len(classmate["classmateName"])]     #get the length of the studentName and classmateName

#callable function
def checkAddressAndNames():
    if "Ilocos Sur" in student["studentAddress"] and "Ilocos Sur" in classmate["classmateAddress"]:     #use as a condition if "Ilocos Sur" is in studentAdress AND cllassmateAddress
        print(student["studentName"], "is from", student["studentAddress"])      #output: Lewis Fonsi is from City of Candon, Ilocos Sur
        print(classmate["classmateName"], "is from", classmate["classmateAddress"])      #output: Andrea Andres is from City of Vigan, Ilocos Sur

        if namelength[0] > namelength[1]:
            print(f"{classmate['classmateName']} has a longer name than {student['studentName']} with {namelength[1]} letters over {namelength[0]}")        #output: Andrea Andres has a longer name than Lewis Fonsi with 13 letters over 11 letters
        else:
            print(f"{student['studentName']} has a longer name than {classmate['classmateName']} with {namelength[0]} letters over {namelength[1]}")        #output: Lewis Fonsi has a longer name than Andrea Andres with 11 letters over 12 letters
        
    elif "Ilocos Sur" in student["studentAddress"] and "Ilocos Sur" in classmate["classmateAddress"]:     #use as a condition elif "Ilocos Sur" is in studentAdress AND cllassmateAddress
        sName_Split = student["studentName"].split(" ")        #split the studentName with " " - a space as identifier of the splitter
        cName_Split = classmate["classmateName"].split(" ")      #split the studentName with " " - a space as identifier of the splitter
        print(f"One among {sName_Split[0]} or {cName_Split[0]} lives in Ilocos Sur")      #output "One among Lewis or Andres lives in Ilocos Sur" use the sName_Split and cName_Split and use indexing
    else:
        print("None of the Students live in Ilocos Sur")

checkAddressAndNames()

classmateAgeConverted = int(classmate["classmateAge"])       #convert the age of classmate to an integer
print(f"The added age of {student['studentName']} and {classmate['classmateName']} is {student['studentAge'] + classmateAgeConverted}")        #output: The added age of Lewis Fonse and Andrea Andres is 46

classmateFavnumConverted = int(classmate["classmateFavNum1"])        # #convert the favenum of classmate to an integer
print(f"The subtracted value of favenum of {student['studentName']} and {classmate['classmateName']} is {student['studentFavNum1'] - classmateFavnumConverted}")      #output: The subtracted value of favenum of Lewis Fonse and Andrea Andres is 7

classmateAllowanceConverted1 = float(classmate["classmateAllowance"])     #convert the allowance of classmate to an integer
combinedWeeklyAllowance = student["studentAllowance"] + classmateAllowanceConverted1        #add both allowances of the student and classmate
print(f"The weekly allowance of {student['studentName']} and {classmate['classmateName']} is {combinedWeeklyAllowance:.2f}")        #output: The weekly allowance of Lewis Fonse and Andrea Andres is 1200.00

classList = [student["studentName"], classmate["classmateName"]]        #declare the list of student and classmate name
classList_Ext = [student["studentAddress"], classmate["classmateAddress"]]      #declare the list of student and classmate address

classList.extend(classList_Ext)     #extend the value of the classList with the classlist_Ext

for clist in classList:
    print(clist)     #print out the value of the classList using the for loop

classnumbers = [student["studentFavNum1"], student["studentAge"], student["studentAllowance"]]       #declare a list of all numerical vars of the student
classnumbers.append(classmate["classmateAge"])       #append the classmateAge
classnumbers.append(classmate["classmateFavNum1"])       #append the classmateFvaNum1
classnumbers.append(classmateAllowanceConverted1)       #append the classmateAllowance that was converted in to decimal

classnumbers = [str(item) for item in classnumbers]     #convert all the items to string

classnumbers.sort(reverse=True)     #reverse the sort() of the classNumbers List

for cNum in classnumbers:
    print(cNum)     #print out the value of the classNumbers using the for loop

def quizTwo(studentNameCS):     #function which recieves a parameter studentNameCS
    print(f"Congratulations on Quiz 2 {studentNameCS}")     #output: Congratulations on Quez 2 Lewis Fonse

uName = input("Enter your Username: ")
quizTwo(uName)        #call the function quizTwo() passing a variable value of the username input of CS3B

print("Student of CS3B")        #output: Student of CS3B