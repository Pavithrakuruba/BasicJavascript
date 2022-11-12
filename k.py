# a=[200,300,400,500,600]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     j=0
#     d=" "
#     while j<len(c):
#         if c[j]!=str(0):
#             b.append(c[j])
#         j+=1
#     i+=1
# print(b)


# i=1
# while i<=10:
#     if i==8:
#         continue
#     if i==7:
#         pass
#     if i==9:
#         break
#     i+=1
# print(i)

# a=["m@y nam2e is Pavi$thra i@m a2n Indi@a"]
# o/p[my name is pavithra im an Indian]
# b=[]
# str=''
# for i in a:
#     for j in i:
#         # print(j)
#         if (j>='A' and j<='Z') or (j>='a' and j<='z'):
#             str+=j
#         elif j==' ':
#             str+=' '
#         # else:
#         #     pass
# b.append(str)
# print(b)



# a=2
# print(a)

# print("hello")
# def fun(a,b):
#     a=30
#     print(a+b)
# def fun2(a):
#     return a+20
# a=10
# c=20
# fun(a,c+fun2(c))
# print(a)
# print("bye")


# def some_thing(number1, number2):
#     first_value = number1 + 8
#     second_value = number2 - 5
#     return first_value

# some_thing(13, 10)


def fun1(a):
       if(a==1):
           return a
       return a*fun1(a-1) #5*fun1(4)
n=int(input()) #5
print(fun1(n)) 