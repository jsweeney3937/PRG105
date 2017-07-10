# information Class
class Information:
    # init method
    def __init__(self, name, address, age, phone):
        # name attribute
        self.__name = name
        # address attribute
        self.__address = address
        # age attribute
        self.__age = age
        # phone attribute
        self.__phone = phone

    # mutator sets name to __name
    def set_name(self, name):
        self.__name = name

    # mutator sets address to __address
    def set_address(self, address):
        self.__address = address

    # mutator sets age to __age
    def set_age(self, age):
        self.__age = age

    # mutator sets phone to __phone
    def set_phone(self, phone):
        self.__phone = phone

    # accessor returns name
    def get_name(self):
        return self.__name

    # accessor returns address
    def get_address(self):
        return self.__address

    # accessor returns age
    def get_age(self):
        return self.__age

    # accessor returns phone
    def get_phone(self):
        return self.__phone

# creates instance my_info to Information class with name, address, age, and phone passed as arguments
my_info = Information("John Sweeney", "897 Green Rd.", "31", "593-309-5903")
# prints name, address, age, and phone number stored in my_info
print("Here is the information entered about yourself. ")
print("Name:", my_info.get_name())
print("Address:", my_info.get_address())
print("Age:", my_info.get_age())
print("Phone:", my_info.get_phone())

# creates instance my_info_friend to Information class with name, address, age, and phone passed as arguments
my_info_friend = Information("Josh Becker", "490 Amherst Dr.", "30", "864-300-2119")
# prints name, address, age, and phone number stored in my_info
print("Here is the information entered about your friend. ")
print("Name:", my_info_friend.get_name())
print("Address:", my_info_friend.get_address())
print("Age:", my_info_friend.get_age())
print("Phone:", my_info_friend.get_phone())

# creates instance my_info_family to Information class with name, address, age, and phone passed as arguments
my_info_family = Information("Sean Sweeney", "89 Willow Ct.", "29", "096-393-2194")
# prints name, address, age, and phone number stored in my_info
print("Here is the information entered about your family member. ")
print("Name:", my_info_family.get_name())
print("Address:", my_info_family.get_address())
print("Age:", my_info_family.get_age())
print("Phone:", my_info_family.get_phone())
