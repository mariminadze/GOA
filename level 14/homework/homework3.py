# დაწერე პროგრამა, რომელიც ამოწმებს, რიცხვი ლუწია ან 3-ის გამყოფი.




def check_number(num):
     if num % 2 == 0 or num % 3 == 0:
         return "რიცხვი ლუწია ან 3-ის გამყოფი."
         else: return "რიცხვი არც ლუწია და არც 3-ის გამყოფი."
 
 
 
 
 # შესამოწმებელი რიცხვი
 
  number = int(input("შეიყვანეთ რიცხვი: "))
result = check_number(number) 
print(result)