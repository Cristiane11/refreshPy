# import re
# text = "Contact us at support@example.com or sales@example.com"
# emails= re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
# print(emails)

import re
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]
# Write your code below to validate the emails using re.search()

for email in emails:
    # Implement regex search here
    if  re.search(r"^[\w\.-]+@[\w\.-]+\.[a-z]{2,3}$", email):  # Update condition with regex search
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")