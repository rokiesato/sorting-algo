# Name: Edriann Nazareth
# Date: 1/7/2024

class Client:
    def __init__(self, client_id=0, first_name="Unkonwn", last_name="Unknown", phone="Unknown", email="Unknown"):
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email
            
            
    # classes that compare objects must inplement __eq__method and __lt__method
    # __lt__ means "less than" and it must return a boolean
    # __eq__ means "equals" and it must return a boolean
    def __lt__(self, other):
        return self.__client_id < other.__client_id 
       
    def __eq__(self, other):
        return self.__client_id < other.__client_id     
       
    #__str() method is automatically called when you print the object
    def __str__(self):
        return str(self.__client_id) + ", " + self.__last_name + ", " + self.__first_name
        
    # getters and setters
    def get_client_id(self):
        return self.__client_id
        
    def set_client_id(self, client_id):
        self.__client_id = client_id
            
    def get_first_name(self):
        return self.__first_name
        
    def set_first_name(self, first_name):
        self.__first_name = first_name
            
    def get_last_name(self):
        return self.__last_name
        
    def set_last_name(self, last_name):
        self.__last_name = last_name
            
    def get_phone(self):
        return self.__phone
           
    def set_phone(self, phone):
        self.__phone = phone
            
    def get_email(self):
        return self.__email
           
    def set_email(self, email):
        self.__email = email
        

