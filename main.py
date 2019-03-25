import requests
json_data = requests.get("https://randomuser.me/api/?format=json&results=5&inc=gender,name,location,phone%27").json()

class User:
    def __init__(self,first_name,last_name,gender,age,phone):
        self.name = first_name
        self.name += ' '
        self.name += last_name
        self.phone = phone
        self.gender = gender
        self.age = age

    def __str__(self):
        return  '\n%s\n%s\n%s\n%s\n'%(self.name,self.gender,self.age,self.phone)

class UsersList:
    def __init__(self,users):
        self.users=users
    def get_user(self,index):
        return self.users[index]


list = []


for i in range (0,9):
    json_first_name = json_data['results'][i]['name']['first']
    json_last_name = json_data['results'][i]['name']['last']
    json_age = json_data['results'][i]['dob']['age']
    json_gender = json_data['results'][i]['gender']
    json_phone = json_data['results'][i]['phone']
    current_person = User(json_first_name,json_last_name,json_gender,json_age,json_phone)
    list.append(current_person)

mainObject = UsersList(list)






