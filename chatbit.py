user_query = {"greeting" : ["hi","hello","hey"],
              "bit" : ["tell me something about bit"],
              "braches" : ["cs","ece"]
              }


bot_reply = {"greeting": ["hello","hey","hi"],
        "tell me about bit": ["birla institute of technology","mesra"],
        "tell me about branches in bit" : ["cs/ece"],
        "default" : ["sorry i did'nt understand"]
        }

import random
import time


def intent_match(user_msg):
  for intent, entity in user_query.items():
    if (user_msg.lower() in entity):
       return intent
  return "default"

def respond(user_msg):
   intent = intent_match(user_msg)
   return random.choice( bot_reply [intent])
   

bot_msg = " "
user_msg = " "

while (1):
  user_msg = input("user : ")
  if(user_msg == "get out"):
      print("bot : bye. nice to talk")
      break
  bot_msg = respond(user_msg)
  time.sleep(0)
  print("bot : {}".format(bot_msg))        