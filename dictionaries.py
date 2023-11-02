#1.
student={
    "name":"alice",
    "age":20,
    "grade":"A",
    "city":"New York"
}
del student["grade"]
print(student)
#for value in student.value[]:
    #print(f"{value}")

#2.
squares ={ num : num**2 for num in range(1,6)}
print(squares)

square ={ num : num**3 for num in range(1,6)}
print(square)

#3.
dict={0:10,1:20}
dict[2]=30
print(dict)

#4
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#5
d={'x':10,'y':20,'z':30}
for key,value in d.items():
    print(f"key: {key},value:{value}")

#6
n=int(input("enter a number:"))
sample={n:n*n for n in range(1,n+1)}
print(sample)