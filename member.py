all_users = []
next_id = 1

def add_new_user():
 global next_id
 name=input("Enter your name: ")
 email = input("Enter E-mail ID: ")
 phone = input("Enter phone no.: ")

 

 valid=True
 if len(phone) == 0:
    valid=False
 for character in phone:
    if character not in "0123456789":
        valid = False

 if not valid:
    print("Invalid phone number.")
    return 

 phone_num = int(phone)
 
 
 user_data = {}
 user_data["id"] = next_id
 user_data["name"] = name
 user_data["email"]=email
 user_data["phone"] = phone_num

 all_users.append(user_data)
 print("Assigned member ID:", next_id)
 
 
 next_id = next_id + 1

def find_by_id(search_id):
 for index in range(len(all_users)):
    current_person = all_users[index]
    if current_person["id"] == search_id:
        return current_person
 return None


def find_by_name(search_name):
 for user in all_users:
    
    if user["name"].lower() == search_name.lower():
        return user
        
 return None
