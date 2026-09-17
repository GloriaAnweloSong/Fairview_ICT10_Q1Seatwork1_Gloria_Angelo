from pyscript import document, display

#part 1

Name = "Angelo" #string
Age = 14 #integer
Height1 = 162 #integer
Countries_I_Want_Visit = ["England", "Italy", "Taiwan"] #list 
student_type = False #boolean
dictionary = {"color" : "Pink", "car_brand" : "Toyota", "shoe_size" : 9, "best_friend": "Ernest"} #dictionary
favorite_fruits = {"mango", "pineapple", "watermelon", "dragonfruit", "apple"} #set
week = ("sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday") #tuple

display((Name), target="div1")
display((Age), target="div1")
display((Height1), target="div1")
display((Countries_I_Want_Visit), target="div1")
display((student_type), target="div1")
display((dictionary), target="div1")
display((favorite_fruits), target="div1")
display((week), target="div1")

#part 2

def add_num(e): #pyscript event to trigger functions
    document.getElementById("output").innerHTML = "" # to clear our last result

    num1 = float(document.getElementById("inputnum1").value)
    num2 = float(document.getElementById("inputnum2").value)
    result = num1 + num2 #adds both numbers the users input in both boxes
    display(result, target="output")