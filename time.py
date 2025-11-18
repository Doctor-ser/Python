class time:
    def __init__(self,hour=0,minute=0,second=0):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
        
    def __add__(self,other):
        tot_sec=(self.__hour + other.__hour)*3600 + \
                (self.__minute + other.__minute)*60 + \
                (self.__second + other.__second)
        hours=tot_sec//3600
        minutes=(tot_sec % 3600) // 60
        seconds=tot_sec % 60
        return time(hours,minutes,seconds)

    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

print("enter first time:")
h1=int(input("hours:"))
m1=int(input("minutes:"))
s1=int(input("seconds:"))

print("enter second time:")
h2=int(input("hours:"))
m2=int(input("minutes:"))
s2=int(input("seconds:"))

t1=time(h1,m1,s1)
t2=time(h2,m2,s2)
t3=t1+t2

print("\n Result")
print("time 1:",end="")
t1.display()
print("time 2:",end="")
t2.display()
print("sum: ",end="")
t3.display()
