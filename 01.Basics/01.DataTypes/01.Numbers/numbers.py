x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

# we can not convert complex to float or complex to int
d = int(z)
d = float(z)


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))