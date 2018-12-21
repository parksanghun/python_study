a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)

a = [38, 21, 53, 62, 19]
biggest = a[0]
for i in a:
    if i > biggest:
        biggest = i
print(biggest)


a = [i for i in range(0, 11)]
b = list(i for i in range(0, 11))

a = ['alpha', 'bravo', 'charlie', 'delta']

