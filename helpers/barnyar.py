people = ["ku","ju","paing","pu","poo","aung","phyo"]

n = len(people) # int
for i in range(0,n): # range() gives us only whole numbers
    print(people[i])

print("---------------------")

for p in people: # give each items in a list
    print(p)

def sumNums(x,y):
    return x + y

result = sumNums(5,6) # use ',' in calling functions with parameters
print(result)

range(0,5,6) # built in function, so we must use ','

x = people[:5] # not a funtion, so we use ':'

# more built-in funtions
print(x)
int('3')
str(6)