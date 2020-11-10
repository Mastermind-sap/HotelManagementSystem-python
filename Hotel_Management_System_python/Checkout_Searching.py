import java.util.*
import java.text.DateFormat
import java.text.SimpleDateFormat
import java.util.Calendar
class Checkout_Searching
{
    static Scanner sc=new Scanner(System.in)
    static Hotel_Management_Software ob=new Hotel_Management_Software()
    Billing b2=new Billing()

    void checkout(int pos)    //method to check out a guest
    {
        int d=1
        do
        {
            print("Do you want to checkout?(yes/no)")  //confirming whether the guest wants to checkout
            String s=sc.next()

            if(s.equalsIgnoreCase("yes"))
            {
                d=1
                if(ob.register_no<ob.register)
                {DateFormat df = new SimpleDateFormat("dd/MM/yy HH:mm:ss")   //taking system date and time as the checkout date and time
                    Date dateobj = new Date()
                    ob.checkout_date_time[pos]=df.format(dateobj)
                    int date=Integer.parseInt(ob.checkin_date_time[pos].substring(0,2))                     //calculating the number of days stayed
                    int month=Integer.parseInt(ob.checkin_date_time[pos].substring(3,5))
                    int year=Integer.parseInt(ob.checkin_date_time[pos].substring(6,8))
                    int date1=Integer.parseInt(ob.checkout_date_time[pos].substring(0,2))
                    int month1=Integer.parseInt(ob.checkout_date_time[pos].substring(3,5))
                    int year1=Integer.parseInt(ob.checkout_date_time[pos].substring(6,8))
                    ob.day_stay[pos]=(((year1-year)*365)+((month1-month)*30)+(date1-date))
                    ob.name_r[ob.register_no]=ob.name[pos]                                          //entering the records in the register
                    ob.gender_r[ob.register_no]=ob.gender[pos]
                    ob.age_r[ob.register_no]=ob.age[pos]
                    ob.address_r[ob.register_no]=ob.address[pos]
                    ob.pan_r[ob.register_no]=ob.pan[pos]
                    ob.checkin_date_time_r[ob.register_no]=ob.checkin_date_time[pos]
                    ob.checkout_date_time_r[ob.register_no]=ob.checkout_date_time[pos]
                    ob.suite_r[ob.register_no]=ob.suite[pos]
                    ob.day_stay_r[ob.register_no]=ob.day_stay[pos]
                    ob.register_no+=1
                    print("Checkout Successful!!")
                    int b=0
                    do
                    { print("Do you want to print a bill?(yes/no)")            //asking whether the guest wants a bill or not
                        String bill=sc.next()
                        bill+=sc.nextLine()
                        if(bill.equalsIgnoreCase("yes"))
                        {b2.bill(pos)
                            b=0
                            break}
                        else if(bill.equalsIgnoreCase("no"))
                        {b=0
                            break}
                        else
                        {print("Please give your opinion in yes or no")
                            b=1}
                    }while(b==1)
                    for(int i=pos+1i<(ob.no_rooms-ob.remaining_rooms)i++)
                    {   ob.name[i-1]=ob.name[i]
                        ob.address[i-1]=ob.address[i]
                        ob.checkin_date_time[i-1]=ob.checkin_date_time[i]
                        ob.checkout_date_time[i-1]=ob.checkout_date_time[i]
                        ob.gender[i-1]=ob.gender[i]
                        ob.age[i-1]=ob.age[i]
                        ob.day_stay[i-1]=ob.day_stay[i]
                        ob.pan[i-1]=ob.pan[i]
                        ob.suite[i-1]=ob.suite[i]
                    }
                    ob.remaining_rooms+=1
                }
                else
                    print("No space in register")

            }
            else if(s.equalsIgnoreCase("no"))
            {d=1
                break}
            else
            {print("Sorry ,please give your opinion in yes or no")
                d=0}
        }while(d==0)
    }

    void search(String name)                             //method to search for a guest in the register
    {
        int available1=0
        for(int i=0i<ob.register_noi++)
        {if(available1!=1)
            {
                if(name.equalsIgnoreCase(ob.name_r[i]))
                {  available1=1
                    print("\nGuest name:"+ob.name_r[i]+"\nGender:"+ob.gender_r[i]+"\nAge:"+ob.age_r[i]+"\nAddress:"+ob.address_r[i]+"\nPAN card number:"
                        +ob.pan_r[i]+"\nCheck-in date and time(dd/MM/yy HH:mm:ss):"+ob.checkin_date_time_r[i]+"\nCheck-out date and time(dd/MM/yy HH:mm:ss):"+ ob.checkout_date_time_r[i]+"\nType of Suite:"+ob.suite_r[i]+" suite\nNumber of days stayed:"
                        +ob.day_stay_r[i])
                    break}
                else if(ob.name_r[i].startsWith(name))
                {int test1=1
                    do
                    {print("Is the guest's name "+ob.name_r[i]+" ?(yes/no)")
                        String condition1=sc.next()
                        if(condition1.equalsIgnoreCase("yes"))
                        {   test1=1
                            available1=1
                            print("\nGuest name:"+ob.name_r[i]+"\nGender:"+ob.gender_r[i]+"\nAge:"+ob.age_r[i]+"\nAddress:"+ob.address_r[i]+"\nPAN card number:"
                                +ob.pan_r[i]+"\nCheck-in date and time(dd/MM/yy HH:mm:ss):"+ob.checkin_date_time_r[i]+"\nCheck-out date and time(dd/MM/yy HH:mm:ss):"+ ob.checkout_date_time_r[i]+"\nType of Suite:"+ob.suite_r[i]+" suite\nNumber of days stayed:"
                                +ob.day_stay_r[i])
                            break
                        }
                        else if(condition1.equalsIgnoreCase("no"))
                        {test1=1
                            break
                        }
                        else
                        { print("sorry didn't get you!")
                            test1=0
                        }
                    }
                    while(test1==0)
                }
            }
        }
        if(available1==0)
            print("There is no such customer in our records")
    }

    public static void main()
    {Checkout_Searching c1=new Checkout_Searching()
        print("Enter 1 to checkout \n 2 to search for a guest in the register")
        String n1=sc.next()
        n1+=sc.nextLine()
        int n=0
        try
        { n=Integer.parseInt(n1)
        }catch(Exception e)
        {
        }
        switch(n)
        {case 1:
            print("")
            print("\t\t\t\t\t\t\t\tCheckout")
            print("\t\t\t\t\t\t\t\t********")
            print("")
            int d=0
            do
            {  d=0
                print("Enter the name of the guest")
                String se=sc.next()
                se+=sc.nextLine()
                int available=0
                for(int i=0i<(ob.no_rooms-ob.remaining_rooms)i++)
                {if(available!=1)
                    {
                        if(se.equalsIgnoreCase(ob.name[i]))
                        {   available=1
                            c1.checkout(i)
                            break
                        }
                        else if(ob.name[i].startsWith(se))
                        {int test=1
                            do
                            {print("Is the guest's name "+ob.name[i]+" ?(yes/no)")
                                String condition=sc.next()
                                condition+=sc.nextLine()
                                if(condition.equalsIgnoreCase("yes"))
                                {   test=1
                                    available=1
                                    c1.checkout(i)
                                    break
                                }
                                else if(condition.equalsIgnoreCase("no"))
                                {test=1
                                    break
                                }
                                else
                                { print("sorry didn't get you!")
                                    test=0
                                }
                            }
                            while(test==0)
                        }
                    }
                }
                if(available==0)
                {
                    print("There is no guest with this name")
                    int d1=1
                    do
                    {
                        print("Do you want to re-enter the name?(yes/no)")
                        String s=sc.next()
                        s+=sc.nextLine()
                        System.out.print("")
                        if(s.equalsIgnoreCase("yes"))
                        {
                            d1=1
                            d=1
                            break
                        }
                        else if(s.equalsIgnoreCase("no"))
                        {
                            d1=1
                            d=0
                            break
                        }
                        else
                        {print("Sorry ,please give your opinion in yes or no")
                            d1=0}
                    }
                    while(d1==0)
                }
            }while(d==1)
            break

            case 2:
            print("")
            print("\t\t\t\t\t\t\t\tSearching in records")
            print("\t\t\t\t\t\t\t\t********************")
            print("")
            print("Enter the name of the customer")
            String se=sc.next()
            se+=sc.nextLine()
            c1.search(se)
            break
            default:
            print("Wrong choice")
        }
    }
}
