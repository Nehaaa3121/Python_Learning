#isalnum- return true if all characters in the string are alphanumeric
#isalpha- returns true if all characters in the tsring are in the alphabet
#isdecimal - returns true if all characters in the string are decimals
# isdigit - returns true of all characters in the string are decimal
#isnumeric - returns true if all characters in the string are digits
#islower - converts a string into lower case
#isupper - returns true if all characterns in the string are numeric
#isspace - returns true if all characters in the strings are whitespace
#istitle - returns true if the string follows the rules of a title

a = "hello23"
print(a,a.isalnum())

b= "hello123"
print(b,b.isalpha())

c = "23"
print(c,c.isdecimal())

d= "Hello"
print(d,d.isdigit())

v = "Neha Choudhary"
print(v,v.islower())

N = "NEHA CHOUDHARY"
print(N,N.isupper())

x= "123445"
print(x,x.isnumeric())

m = " "
print(m,m.isspace())

q= "Hi My Name Is Neha Choudhary"
print(q,q.istitle())

