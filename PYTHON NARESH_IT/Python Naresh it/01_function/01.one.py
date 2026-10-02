#1.
# config = {"model":"claude"}
# #print(config["model"])
# #print(config.get("temmperature", 0.7))
# counts ={}
# for i in {"fees", "fees", "timing"}:
#     counts[i] = counts.get(i, 0)+1
#     print(counts)





#print(len(set(["a", "a", "b"])))




# define one call meny times
# def greet(name):
#     print(f"hello {name} ! welcome to Ai launched")
# greet("Satyam")

# # call many times
# greet("Rekha")
# greet("Seema")



# def boot(model):
#     print(f"booting {model} model")
# boot("GPT")
# boot("claude")



# Return => 
# def add_buffer(token):
#     return token + 5000
# safe = add_buffer(2000)
# print("safe limits", safe)
# print("Double", safe*2)

# Compare with Prints
# def add_buffer_add(token):
#     print(token + 200)
# x = add_buffer_add(1000)
#  print(x)


# def clean(text):
#     return text.strip().lower()
# msg = clean("fees??")
# print(repr(msg))
# print("fees" in msg)

# def squre(n):
#     return n*n
# result = squre(6)
# print(result)
# print(squre(5), squre(10))




# def make_call(prompt, model="claude", temperature = 0.7):
#     return f"[{model} @ temp = {temperature}] {prompt} "
# # use all defaults
# print(make_call("Summarise this report..."))

# #Override some
# print(make_call("Write a poem", temperature=0.1))

# #override by name
# print(make_call("Exact Data", model="gpt", temperature=0.0))


# def build_config(model="claude", max_tokens=4096, temperature = 0.7):
#     return{"model":model, "max_tokens" : max_tokens,"temperature":temperature}
# cfg = build_config() #(temperature=0.2)
# #print(cfg)
# #print("Model",cfg["model"])
# print(cfg)





# def build_prompt(role, task, constraint="be concise"):
#     """
#     Assemble an engineered prompt from three parts.
#     args:
#          role: who the Ai should act as (str)
#          task: what the Ai should do (str)
#          constraint: an optional style/formate rule (str)
#     Returns:
#             A single formatted prompt string.
#     """
#     return f" you are a {role}. plese {task}, {constraint}"
# print(build_prompt("Data Scientist", "explain overfitting"))
# help(build_prompt)




# def word_count(text):
#     """ Return the word number of this text..."""
#     return len(text.split())
# sample_text = "Hello world this is a sample sentence here...."
# print(word_count(sample_text))


# def build_prompt(role, task, constraint="be concise and clear"):
#     """Return an engineering prompt strint from role + task + constraint"""
#     return f"you are a {role}. please {task}, constraint."
# prompts = [
#     build_prompt("Docter",)
#     build_prompt("financial",)
#     build_prompt("Python tutoreal",)
# ]
# for i, p in enumerate(prompts, start=1):
#     print(f"{i}, {p}")



# INVENTORY = {"green tea": 12, "black cofeee" : 0, "masala chai" :5}
# def check_inventory(items):
#     """Return how many units of `item` are in stock(0 if unknown). """
#     return INVENTORY.get(items, 0)
# def place_order(item, qty=1):
#     """Attempt to order `qty` of  `item`. 
#     return status dict: {'ok': bool, 'message' : str}"""
#     stock = check_inventory(item)
#     if stock >= qty:
#         INVENTORY[item] = stock - qty
#         return {"okey" : True, "mesage": f"Ordered {qty} x {item}. remaining: {INVENTORY[item]}"}
#     else:
#         return{"okey" : False, "message": f"sorry, only {stock} x {item} in stock."}
# print(check_inventory("green tea"))
# print(place_order("green tea", 3))
# print(place_order("black_cofee"), 1)
# print(place_order("masala chai"), 2)