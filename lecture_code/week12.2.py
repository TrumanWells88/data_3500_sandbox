# handling exceptions

try:
    2/0
except:
    print("You can't divide by 0")

try:
    with open("Python.py", "r") as file:
        print(file.readlines)
except:
    print("That file doesn't exist")



# creating a json
import json

person = {}

person["full_name"] = "Jonas Lockhart"
person["car"] = "Ford Focus"
person["grade"] = "So"
person["classes"] = ["DATA3500", "DATA3300", "DATA3330", "DATA3400", "BUS1700"] 

json.dump(person, open("/workspaces/data_3500_sandbox/lecture_code/jonas.json", "w"), indent=2)


# load a json file

jonas = json.load(open("/workspaces/data_3500_sandbox/lecture_code/jonas.json"))

print(jonas["full_name"])

try: 
    jonas["classes"].append("PE1750")
    print(jonas["classes"])
except:
    print("")

for class_ in jonas["classes"]:
    print(class_)



# json url

import json
import requests

url = "https://v2.jokeapi.dev/joke/Programming"

request = requests.get(url)
joke_dict = json.loads(request.text)

print(joke_dict)

print(joke_dict)

input("press enter to hear the punchline")
print(joke_dict["delivery"])

try:
    print(joke_dict["setup"])
    input("press enter to hear the punchline")
    print(joke_dict["delivery"])
except:
    print(joke_dict["joke"])