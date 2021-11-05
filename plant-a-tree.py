import requests, random

string = ""
# generates random string
for i in range(10):
    character = chr(random.randint(48, 90))
    string += character
request = requests.get(f"https://www.ecosia.org/search?q={string}")
if request.status_code == 200:
    print(f"Went well. Search: {string}")
else:
    print(f"""Something went wrong. Search: {string} Status code: 
    {request.status_code}""")