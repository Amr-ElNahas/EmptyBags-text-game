bag1=10
bag2=10
bag3=10
print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
print("Start!")
import random
def human():
    global bag1
    global bag2
    global bag3
    x= eval(input("choose bag number"))
    valid_bag=False
    valid_bag_h=False
    while valid_bag==False or valid_bag_h==False:
        if bag1==0 and x==1:
            x= eval(input("bag's empty, try another bag"))
        elif bag2==0 and x==2:
            x= eval(input("bag's empty, try another bag"))
        elif bag3==0 and x==3:
            x= eval(input("bag's empty, try another bag"))
        else:
            valid_bag_h=True
        if x!=1 and x!=2 and x!=3:
            x= eval(input("choose a valid bag number"))
        else:
            valid_bag=True
    y=int(input ("insert number of objects to remove"))
    valid_o_h=False
    while valid_o_h==False:
        if y>0 and y<6:
            if x==1:
                if y>bag1:
                    y=int(input("bag doesn't have enough objects, try again"))
                else:
                    valid_o_h=True
                    bag1-=y
                    print("you removed %d objects from bag %d"%(y,x))
                    print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
            elif x==2:
                if y>bag2:
                    y=int(input("bag doesn't have enough objects, try again"))
                else:
                    valid_o_h=True
                    bag2-=y
                    print("you removed %d objects from bag %d"%(y,x))
                    print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
            else:
                if y>bag3:
                    y=int(input("bag doesn't have enough objects, try again"))
                else:
                    valid_o_h=True
                    bag3-=y
                    print("you removed %d objects from bag %d"%(y,x))
                    print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
        elif y==0:
            y=int(input("you cannot remove 0 objects, choose a number between 1 and 5 inclusive."))
        else:
            y=int(input("you cannot remove more than 5 objects, choose a number between 1 and 5 inclusive."))
def comp():
    global bag1
    global bag2
    global bag3
    a=random.randint(1,3)
    b=random.randint(1,5)
    valid_o_c=False
    valid_bag_c=False
    while valid_bag_c==False:
        if bag1==0 and a==1:
            a=random.randint(1,3)
        elif bag2==0 and a==2:
            a=random.randint(1,3)
        elif bag3==0 and a==3:
            a=random.randint(1,3)
        else:
            valid_bag_c=True
    while valid_o_c==False:
        if a==1:
            if b>bag1:
                b=random.randint(1,5)
            else:
                valid_o_c=True
                bag1-=b
                print("computer took %d objects from bag %d"%(b,a))
                print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
        elif a==2:
            if b>bag2:
                b=random.randint(1,5)
            else:
                valid_o_c=True
                bag2-=b
                print("computer took %d objects from bag %d"%(b,a))
                print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
        else:
            if b>bag3:
                b=random.randint(1,5)
            else:
                valid_o_c=True
                bag3-=b
                print("computer took %d objects from bag %d"%(b,a))
                print("bag 1 has %d objects, bag 2 has %d objects, bag 3 has %d objects"%(bag1,bag2,bag3))
while bag1+bag2+bag3!=0:
    human()
    if bag1+bag2+bag3==0:
        print("you won, congrats")
        break
    comp()
    if bag1+bag2+bag3==0:
        print("you lost, game over")
