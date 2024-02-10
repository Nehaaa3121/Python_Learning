a= "Neha Choudhary"
print(a.endswith("y"))

print(a.startswith("N"))

print(a.swapcase())

b = "    Neha Choudhary ******"
print(b)
print(b.strip("*, "))

c= "00Nhsjsiisao#bjanoa#jbashsai#dad#"
print(c.split("#"))

d= "My Name is"
e=d.ljust(20, "#")
print(e, "Neha Choudhary")
e=d.rjust(20,"#")
print(e,"Neha Choudhary")

f ="My name is Neha Choudhary"
print(f.replace("My name is", "I am"))

print(f.rindex("Neha"))
print(f.rfind("My"))