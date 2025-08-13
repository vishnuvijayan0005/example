#sq=lambda x:x**2
#add= lambda x,y:x+y

#def test():
 #   num=10
 #   print(num)

#test()
#num=20
#test()

def test():
    global num
    num=10
   # print(num)

num=20
test()
#print(num)

def outer():
    y=0
    x=10
    def inner():
        nonlocal y
        y=20
        print("x+y : ",x+y)
    inner()
    print("x+y : ",x+y)
outer()
