import time
import datetime


class Helper():
    """
    ## Helper Class
    - This class contains logic and functionality of ATM Simulation
    -----------------------------------------------------------------
    The following functionality was implemented
    - Account Balance 
    - Cash Withdrawal
    - Cash Depsit
    - PIN Change
    - Transaction History

    ~ NB: May contain bugs

    ~ version 1.0

    """

     # ATM Basic Functions
    # This method initializes welcome message and the  basic atm functionaliy 
    # to the user and the user will have 
    # to choose one of it.
    def __init__(self):
        self.welcome_msg = """
        ====================================================
        ============== WELCOME TO OCTANET ATM ==============
        Your N0.1 reliable Bank you can trust with security.

        """

        self.instruction = """
        What do you want to do today?

        1. Account Balance Inquiry
        2. Cash Withdrawal
        3. Cash Deposit
        4. Pin Change
        5. Transaction History
        6. Exit
        """

        # Default account balance
        self.balance = 10000
        
        # defalut currency to Ghana cedis
        self.currency = 'GHS'

        # check if user is logged in
        self.isLogin = False

        # defalut atm pin
        self.pin = 2024

        # counter. This check the number of failed logins
        self.failed_login = 0

        # transaction history db
        self.transaction_history = []
        
    
    # Welcome message
    # @return welcome message to the user
    def welcome(self):

        if(self.isLogin):
            print(f'{self.welcome_msg}  {self.instruction}')

            try:
                # check user option and process it
                self.user_option = int(input('Enter option: '))

                # checking account balance
                if(self.user_option == 1):
                    # delay by 1s
                    self.delay(1)

                    print('...')
                    #delay by 2s
                    self.delay(2)
                    print(f'Your currnt balance is {self.currency} {self.balance}')
                    self.delay(1)
                    print('...')
                    self.delay(2)
                    self.welcome()

            except:
                print('Incorrect option.')
                self.delay(1)
                print('...')
                self.delay(1)
                self.welcome()
                
            
            # Cash withdrawal
            if(self.user_option == 2):

                self.amount = int(input('Enter amount to withdraw: '))
                # delay by 1s
                self.delay(1)
                print('Processing...')

                # check if amount is not greater than balance
                if(self.amount < self.balance ):
                    # deduct amount from current balance
                    self.balance = self.balance-self.amount

                    # add record to transaction history
                    self.transaction_history.append('You withdrawn an amount of {} | Date: {} and Time: {}'.format(self.amount, self.getDate(), self.getTime()))

                    # delay for 1 second
                    self.delay(1)
                    print(f'You have withdrawn {self.currency} {self.amount} from Octanet ATM')
                    print(f'Your currnt balance is {self.currency} {self.balance}')
                    self.delay(1)
                    print('...')
                    self.delay(2)
                    self.welcome()

                else:
                    # amount to withdraw is greater than account balance
                    # delay program for 3s and re-run welcome screen
                    print('You have insufficient balance in your account')
                    self.delay(1)
                    print('...')
                    self.delay(2)
                    self.welcome()


            # Deposit money into account
            if(self.user_option == 3):
                self.amount = int(input('Enter amount to deposit: '))
                # delay by 1s
                self.delay(1)
                print('Processing...')
                
                # add amount to current balance
                self.balance = self.balance + self.amount

                # add record to transaction history
                self.transaction_history.append('You deposited an amount of {} | Date: {} and Time:{}'.format(self.amount,self.getDate(), self.getTime()))
                
                # delay for 1 second
                self.delay(1)
                print(f'You have deposited and amount of {self.currency} {self.amount} from Octanet ATM')
                print(f'Your currnt balance is {self.currency} {self.balance}')
                self.delay(1)
                print('...')
                self.delay(2)
                self.welcome()

            # Change PIN
            if(self.user_option == 4):
                print('You are about to change your ATM PIN')

                # handle input exception
                try:
                    # ask user to input new pin
                    self.settings = int(input('Enter your new pin: '))

                    # change default pin to new pin
                    self.pin = self.settings
                    self.delay(1)
                    print('Updating password...')
                    print('Finishing setting up...')
                    self.delay(1)
                    print('Done!')
                    print('Your pin code successfully updated.')
                    print('Let\'s log in again...')
                    
                    # log user out and redirect to login
                    self.isLogin = False

                    # log user into the system
                    self.login()
                    
                except:
                    print('Please enter numbers only')
                    self.delay(1)
                    print('...')
                    self.delay(1)
                    self.welcome()

            # Transaction History
            if(self.user_option == 5):
                print('\n')
                print('Your Transaction History')
                print('================================')
                
                # Check if transaction history is empty
                if len(self.transaction_history) == 0:
                    print('No Transaction History. Do more transaction with OCTANET ATM. ')
                    
                # loop through transaction and print each on a separate line 
                for self.history in self.transaction_history:
                    print(self.history)
                    print('---------------------------------------------------')

                # delay for 4s and re-run welcome scren  
                self.delay(2)
                print('...')
                self.delay(2)
                self.welcome()

            # Exiting the ATM
            if(self.user_option == 6):
                self.isLogin = False
                print('Exiting...')
                self.delay(1)
                print('GOOD BYE')
                exit(0)


    # this function log the user into the ATM interface
    def login(self):

        print(f'{self.welcome_msg}')
        
        # allow program to re-run and exit upon user command
        # i.e. if user enter exit number.
        while True:
            # handle input exception
            try:
                # check user login attemps
                if(self.failed_login == 3):
                    # user has reached login attempts, break from the loop and exit
                    print('Login Attempts reached. Please re-run the program.')
                    print('Exiting.....')
                    time.sleep(2)
                    break
                else:
                    # handle input exception
                    try:
                        # ask user to enter ATM PIN
                        self.pin_code = int(input('Enter your pin: '))

                        #if pin matches, log user in by setting self.isLogin = True
                        if(self.pin_code == self.pin):
                            self.isLogin = True
                            break
                        else:
                            # if wrong pin, set self.isLogin = True and increase self.failed_login by 1
                            print('Invalid PIN. Try again: ')
                            self.isLogin = False
                            self.failed_login += 1
                    except:
                        # if wrong pin, set self.isLogin = True and increase self.failed_login by 1
                        # Here if user enters characters & sysbols instead of numbers
                        print('Input Error: Enter number only. Trying again: ')
                        self.isLogin = False
                        self.failed_login += 1
                        # delay for 1s
                        self.delay(1)

            # catch errors if try block failed to execute
            except:
                print('System encountered an unknown error: ')
                print('Exiting.....')
                time.sleep(2)
                break
           
                

        # Launch welcome screen
        # This only runs upon succesful login
        self.welcome()  

    # delay time
    def delay(self,seconds = 0):
        time.sleep(seconds)


    # get date only
    def getDate(self) -> str:
        self.current_date = datetime.datetime.now()
        self.formated_date = self.current_date.strftime('%Y-%m-%d')

        return self.formated_date

    # Get time only
    def getTime(self) -> str:
        self.current_date = datetime.datetime.now()
        self.formated_date = self.current_date.strftime('%H:%M:%S')

        return self.formated_date
    
    