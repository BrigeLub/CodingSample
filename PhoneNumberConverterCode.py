#Purpose: Convert Phone Number
#Author: Brigitte Lubker
#Date:4/21/22

#code to decipher what each letter converts to in digits
code = {"A" : 2, "B" : 2, "C" : 2, "D" : 3, "E" : 3, "F" : 3, "G" : 4, "H" : 4, "I" : 4, "J" : 5, "K" : 5,
"L" : 5, "M" : 6, "N" : 6, "O" : 6, "P" : 7, "Q" : 7, "R" : 7, "S" : 7, "T" : 8, "U" : 8, "V" : 8, "W" : 9, 
"X" : 9, "Y" : 9, "Z" : 9, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "0" : 0,"-" : "-"}

#title
print("Phone Number Translator")

#takes user phone number
number = input("Enter a phone number in the format XXX-XXX-XXXX: ")

#break up each character of number
n = list(number)

#rebuild the converted number as a new string
newNumber = ""
newNumber = str((code[n[0]],code[n[1]],code[n[2]],code[n[3]],
             code[n[4]],code[n[5]],code[n[6]],code[n[7]]
             ,code[n[8]],code[n[9]],code[n[10]],code[n[11]]))

#remove unnecessary characters left over from list formating
newNumber = newNumber.replace(",", "")
newNumber = newNumber.replace("'", "")
newNumber = newNumber.replace(")", "")
newNumber = newNumber.replace("(", "")
newNumber = newNumber.replace(" ", "")

#print out conversion
print("Dial:",newNumber)