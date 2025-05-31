name = input("What is your name, fellow student at West Park High:")
if name == "" or name == " ":
 print("Invalid Input, enter a name.")
else:
 grade = int(input("What grade are you in?:"))
 if grade > 11:
  print(f"Sorry,{name}, you are not eligible for the junior awards, as you are not a junior.")
 elif grade < 11:
  print(f"Sorry,{name}, you are not eligible for the junior awards, as you are not a junior.")
 else:
  print(f"Congrats {name}, you are eligible to recieve a junior award. However, you will need to enter in your GPA")
  gpa = float(input("What is you cummulative high school GPA?:"))
  if gpa >= 3.31:
   print(f"Congrats,{name}, you are invited to the ceremony!")
   participation = input("Will you be present at the awards?:")
   if participation == "no":
     print(f"Since you opted out {name}, you will not be recieving an award")
   elif participation == "NO":
     print(f"Since you opted out {name}, you will not be recieving an award")
   elif participation == "No":
     print(f"Since you opted out {name}, you will not be recieving an award")
   if participation == "yes":
     if gpa > 4.0:
       print(f"CONGRATS, {name}, You Achieved Gold Plus, A Potential Valedictorian!")
     elif gpa > 3.75 and gpa < 4.0:
       print(f"Congrats, {name}, you won a Gold Award!")
     elif gpa > 3.31 and gpa < 3.75:
       print(f"Congrats {name}, you won a Silver Award!")
     else:
       print("invalid response")
   elif participation == "YES":
     if gpa > 4.0:
       print(f"CONGRATS, {name}, You Achieved Gold Plus, A Potential Valedictorian!")
     elif gpa > 3.75 and gpa < 4.0:
       print(f"Congrats, {name}, you won a Gold Award!")
     elif gpa > 3.31 and gpa < 3.75:
       print(f"Congrats {name}, you won a Silver Award!")
     else:
       print("invalid response")
   elif participation == "Yes":
     if gpa > 4.0:
       print(f"CONGRATS, {name}, You Achieved Gold Plus, A Potential Valedictorian!")
     elif gpa > 3.75 and gpa < 4.0:
       print(f"Congrats, {name}, you won a Gold Award!")
     elif gpa > 3.31 and gpa < 3.75:
       print(f"Congrats {name}, you won a Silver Award!")
     else:
       print("invalid response")  
  else:
    print(f"Sorry {name}, since your GPA was not that high, you are not invited to the awards.")