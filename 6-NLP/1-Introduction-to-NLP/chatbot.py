import random

responses = ["That is quite interesting, please tell me more.",
             "I see. Do go on.",
             "Why do you say that?",
             "Funny weather we've been having, isn't it?",
             "Let's change the subject.",
             "Did you catch the game last night?"]

print("Hello, I am Eliza, the chatbot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today?")

while True:
    choice = input()
    if choice == 'bye':
        break
    print(random.choice(responses))

print("Bye, It was nice talking to you!")