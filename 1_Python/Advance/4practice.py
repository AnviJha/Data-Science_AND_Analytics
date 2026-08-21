# write a program to dispay a/b where a  and b are integers .if b=0,display infinite by handling the 'ZeroDivisionError'


try:
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    result=a/b
    print("result :",result)
except ZeroDivisionError:  
    print("Infinite(cannot divide by Zero)")