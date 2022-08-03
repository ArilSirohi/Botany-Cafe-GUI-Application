# Importing Kivy, app widget, ScreenManager, object properties and Labels in python

'''Kivy - importing required functions, classes and methods for Graphical User Interface
   App  - importing for working on numerous devices and future proofing. Application can be used on windows,android and ios devices
   ScreenManager - importing Screens in Kivy framework that allows for multiple user input screens,windows and animations
   Label - Graphical User interface object used for displaying texts
   ObjectProperty - sets object value to the token ID in kivy file for working with defined widgets in python. This helps python to take user input and execute functions 
   StringProperty - sets string value to the token ID in kivy file for working with defined widgets in python. This helps python to take user input and execute functions 
   BooleanProperty- sets boolean value to the token ID in kivy file for working with defined widgets in python. This helps python to take user input and execute functions
   '''

import kivy 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.audio import SoundLoader

# Initialization
'''These lists, strings and constants are set up when application is started. These are used throughout the program and therefore initialized 
everytime the application is opened. 
'''

'''User related lists'''
user_list = [ ]
password_list = [  ]
user_orders = [ ]
username = '' 
user_address_list = [ ]

'''Menu items lists'''
items_list = [ ]
item_names = [ ]
item_prices = [ ]

'''Price of items that user has added in the cart after checkout'''
total_price = [ ]
total = 0

# User Class that has user related functions including usernames, password, login and new account  
class User():

    # Opens Username text file and appends the usenames in user list 
    def userfile():
            with open ('userfile.txt', 'r') as userfiles:
                lines = userfiles.readlines()
                for line in lines:
                    members = line.split()
                    for member in members:
                        user_list.append(member)
                userfiles.close()
    
    # Opens Password text file and appends the passwords in password list 
    def passwordfile():
            with open ('passwordfile.txt', 'r') as passwordfile:
                lines = passwordfile.readlines()
                for line in lines:
                    members = line.split()
                    for member in members:
                        password_list.append(member)
                str(password_list)
                passwordfile.close()
  
    # removes password and username of previous user from GUI after user clicks on 'login' for privacy, allowing multiple program uses
    def user_login_try(self):
        self.login_username.text = ''
        self.login_password.text = ''

     # Removes user information from python lists for maintaining privacy of username and password from other users 
    def user_logout():
        user_list.clear()
        password_list.clear()

    #Login for user. Uses userfile() and passwordfile() for a 2D List in python that is checked using 'for loop'
    def login_status(self):

        '''For future proofing, the textfiles and external database storage can be changed without affecting Login method 
        by calling them like bellow. By changing the text file name in userfile() or passwordfile() the 2D list is updated dynamically,
        resulting in minimizing the amount of code. userlogout() is used for safety reasons by remmoving sensitive information from the program
        after it has been utilized in python for matching registered usernames and passwords'''

        User.userfile()
        User.passwordfile()   
        
        for i in range(len(user_list)):
            if str(self.login_username.text) == user_list[i]:
                if self.login_password.text == password_list[i]:
                    self.error_message = f'You have logged in successfully {self.login_username.text}!\n          You can access the Menu'
                    self.menu_enabled = True
                    username = str(self.login_username.text)
                    break
                break
            else:
                self.error_message = 'Please check your Username or Password\nand Try Again'
                self.menu_enabled = False         
        else:
            self.error_message = 'Please check your Username or Password\nand Try Again'
            self.menu_enabled = False
            self.login_username.text = ''
            self.login_password.text = ''
          
        User.user_logout()

    # New Account method for new users. If user age is valid, saves username and password in seperate text files. Updates labels on Graphical User Interface
    def new_account(self):
        print(self.user_age.text)
        try:
            if self.user_age.text == '':
                self.error_message_2 = 'Please enter your age'

            elif str(self.new_username.text) == '':
                    self.error_message_2 = 'Please enter a valid username'

            elif str(self.new_password.text) == '':
                self.error_message_2 = 'Please enter a valid password'           
            else:
                
                if int(self.user_age.text) >= 16 and int(self.user_age.text) <= 100:
                    username = self.new_username.text
                    password = self.new_password.text

                    with open('usernames.txt','a') as usernames:
                        usernames.write(username + '\n')
                        usernames.close()
                    with open('passwordfile.txt','a') as passwords:
                        passwords.write(password + '\n')
                        passwords.close()

                    self.new_username.text = ''
                    self.new_password.text = ''
                    self.user_age.text = ''
                    self.error_message_2 = 'You are registered! Please click Return and Login'

                elif int(self.user_age.text) < 16:
                    self.error_message_2 = 'You are under 16!'
                else:
                    self.error_message_2 = 'Your age is above boundary limit!'
        except:
            self.error_message_2 = 'Please type a number'

# Menu class with methods for chooosing items, quantity and appending item lists from text files which are binded to button click. 
# These metohds of Menu class are linked with 'my.kv' kivy file for button click to work properly. 
class Menu():

   # Shows recently chosen item name to user on Menu Screen. Every even numbered item in 'user_orders' list is item name and odd numbered are prices.  
    def view_cart(self):

        cart = [ ]
        item_count = 0
        self.cart_message = 'Your items'
        for items in user_orders:
            if item_count% 2 == 0:
                cart.append(items)
                item_count+=1

            else:           
                item_count+= 1
        if cart == []:
            self.items = f'Your cart is empty'
            self.delivery_enabled = False

        else:
            self.items = f'''{cart}'''
            self.delivery_enabled = True

    # Adds prices of items chosen and stores in 'total' variable. 

    '''Checks if the user input is in integers. Items prices and quantity are sotred in seprate variables, multiplied and shown to users as 'total' price
       Users choose the item using Item Number(IN) which are in integers, that are matched with index of items from 'item_names' list and appended to user
       cart. The boundary for item selection and quantity is 1.'''

    '''Global variables are avoided as much as possible as they can throw errors later in development. Only the following variable has been
       made global to update the value of 'total' to allow users place miltiple orders without closing and opening the application, increasing Usability. 
       Logging out clears the user cart but keeps previous value of 'total' (Example, User 'A' order costing $2 is added during
       User 'B' checkout, due to 'Add Item' button pressed more than once by User 'B') To allow multiple uses without logging in again, total is reset
       after each use by using global'''

    def add_item(self):
        global total
 
        try:
            if int(self.item_number.text) <= 0:
                self.menu_item_message = f'Please enter positive value !'
                print('check')

            elif int(self.quantity.text) <= 0 or int(self.quantity.text) >= 12:
                self.menu_item_message = f'Please enter valid amount !'
                print('check')

            else: 
                user_orders.append(item_names[int(self.item_number.text)-1])
                user_orders.append(int(self.quantity.text))
                str(user_orders)
                total_price.append(item_prices[int(self.item_number.text)-1])
                total += float(total_price[0])*int(self.quantity.text)

                for items in range(0,len(user_orders),2):
                    self.menu_item_message = f'Recently Added to your cart: {user_orders[items]}\nTotal: ${total}'
                total_price.clear()
        except:
            self.menu_item_message = f'Please select Item Number(IN)\nfrom available items!'
   
    # deletes cart items 
    '''Same variable called 'total' set to global for resetting throughout the program. '''

    def clean_cart(self):
        global total
        total = 0
        items_list.clear()
        item_names.clear()
        item_prices.clear()
        self.cart_message = 'Your cart is empty'

    # Item Category text file 1 from which item names and prices are appended as 2D lists in items_list as ['item name', 'item price']

    '''The following methods ( Category_1, Category_2, Category_3 ) append the item names from external databse such as textfiles and display on Menu.
       Number of items are limited to 10 for efficiency which can be increased. As there are three seperate buttons for each category, the method 
       is specific to the button ( Food, Beverage and Specials ) 
    '''

    def category_1(self):
        item_count = 0 
        with open ('Food.txt', 'r') as category_1:
                lines = category_1.readlines()
                for line in lines:
                    items = line.split('$')
                    for item in items:
                        items_list.append(item)
                category_1.close()
          
        for items in items_list:
            if item_count% 2 == 0:
                item_names.append(items)
                item_count+=1
            else:
                item_prices.append(items)
                item_count+= 1
        self.category_heading = ''' IN     Food and Prices'''     
        self.items = f'''
        1)     {item_names[0]}  ${item_prices[0]}
        2)     {item_names[1]}  ${item_prices[1]}
        3)     {item_names[2]}  ${item_prices[2]}
        4)     {item_names[3]}  ${item_prices[3]}
        5)     {item_names[4]}  ${item_prices[4]}
        6)     {item_names[5]}  ${item_prices[5]}
        7)     {item_names[6]}  ${item_prices[6]}
        8)     {item_names[7]}  ${item_prices[7]}  
        9)     {item_names[8]}  ${item_prices[8]}
        10)    {item_names[9]}  ${item_prices[9]} 
        '''
    
    # Item Category text file 2 from which item names and prices are appended as 2D lists in items_list as ['item name', 'item price']
    def category_2(self):
        item_count = 0 
        with open ('Beverages.txt', 'r') as category_2:
                lines = category_2.readlines()
                for line in lines:
                    items = line.split('$')
                    for item in items:
                        items_list.append(item)                
                category_2.close()

        for items in items_list:
            if item_count% 2 == 0:
                item_names.append(items)
                item_count+=1
            else:
                item_prices.append(items)
                item_count+= 1

        self.category_heading = '''   IN     Drinks and Prices'''     
        self.items = f'''
        1)     {item_names[0]}  ${item_prices[0]}
        2)     {item_names[1]}  ${item_prices[1]}
        3)     {item_names[2]}  ${item_prices[2]}
        4)     {item_names[3]}  ${item_prices[3]}
        5)     {item_names[4]}  ${item_prices[4]}
        6)     {item_names[5]}  ${item_prices[5]}
        7)     {item_names[6]}  ${item_prices[6]}
        8)     {item_names[7]}  ${item_prices[7]}  
        9)     {item_names[8]}  ${item_prices[8]}
        10)    {item_names[9]}  ${item_prices[9]}
                     '''
 
    # Item Category text file 3 from which item names and prices are appended as 2D lists in items_list as ['item name', 'item price']
    def category_3(self):
        item_count = 0 
        with open ('Specials.txt', 'r') as category_3:
                lines = category_3.readlines()
                for line in lines:
                    items = line.split('$')
                    for item in items:
                        items_list.append(item)
                category_3.close()
        
        for items in items_list:
            if item_count% 2 == 0:
                item_names.append(items)
                item_count+=1
            else:
                item_prices.append(items)
                item_count+= 1

        self.category_heading = '''IN    Specials and Prices'''     
        self.items = f'''
        1)     {item_names[0]}  ${item_prices[0]}
        2)     {item_names[1]}  ${item_prices[1]}
        3)     {item_names[2]}  ${item_prices[2]}
        4)     {item_names[3]}  ${item_prices[3]}
        5)     {item_names[4]}  ${item_prices[4]}
        6)     {item_names[5]}  ${item_prices[5]}
        7)     {item_names[6]}  ${item_prices[6]}
        8)     {item_names[7]}  ${item_prices[7]}  
        9)     {item_names[8]}  ${item_prices[8]}
        10)    {item_names[9]}  ${item_prices[9]}
                     '''
                     
# Orders class that contains methods of confirming order and address of users
class Orders():

    # Adds username, orders and total price in 'Orders' text file 
    def confirmed_order(self):
        self.delievery_confirmed = False
        with open('orders.text','a') as orders:
            orders.write(f'{str(self.login_username.text)} ordered {user_orders} for ${total + 2}\n')
            orders.close()

    # Adds user address in 'address' text file and binded to 'Online' delivery button 
    def confirmed_address_online(self):
        with open('address.text','a') as address:
                address.write(f'User: {self.login_username.text}\naddress: online\n__________\n')
                address.close()

    # Adds user address in 'address' text file and binded to 'Home' delivery button, also adds $2 for home delievery
    def confirmed_address_home(self):
        print(self.user_address.text)
        if str(self.user_address.text) == '':
            self.delievery_message = 'Please enter a valid address'          
        else:
            user_address_list.append(self.user_address.text)
            self.delievery_message = 'Confirm Order?'
            self.delievery_confirmed = True
            with open('address.text','a') as address:
                address.write(f'User: {self.login_username.text}\naddress: {self.user_address.text}\n__________\n')
                address.close()


# Kivyfile class for organizing 'my.kv' Kivy file's token IDs for defining objects and python to execute functions
'''The labels, hint texts are updated dynamically by assigning the ID to a variable in python file. The property of widget, objects used in kivy 
   has to be defined in python for managing application behaviour ( Exampple - button click takes user to next screen)'''
class KivyFile():
    # Assigning property value of variables for Graphical User Interface to send to .py file 

    login_username = ObjectProperty(None)
    login_password = ObjectProperty(None)
    item_number = ObjectProperty(None)
    quantity = ObjectProperty(None)
    user_age = ObjectProperty(None)
    user_address = ObjectProperty(None)
    category_heading = StringProperty(f'')
    items = StringProperty(f'')
    greeting_message = StringProperty('Welcome to Ordering Application!')
    error_message = StringProperty('')
    error_message_2 = StringProperty('')
    menu_item_message = StringProperty('')
    cart_message = StringProperty('')
    delievery_message = StringProperty('')
    delievery_confirmed = BooleanProperty(False)
    menu_enabled = BooleanProperty(False)
    delivery_enabled = BooleanProperty(False)

# Kivyfile class for organizing 'my.kv' Kivy file's token IDs for defining objects and python to execute functions
'''The labels, hint texts are updated dynamically by assigning the ID to a variable in python file. The property of widget, objects used in kivy 
   has to be defined in python for managing application behaviour ( Exampple - button click takes user to next screen)'''
class Display(ScreenManager, KivyFile, User, Menu, Orders):

    # Return function for Graphical User Interface. Refreshes the program's labels, error messages, hint texts and takes user to previous screen
    '''This function is used to refresh the program's functions and set labels,
       text inputs to default and lets the application be used multiple times 
       without leaving, forming a loop without the need for user to close the program and login again.
       This function works with other classes when defined under main 'Display' class'''

    def return_status(self):
        self.error_message = f''
        self.error_message_2 = ''
        self.delievery_message = ''
        self.new_username.text = ''
        self.new_password.text = ''
        self.user_age.text = ''
        self.item_message = ''
        self.item_number.text = ''
        self.quantity.text = ''
        self.user_address.text = ''
        user_orders.clear()
        total_price.clear()
        self.menu_enabled = False
        self.delievery_confirmed = False
        total = 0

    # Sounds for click, cart and order confirmation 
    def play_click(self):
        self.sound = SoundLoader.load('click.wav')
        self.sound.play()

    def play_cart(self):
        self.sound = SoundLoader.load('Cart.wav')
        self.sound.play()

    def play_order(self):
        self.sound = SoundLoader.load('order.wav')
        self.sound.play()


# MyApp class for importing properties of base kivy App class.  'App' class is imported and assigned to 'MyApp' for custom types 
'''This allows applying custom properties defined in my.kv kivy file for buttons,labels,hint texts,images and text inputs''' 
class BotanyCafe(App):

    '''This is the base for Kivy applications and main Kivy run loop. 'build' returns an empty widget and takes property from 'my.kv' kivy file 
       while functions are executed by returning 'Display' Class'''

    def build(self):
        return Display()

# Executing mainloop and MyApp class 
'''This lets the application to be used multiple times without closing it.'''
if __name__ == "__main__":
    BotanyCafe().run()
