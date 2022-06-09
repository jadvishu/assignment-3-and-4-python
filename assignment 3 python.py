#Answer of question 1
a=int(input("Enter a number to convert it into its binary equivalent:"))
print("binary form=",bin(a)[2:])

#answer of question 2
e=eval(input("Enter your expression to evaluate:"))
print("Answer of the expression=",e)

#Answer of quest 3
#(a)
a=3
b=4
c=5
sum1=(a+b)*(c)
print(sum1)

#(b) x=(n*(n-1))/2

#(c) 4*math.pi*r*r
#(d) math.sqrt(r*(math.cos(a)**2)+r*(math.sin(b)**2))
#(e) (y2-y1)/(x2-x1)

#Answer of question 4
#     a) range(5)                      -> [0, 1, 2, 3, 4]
#     b) range(3,5)                    -> [3, 4]
#     c) range(4,13,3)                 -> [4, 7, 10]
#     d) range(15,5,-2)                -> [15, 13, 11, 9, 7]
#     e) range(5,3)                    -> []

#Answer of question 5
a=int(input("Enter the number of hydrogen atoms:"))
b=int(input("Enter the number of carbon atoms:"))
c=int(input("Enter the number of oxygen atoms:"))
m1= (a*1.00794)
m2=(b*12.0107)
m3=(c*15.9994)
sum1= m1+m2+m3
print("Total molecular weight of carbohydrate=",sum1) 


