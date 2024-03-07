#Samantha Patin and Therese Burns
x=input("Enter word\n")

def function(x):
    total=0
    for y in x:
        if y=="o":
            total=total+1
    print(total)

function(x)

print("abc"[0])
print("abc"[2])
print("waffles"[1])

dinner= "falafels"
print(dinner[4])

print(["a", "b", "c"][2])
print([1,2,3,4][0])

colors=["red", "green", "blue"]
print(colors[1])

countdown=[3,2,1, "action!"]
print(countdown[3])

print("frog"[-1])
print("fish"[-2])
print("fish"[2])
