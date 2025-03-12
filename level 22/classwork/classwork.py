# 1) დაპრინტეთ ყველა ლუწი რიცხვი 0 დან 100 მდე

for num in range(0, 101, 2):
    print(num)


# 2) დაპრინტეთ ყველა კენტი რიცხვი 1 დან 100 მდე

for num in range(1, 100, 2):
    print(num)



#3) დაპრინტეთ 1 დან 100 მდე ყველა რიცხვის ჯამი 

summary = 0
for i in range(1, 101):
    summary = summary + i
print(summary)



# 4) დაპრინტეთ 1 დან 100 ის ჩათვლით ყველა ლუწი რიცხვის ჯამი
summary = 0
for i in range(2, 101, 2):
    summary = summary + 2
print(summary)



# 5) დაპრინტეთ 1 დან 100 ის ჩათვლით ყველა კენტი რიცხვის ჯამი

summary = 0
for i in range(1, 101, 2):
    summary = summary + 1
print(summary)
