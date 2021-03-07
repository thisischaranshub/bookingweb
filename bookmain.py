import math
x=int(input("Enter number of rows "))
y=int(input("Enter number of colms "))
booked_seats=[]
data=[]
val=0
total_price=0
full_hall_price=0
while(val!=5):
    print("\n1.show the seats\n2.buy a ticket\n3.statistics\n4.show booked ticket\n5.exit")
    val=int(input())
    no_of_seats=x*y
    if(no_of_seats<=60):
        t_price=10
        full_hall_price=(x*y)*t_price
    else:
        full_hall_price=(int(x/2)*y*10)+(x-int(x/2)*y*8)
        t_price=0;
    print('\n')
    if(val==1):
        print(" ",end=" ")
        for k in range(1,y+1):
            print(k,end=" ")
        print("\n")
        for i in range(1,x+1):
            print(i,end=" ")
            for j in range(1,y+1):
                if([i,j] not in booked_seats):
                    print('s',end=" ")
                else:
                    print('b',end=" ")
            print("\n")
    if(val==2):
        seat_row=int(input("Enter row"))
        seat_col=int(input("Enter col"))
        c=[seat_row,seat_col]
        if(c not in booked_seats and seat_col<=y and seat_row<=x):
            Name=input("Enter name")
            Price=t_price
            Gender=input("Enter Gender")
            Age=input("Enter Age")
            phone_number=input("Enter Phone Number")
            if(t_price==0):
                if(seat_row<=int(x/2)):
                    t_price=10
                else:
                    t_price=8
            total_price+=t_price
            booked_seats.append(c)
            data.append(("Name : "+Name,"Price : "+str(Price),"Gender : "+Gender,"Age : "+Age,"Phone Number : "+phone_number))
            print("seat confirmed")
        else:
            print("Seat already taken or out of range")
    if(val==3):
        print("number of purchased tickets:",len(booked_seats))
        print("percentage:",((x*y)/100)*len(booked_seats))
        print("current income:",total_price)
        print("total income:",full_hall_price)
    if(val==4):
        b_row=int(input("Enter Row "))
        b_col=int(input("Enter Col "))
        if([b_row,b_col] in booked_seats):
            ind=booked_seats.index([b_row,b_col])
            for i in data[ind]:
                print (i)