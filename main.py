import os

os.system("clear")
color = input("Enter HEX code of color to check without the #: ")
os.system(f"curl https://api.color.pizza/v1/{color} -s | jq > color.json")