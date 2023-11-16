value = input("wprowadz walute zl or eu: ")
num1 = float(input("podaj kwote jaka chcesz zmienić: "))
value_course = 4.5

if  value == "zl":
   result= num1  / value_course
   print(f"Posiadasz tyle {num1} zlotych a to tyle {result} euro ")
else:
    result = num1*value_course
    print(f"Posiadasz tyle {num1} euro a to tyle {result} złotych ")

print("test2")




