# refactore it & keep it DRY
Appetizers = ["wings",'cookies'," spring rolls"]
Entrees = ['salmon','steak','meat tornado','a literal garden']
Desserts = ['ice cream','cake','pie']
Drinks = ['coffee','tea','unicorn tears']
def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

def user_insertion():
    user_input=input(">")  
    return user_input        

def end_application():
    print("thanks for using snakes cafe application !")



def main():
    a=''
    i=0
    l = []
    intro()
    user_input = user_insertion()
    while(user_input.lower() != "quit"):
        
        
        if user_input.lower() in Appetizers or user_input.lower() in Entrees or user_input.lower() in Desserts or user_input.lower() in Drinks:
                l.append(user_input.lower())
                for x in l :
                 if user_input.lower() == x :
                  i +=1
                print('**',i,'order of',user_input,'has been added to your meal **')
                #TODO: handle the order numbers
                i=0
        else:
                print("sorry we dont have this item !\b")
        print('Your items list is: ',l,'\b')        
        user_input = user_insertion()    
 
    print('Your items list is: ',l,'\b')  
    l=[]
    end_application()



main()