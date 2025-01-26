 #მომხმარებელმა უნდა შეიყვანოს თავისი ასაკი და სახელი. პროგრამამ უნდა შეამოწმოს, რომ ასაკი 18-ზე მეტია და სახელი იწყება "A"-ზე.

age=int(input("enter your age"))
name=input("enter your name")


print(age>18 and name.startswith("A"))