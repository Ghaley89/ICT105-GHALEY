def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("Dorji", " O\"Pema")
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''): 
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("Dorji", "Pema", "Tenzin")
print(musician) 

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person("Dorji", "Pema", age=30)
print(musician) 

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg) 
        
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#today 
    
    
