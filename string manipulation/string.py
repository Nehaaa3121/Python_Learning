#strings are the combination of number,symbols,and letters enclosed inside quotations

a = "neha choudhary"
print(type(a))
print(a)
#string methods
# 1. length
#2.count
#3. upper
#4. lower
#5. index
#6.capitalize
#7. casefold
#8 .find
#9. format
#10. center

name = "Neha_Choudhary"
print(len(name))
print(name.count("N"))

print(name.upper())
print(name.lower())
print(a.index("y"))
print(name.capitalize())
print(name.casefold())
print(name.find("h"))
print(name.center(20,"#"))

v= "my name is {}"
print(v.format(name))