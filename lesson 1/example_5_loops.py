# for loop
for i in range(5):
    a = i * 2
    print(a)

# i is a var that loops through the array (in this case range funcion)
print("------------")

for i in range(8):
    if i % 3 == 0:
        continue #continue means go to the next loop
    print(i)

#so if i equals 3 6 etc the loop will continue and skip the print i func
print("------------")

for i in range(8):
    if i % 3 == 0:
        break #break means stop the loop
    print(i)

# While loop

var = 5 # needs to declare a var
while var >= 1:
    var -= 1 #needs to manually loop
    print(var)
