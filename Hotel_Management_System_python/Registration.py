import Hotel_Management_Software
class Registration:
    def main(self):
        print("")
        print("\t\t\t\t\t\t\t\t\tRegistration")
        print("\t\t\t\t\t\t\t\t\t************")
        print("")
        ob=Hotel_Management_Software()
        g=0
        n1=0
        while g==0:
            #Input for number of guests to be registered
            try:
                n1 = int(input("enter number of guests"))
            except ValueError:
                print("Invalid input")
            else:
                g = 1
                break
            finally:
                if  (n1==0) or (n1<1):
                    g=0
                    print("Invalid input")
        if n1<=ob.remaining_rooms:
            i = (ob.no_rooms - ob.remaining_rooms)
            for d in range(0,n1):
                ob.remaining_rooms=ob.remaining_rooms-1
                ob.name[i]=input("enter name of the guest")  #input for the name of the guest to be registered
                f=0
                #input for the gender of the guest to be registered
                while f==0:
                    choice=input("enter 'M' if guest is a male\n      'F' if guest is a female")[0].upper()
                    if choice=='M':
                        ob.gender[i]="male"
                        break
                    elif choice=='F':
                        ob.gender[i]="female"
                        break
                    else:
                        print("Invalid input")


                #input for the age of the guest to be registered
                g1=0
                while g1==0:
                    try:
                        ob.age[i]=int(input("enter age of the guest in years"))
                    except ValueError:
                        print("Invalid age")
                        print("Try Again!")
                    else:
                        if(ob.age[i]==0) or (ob.age[i]<1) or (ob.age[i]>110):
                            print("Invalid age")
                            print("enter age of the guest again")
                        else:
                            g1=1
                            break

                #input for the address of the guest to be registered
                ob.address[i]=input("enter address of the guest")


                print("enter PAN number of the guest")   #input for the PAN number of the guest to be registered
                int p=0
                do
                {
                    ob.pan[i]=sc.next()
                    ob.pan[i]+=sc.nextLine()
                    ob.pan[i]=ob.pan[i].toUpperCase()
                    if((ob.pan[i].length()==10)&&(Character.isLetter(ob.pan[i].charAt(0)))&&(Character.isLetter(ob.pan[i].charAt(1)))
                    &&(Character.isLetter(ob.pan[i].charAt(2)))&&(Character.isLetter(ob.pan[i].charAt(3)))
                    &&(Character.isLetter(ob.pan[i].charAt(4)))&&(Character.isDigit(ob.pan[i].charAt(5)))
                    &&(Character.isDigit(ob.pan[i].charAt(6)))&&(Character.isDigit(ob.pan[i].charAt(7)))
                    &&(Character.isDigit(ob.pan[i].charAt(8)))&&(Character.isLetter(ob.pan[i].charAt(9))))
                        p=0
                    else
                    {print("invalid PAN number")
                        print("PAN structure is as follows: AAAPL1234C")
                        print("please enter the PAN number again")
                        p=1
                    }

                }while(p==1)









                DateFormat df = new SimpleDateFormat("dd/MM/yy HH:mm:ss")        #Take the system date and time as the check in date and time
                Date dateobj = new Date()
                ob.checkin_date_time[i]=df.format(dateobj)

                int w=0                                                      #Input for the type of suit the guest wishes to live in
                while(w==0)
                {
                    print("Enter 1 for Deluxe suit-- Rs.2000/day \n 2 for Super Deluxe suit-- Rs.4000/day \n 3 for Executive suit-- Rs.6000/day  \n 4 for Presidential suite-- Rs.8000/day ")
                    String s1=sc.next()
                    s1+=sc.nextLine()
                    int s=0
                    try
                    { s=Integer.parseInt(s1)
                    }catch(Exception e)
                    {
                    }

                    switch(s)
                    {
                        case 1:
                        ob.suite[i]="Deluxe"
                        w=1
                        break
                        case 2:
                        ob.suite[i]="Super Deluxe"
                        w=1
                        break
                        case 3:
                        ob.suite[i]="Executive"
                        w=1
                        break
                        case 4:
                        ob.suite[i]="Presidential"
                        w=1
                        break
                        default:
                        print("Wrong choice")
                    }
                }
            }
            print("")
            print("\t\t\t\t\t\t\t\tRegistration is complete!")
            print("\t\t\t\t\t\t\t\t*************************")
            print("")
        }
        else
        {
            print("Sorry ,we are out of rooms")                                          #inavailibity of rooms in the hotel
            print("We have only "+ob.remaining_rooms+" rooms at the moment")
        }
    }
}
