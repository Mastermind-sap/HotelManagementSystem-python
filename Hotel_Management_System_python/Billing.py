import java.util.*
import java.text.DateFormat
import java.text.SimpleDateFormat
import java.util.Calendar
class Billing
{  static Hotel_Management_Software ob=new Hotel_Management_Software()
    static Scanner sc=new Scanner(System.in)

    void bill(int i)                                //method for printing bill of the guest
    {int n1=0
        if(ob.checkout_date_time[i]==null)
        {DateFormat df = new SimpleDateFormat("dd/MM/yy HH:mm:ss")
            Date dateobj = new Date()
            String d1=df.format(dateobj)
            int date=Integer.parseInt(ob.checkin_date_time[i].substring(0,2))        //calculating the number of days stayed
            int month=Integer.parseInt(ob.checkin_date_time[i].substring(3,5))
            int year=Integer.parseInt(ob.checkin_date_time[i].substring(6,8))
            int date1=Integer.parseInt(d1.substring(0,2))
            int month1=Integer.parseInt(d1.substring(3,5))
            int year1=Integer.parseInt(d1.substring(6,8))
            n1=(((year1-year)*365)+((month1-month)*30)+(date1-date))
        }
        else
            n1=ob.day_stay[i]

        print("")
        print("\t\t\t\t\t\t\t\t\t\tBill")
        print("\t\t\t\t\t\t\t\t\t\t****")
        print("")
        print("Guest name:"+ob.name[i]+"\nGender:"+ob.gender[i]+"\nAge:"+ob.age[i]+"\nAddress:"+ob.address[i]+"\nPAN card number:"
            +ob.pan[i]+"\nCheck-in date and time(dd/MM/yy HH:mm:ss):"+ob.checkin_date_time[i]+"\nCheck-out date and time(dd/MM/yy HH:mm:ss):"+ ob.checkout_date_time[i]+"\n\t----------------------------------------------------------------------------------------------------")
        double rate=0.0,amount=0.0
        if(ob.suite[i]=="Deluxe")
        {rate=2000
            amount=n1*rate}
        else if(ob.suite[i]=="Super Deluxe")
        {rate=4000
            amount=n1*rate}
        else if(ob.suite[i]=="Executive")
        {rate=6000
            amount=n1*rate}
        else if(ob.suite[i]=="Presidential")
        {rate=8000
            amount=n1*rate}
        print("Room type \t\t | \t Room rate(per day) \t | \t Number of days stayed \t | \t Gross Amount")
        print(ob.suite[i]+" suite \t | \t"+rate+"\t\t\t | \t "+n1 +" \t\t\t | \t "+amount)
        print("-------------------------------------------------------------------------------------------")
        print("\t\t\t\t |   Tax type\t|  Tax rate \t\t| Tax Amount")
        print("\t\t\t\t |   CGST \t|  14% \t\t\t| "+((14.0/100.0)*amount))
        print("\t\t\t\t |   SGST \t|  14% \t\t\t| "+((14.0/100.0)*amount))
        print("\t\t\t\t ------------------------------------------------")
        print("\t\t\t\t Net Amount "+(amount+((14.0/100.0)*amount)+((14.0/100.0)*amount)))
        print("")
        print("==========================================================================")
        print("")
    }

    public static void main()
    {
        print("")
        print("\t\t\t\t\t\t\t\tBilling")
        print("\t\t\t\t\t\t\t\t*******")
        print("")
        Billing b1=new Billing()
        int d=0
        do
        {    d=0
            print("enter the name of the guest whose bill needs to be printed")
            String se=sc.next()
            se+=sc.nextLine()
            int available=0
            for(int i=0i<(ob.no_rooms-ob.remaining_rooms)i++)      //searching the guest whose bill needs to be printed
            {if(available!=1)
                {
                    if(se.equalsIgnoreCase(ob.name[i]))
                    {   available=1
                        b1.bill(i)
                        break
                    }
                    else if(ob.name[i].startsWith(se))
                    {int test=1
                        do
                        {print("Is the guest's name "+ob.name[i]+" ?(yes/no)")
                            String condition=sc.next()
                            if(condition.equalsIgnoreCase("yes"))
                            {   test=1
                                available=1
                                b1.bill(i)
                                break
                            }
                            else if(condition.equalsIgnoreCase("no"))
                            {test=1
                                break}
                            else
                            {print("sorry didn't get you!")
                                test=0}
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
    }
}
