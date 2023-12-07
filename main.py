from os import getenv
env = getenv("ENVIRONMENT")
action = getenv("ACTION")
offof = "wwewee"



if env == "dev" or action == "stop":
                  print("good")