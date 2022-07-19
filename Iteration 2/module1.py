import kivy 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.scrollview import ScrollView

# function for login here, checks the value entered from mainframe1 to the list of names

user_list = [ ]
password_list = [  ]
user_orders = [ ]
accounts = []
username = '' 
user_address_list = [ ]
#list1 = ['Max','123']

items_list = [ ]
item_names = [ ]
item_prices = [ ]
total_price = [ ]
total = 0
#user1 = ''
#user2 = ''
#s
  


    #print(item2)



#orders()   

class User():

    #def userlogin():
    #login_count = 0
    #login_limit = 1

    def userfile():
            with open ('usernames.txt', 'r') as userfiles:
                lines = userfiles.readlines()
                for line in lines:
                    members = line.split()
                    for member in members:
                        user_list.append(member)
                userfiles.close()
                #print(user_list)
    #userfile()

    def passwordfile():
            with open ('passwordfile.txt', 'r') as passwordfile:
                lines = passwordfile.readlines()
                for line in lines:
                    members = line.split()
                    for member in members:
                        password_list.append(member)
                str(password_list)
                passwordfile.close()
                #print(password_list)
    #passwordfile()
    def delievery():
        with open('orders.txt','a') as orders:
            orders.write(username + '\t' + str(user_orders) + '\n')
            orders.close()


    def address():
        with open('address.txt','a') as orders:
            orders.write(username + '\t' + str(user_orders) + '\n')
            orders.close()
        pass

    '''if login_count == login_limit:
        user_list = [ ]
        password_list = [ ]
        #login_count -= 1

        userfile()
        passwordfile()

    else:
        userfile()
        passwordfile()
        login_count += 1'''



    def userlogout():
        user_list.clear()
        password_list.clear()




class Kivyfile():
    #val = 'True'
    user_username = ObjectProperty(None)
    user_password = ObjectProperty(None)
    message = ObjectProperty(None)
    item_name = ObjectProperty(None)
    quantity = ObjectProperty(None)
    user_age = ObjectProperty(None)
    user_address = ObjectProperty(None)
    items = StringProperty(f'')
    my_text = StringProperty('Hello')
    error_message = StringProperty('')
    error_message_2 = StringProperty('')
    #items_list = StringProperty(f'{item_names}')
    item_message = StringProperty('')
    cart_message = StringProperty('')
    delievery_message = StringProperty('')
    delievery_confirmed = BooleanProperty(True)
    count_enabled = BooleanProperty(False)


class Display(ScreenManager, Kivyfile, User):


    def confirmed_order(self):
        self.delievery_message = 'Your order has been placed!'
        self.delivery_confirmed = False
        with open('orders.text','a') as orders:
            orders.write(f'{str(self.user_username.text)} ordered {user_orders} for ${total}\n')
            orders.close()

    def confirmed_order_home(self):
        user_address_list = [ ]
        user_address_list.append(self.user_address.text)
        self.delievery_message = 'Your order has been placed!'
        self.delivery_confirmed = False
        with open('address.text','a') as address:
            address.write(f'User: {self.user_username.text}\naddress: {self.user_address.text}\n__________\n')
            address.close()
        user_address_list = [ ]


    def add_item(self):
        global total
        #total = 0
        try:
            user_orders.append(item_names[int(self.item_name.text)-1])
            user_orders.append(int(self.quantity.text))
            str(user_orders)
            for items in range(0,len(user_orders),2):
                self.item_message = f'Recently Added to your carr: {user_orders[items]}'

            total_price.append(item_prices[int(self.item_name.text)-1])
            total += int(total_price[0])*int(self.quantity.text)
            print(total)
            total_price.clear()
            '''for items in range(0,len(total_price)):
                total += (int(total_price[items])*int(self.quantity.text))
                print(total)'''
          
            
        except:
            self.item_message = f'Please enter in numbers!'
        #print(item_prices)
        #print(item_names)

        print('$' + str(total))
        print(total_price)

        #print(user_orders)

    def view_cart(self):
        cart = [ ]
        i = 0
        self.cart_message = 'Your items'
        for items in user_orders:
            if i% 2 == 0:
                cart.append(items)
                i+=1
            else:
                #item_prices.append(items)
                i+= 1
        item1 = f'''{cart}'''
        self.items = item1

        pass

    def clean_cart(self):
        #user_orders.clear()
        total = 0
        items_list.clear()
        item_names.clear()
        item_prices.clear()
 
        self.cart_message = 'Your cart is empty'


    def category_1(self):
        i = 0 
        with open ('Food.txt', 'r') as category_1:
                lines = category_1.readlines()
                for line in lines:
                    members = line.split('$')
                    for member in members:
                        items_list.append(member)

                category_1.close()
           

        for items in items_list:
            if i% 2 == 0:
                item_names.append(items)
                i+=1
            else:
                item_prices.append(items)
                i+= 1
        item1 = f'''{item_names[0]}\n{item_names[1]}\n{item_names[2]}\n{item_names[3]}\n{item_names[4]}\n{item_names[5]}\n{item_names[6]}\n{item_names[7]}\n{item_names[8]}\n{item_names[9]}'''
        self.items = item1
        
        #pass
    def category_2(self):
        i = 0 
        with open ('Beverages.txt', 'r') as category_2:
                lines = category_2.readlines()
                for line in lines:
                    members = line.split('$')
                    for member in members:
                        items_list.append(member)
                 
                category_2.close()
        for items in items_list:
            if i% 2 == 0:
                item_names.append(items)
                i+=1
            else:
                item_prices.append(items)
                i+= 1
        item1 = f'''{item_names[0]}\n{item_names[1]}\n{item_names[2]}\n{item_names[3]}\n{item_names[4]}\n{item_names[5]}\n{item_names[6]}\n{item_names[7]}\n{item_names[8]}\n{item_names[9]}'''
        self.items = item1
        
 
        #pass
    def category_3(self):
        i = 0 
        with open ('Offers.txt', 'r') as category_3:
                lines = category_3.readlines()
                for line in lines:
                    members = line.split('$')
                    for member in members:
                        items_list.append(member)
                 
                category_3.close()
           

        for items in items_list:
            if i% 2 == 0:
                item_names.append(items)
                i+=1
            else:
                item_prices.append(items)
                i+= 1
        item1 = f'''{item_names[0]}\n{item_names[1]}\n{item_names[2]}\n{item_names[3]}\n{item_names[4]}\n{item_names[5]}\n{item_names[6]}\n{item_names[7]}\n{item_names[8]}\n{item_names[9]}'''
        self.items = item1
        
        #pass


    def login_status(self):
        #for users in accounts:
        #print(accounts)
        User.userfile()
        User.passwordfile()
        #userlogin()
        print((self.user_username.text, self.user_password.text))
        for i in range(len(user_list)):
            print((user_list[i],password_list[i]))
            if self.user_username.text == user_list[i]:
                if self.user_password.text == password_list[i]:
                    print('true')
                    self.error_message = f'You have logged in successfully {self.user_username.text}!\n You can access the Menu'
                    self.count_enabled = True
                    username = str(self.user_username.text)
                    print(username)
                    #orders()
                    #self.user_username.text = ''
                    #self.user_password.text = ''
                    #userfile()
                    break
                break
        else:
            #userlogout()
            self.error_message = 'Please check your Username or Password\n and Try Again'
            self.count_enabled = False
            self.user_username.text = ''
            self.user_password.text = ''
            #userfile()
        User.userlogout()

    def logged_in(self):
        self.user_username.text = ''
        self.user_password.text = ''


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
                
                if int(self.user_age.text) >= 16 and int(self.user_age.text) <= 100: # and self.new_username.text != '' and self.new_password.text != '':
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
                    self.error_message_2 = 'You can Login!'

                elif int(self.user_age.text) < 16:
                    self.error_message_2 = 'You are under 16!'

                else:
                    self.error_message_2 = 'Your age is above boundary limit!'
        except:
            self.error_message_2 = 'Please type a number'






    def delievery(self):
        self.delievery_confirmed = False

    def return_status(self):
        print(self.user_username.text)
        self.count_enabled = False
        self.error_message = f''
        self.delievery_message = ''
        self.delievery_confirmed = False
        self.new_username.text = ''
        self.new_password.text = ''
        self.user_age.text = ''
        self.error_message_2 = ''
        self.item_message = ''
        self.item_name.text = ''
        self.quantity.text = ''
        user_orders.clear()
        total_price.clear()
        #self.count_enabled = False
        #self.user_username = ''
        #self.user_password = ''
        #user_username.text = ''
        #user_password.text = ''


       # if again == 'True':
        #    self.my_text = 'true'
        #else:
         #   self.my_text = 'false'

    def toggle_button_state(self, widget):
        print('toggle state' + widget.state)
       
        if widget.state == 'normal':
            widget.text = 'off'
            self.count_enabled = False
        else:
            widget.text = 'on'
            self.count_enabled = True

  
    def buttonclicked(self):
        print('First Name: ', self.user_username.text, 'Last Name: ', self.user_password.text)

        #Username.user_list() ---> appending users to list 
        if self.user_username.text == let:

            print('correct')      
        # activate the button 
        else:
            self.message.text = 'please check username'


        # cleans the text input 
        self.user_username.text = ''
        self.user_password.text = ''
        #self.message.text = ''

    # function that makes item list screen button active when condition is True

    def user_orders():
        # appends text input into list and appends to order files 
        pass


class MyApp(App):

    def build(self):
        return Display()

  
if __name__ == "__main__":
    MyApp().run()


