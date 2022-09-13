import random

def generate_response(user_input):
  responses = [
    "I think that's good",
    "Agreed",
    "That's wonderful",
    "Sorry to hear that",
    "Tell me more!",
    "Perfect",
    "cool",
    "Thats cool isn't it",
    "Most likely",
    "Wow, Awesome"
  ]
  return random.choice(responses)


def init_chat():
  quit_character = 'q'
  print("-Welcome to chatty kathy, you can tell me anything and everything here!-")
  print("")
  user_input = input("How are you today?\n")
  user_input1 = input("Whats your name?\n")
  user_input2 = input("Do you like dogs or cats?\n")
  user_input3 = input("How many family memebers do you have?\n")
  user_input4 = input("What sports do you play? (If none, type n/a)\n")
  user_input5 = input("Do you like to code?\n")
  user_input6 = input("What grade are you in?\n")
  

  print("Name - " + user_input1)
  print("Dogs or Cats - " + user_input2)
  print("Family members - " + user_input3)
  print("Sports - " + user_input4)
  print("Likes to code - " + user_input5)
  print("Grade - " + user_input6)


  user_input10 = input("Is this information correct?\n")
  

  if user_input10 == "yes":
    print("Perfect, you can continue to tell me more about yourself\n")
  else :
    print("Please refresh, and restart then.\n")
    
  user_input7 = input("I like your name, " + user_input1 + "\n")
  if user_input4 != "n/a":
    user_input8 = input("What position do you play in " + user_input4 + "\n")
  user_input9 = input("It'd be odd if you didnt :) \n")
  
  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")
if __name__ == "__main__":
  init_chat()