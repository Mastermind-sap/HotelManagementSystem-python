import Registration, Billing, Checkout_Searching


class Hotel_Management_Software:
    def __init__(self):
        print("")
        print("\t\t\t\t\t\t\t\tHotel Management Software")
        print("\t\t\t\t\t\t\t\t*************************")
        print("")
        self.no_rooms = 100
        self.name = self.gender = self.address = self.checkin_date_time = self.checkout_date_time = self.suite = self.name_r = self.gender_r = self.address_r = self.checkin_date_time_r = self.checkout_date_time_r = self.suite_r = self.pan = self.pan_r = self.age = self.day_stay = self.age_r = self.day_stay_r = []
        self.remaining_rooms = self.no_rooms
        self.register = 200
        self.register_no = 0

    def main(self):
        flag = 0
        while flag == 0:
            print("Enter 1 for Registration\n      2 for Billing\n      3 for Checkout/Searching")
            d1 = 0
            while d1 == 0:
                try:
                    choice = int(input("Option:"))
                except ValueError:
                    print("Invalid Choice")
                    print("Try Again!")
                else:
                    d1 = 1

            print(
                "******************************************************************************************************************************* \n ")
            if choice == 1:
                r = Registration()  # Registration of the guest
                r.main()
            elif choice == 2:
                b = Billing()  # To print a bill for the guest
                b.main()
            elif choice == 3:
                c = Checkout_Searching()  # To check out the guest or to search for a guest who has already checked out
                c.main()
            else:
                print("Wrong choice")
            print()
            d = 1
            while d == 1:
                # To take user's input on whether the program should again start from the beginning
                s = input("Do you want to continue?(yes/no)")
                if s.lower() == "yes":
                    print(
                        "******************************************************************************************************************************* \n ")
                    break
                elif s.lower == "no":
                    print("\t\t\t\t\t\t\t\t\t***THANK YOU***")
                    flag = 1
                    break
                else:
                    print("Sorry ,please give your opinion in yes or no")


run = Hotel_Management_Software()
run.main()
