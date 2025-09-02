# Creating a dictionary of users, where each user has their own dictionary of details
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

# In this example, each user has a dictionary containing their 'name', 'age',
# and an 'address' dictionary with more details like street, city, and zipcode.

# Accessing the city of user1 by first accessing 'user1', then 'address', and then 'city'
city_user1 = users['user1']['address']['city']
print(city_user1)  # Output: New York

# Updating the zipcode of user2 from '94107' to '94109'
users['user2']['address']['zipcode'] = '94109'
print(users['user2']['address']['zipcode'])  # Output: 94109

# Adding a new key 'phone' to user1 with the value '555-1234'
users['user1']['phone'] = '555-1234'
print(users['user1']['phone'])  # Output: 555-1234

# Looping through the outer dictionary 'users'
for user, info in users.items():
    print(f"User ID: {user}")
    
    # Looping through the inner dictionary for each user
    for key, value in info.items():
        print(f"  {key}: {value}")
        
# Expected Output:
# User ID: user1
#   name: Alice
#   age: 25
#   address: {'street': '123 Main St', 'city': 'New York', 'zipcode': '10001'}
#   phone: 555-1234
# User ID: user2
#   name: Bob
#   age: 30
#   address: {'street': '456 Elm St', 'city': 'San Francisco', 'zipcode': '94109'}