#change to ask for values
testint = 4
for i in range(1,6):
    if i < testint:
        print(str(i) + " is less than " + str(testint))
    else:
        print(str(i) + " is NOT less than " + str(testint))

three = 2
two = 2
if three>two:
    print (str(three) + " is bigger than " + str(two))
elif three == two:
    print ("they are equal")
else:
    print (":(")

def hi(name):
    print ('hi ' + name +'!')

hi("yogi")

girls=['alice', 'joan', 'beth']

for name in girls:
    hi(name)
