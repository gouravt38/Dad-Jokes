from termcolor import colored
from pyfiglet import figlet_format
from random import choice
import colorama
import requests
colorama.init()
txt = "DAD JOKE BY GOURAV"
text= figlet_format(txt)
print(colored(text,color="green"))

topic = input("Let me tell you a joke! Give me a topic : ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(url,
	headers={"Accept": "application/json"},
	params={"term": topic}
	)
data = response.json()
count=data["total_jokes"]

if count > 1 :
	print(f"I have got {count} jokes about {topic}. Here's one: ")
	print(choice(data["results"])["joke"])
elif count == 1:
	print(f"I have got {count} jokes about {topic}. Here's one: ")
	print(data["results"][0]['joke'])
else:
	print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
