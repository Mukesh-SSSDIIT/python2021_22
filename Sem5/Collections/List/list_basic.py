cities = ['Junagadh','Mumbai','Bangaluru']

cities[0] = 'Rajkot'

print(type(cities))
print(cities)
print('--------Positive Indexing-----------------')
print(cities[0])
print(cities[1])
print(cities[2])

print('--------Negative Indexing-----------------')
print(cities[-1])
print(cities[-2])
print(cities[-3])

print('--------List members with different datatypes-----------------')
student = ['Romin',20,78.25]
print(student[0])
print(student[1])
print(student[2])

print('--------Range of Index-----------------')
numbers = [10,20,30,40,50,60,70,80,90,100]
print(numbers[5])
print(numbers[0:3])
print(numbers[2:4])
print(numbers[:4])
print(numbers[5:])
print(numbers[-1])
print(numbers[4:-1])
print(numbers[-4:-1])
