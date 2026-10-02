def make_call(prompt, temperature = 0.7):
    """ Return a formatted call in string...""" # defaut argument
    return f"[temp ={temperature}] {prompt}"
result = make_call("Summarise")
#print(result)


# count down from three




# n = 3 
# while n > 0:
#     print("launchig in ", n)
#     n -= 1
# print("Lift off!")



# n = 3
# while n > 0:
#     print("laumching in", n)
#     n -= 1
# print(" dafault value")




# -> 3..
# SAFE version with a counter that changes:
# attempts = 0
# while attempts < 3:
#     print("Connecting... attempts", attempts)
#     attempts += 1
# if you ever start an infinite loop in calab, press the stop button>)

 
# print number 1 to 5
# i = 1
# while i <= 5 :
#     print(" Print increase the number.... ->" ,i)
#     i = i + 1



# break : stop as soon as we find what we want...
# messages = ["Hi", "How are you", "quit", "This is ignored."]
# for m in messages:
#     if m == "quit":
#         print("User quit. Stopping")
#         break
#     print("Bot Heard..", m)


# Break : as soon as  we find what we want
# messages = ["Hi", "How are You", "quit", "this is ignored"]
# for m in messages:
#     if m == "quit":
#         print("User quit. Stopping")
#         break
#     print("Bot heard", m)
 


# messages = ["Hello", "", " ", "fees?", ""]
# for m in messages:
#     if m.strip() == "":
#         continue
#     print("processing:", m)


# script = ["Hi", "what are the fees", "quit"]
# for user in script:
#     if user.strip().lower() == "quite":
#         print("Bot: goodbye!")
#         break
#     print("Bot: you said -> ",user)


# continue : skip empty messages keep going
# messegas = ["Hello", "", "  ", "fees?", ""]
# for m in messegas:
#     if m.strip() == "":
#         continue        # skip blanks
#     print("processing",m)



# for x in ["a", "stop", "b"]:
#     if x == "stop":
#         break
#     print(x)




# Without protecting , this crashes the whole program
# age = int("twenty")
# with try/ except, we recover gracefully
# raw = "twenty"
# try:
#     age = int(raw)
#     print("Age is ", age)
# except ValueError:
#     print("That wasnt a number. please enter digits like 25")



# convert a batch of user-entered  number; skip the bad ones
# raw_values = ["100", "250", " oops", "500", "N/A", "200"]
# total = 0
# good = 0
# for raw in raw_values:
#     try:
#         total = total + int(raw)
#         good = good + 1
#     except ValueError:
#         print("Skipping bad values:", repr(raw))
# print(f"Summed {good} good values -> total {total}")






# n = 5 
# while n > 0:
#     print(n)
#     n -= 1

# n = 1
# while n < 10:
#     print(n)
#     n = n + 2

# i = 0 
# while i < 5:
#     i = i+ 1
#     if i == 3:
#         continue
#     if i == 5:
#         break
#     print(i)


