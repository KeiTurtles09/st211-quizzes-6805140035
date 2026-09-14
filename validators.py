import re

def validateEmail(email):
   pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   if not re.match(pattern, email):
       raise ValueError(f"Invalid email: {email}")
   else:
       return True

def validateAge(age):
   if not isinstance(age, int) or age < 0 or age > 120:
       raise ValueError(f"Invalid age: {age}")
   else:
       return True