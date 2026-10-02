# def route(msg):
#     msg = msg.strip().lower()
#     if"hi" in msg or "hello" in msg:
#         #print("greeting")
#         return "Greeting"
#     elif "fee" in msg or "cost" in msg or "price" in msg:
#         #print("fees")
#         return "fees"
#     elif "time" in msg or "when"in msg:
#         return "timing"
#     else:
#         return "unknown...."
# #for m in ["Hello!","how much are fees ?","when do we start","how much i play"]:
# #     print(f"{m:30s}  -> {route(m)}")       


# # 3.1. =>
# # temp = float(input("Please Enter the tempracture.."))
# # if temp >0.7:
# #     print("Creative...")
# # elif temp > 0.3:
# #     print("Balanced....")
# # else:
# #     print("Presice")


# # 3.2 => 
# msg = ["hi there", "how much are the fees", "when do classes start", "thanks?"]
# # print(msg)
# # print("number of meggege....", len(msg))


# # 3.3 => 
# config = ["cloude", 8000, 0.7, True]
# #print(config)


# # 3.4 =>
# #List = ["hi there", "how much are the fees", "when do classes start", "thanks?"]
# #
# # print(List[0])
# # print(List(1))
# # print(List[-1])


# # 3.5 => 
# # messages = "Hello!"
# # print(messages)



# #3.6 =>
# models = ["gpt", "claude", "gemini", "llama"]
# # print(models[0])
# # print(models[-1])
# # print(len(models))  # print total words...

# # 3.7 =>
# nums = [10, 20, 30, 40, 50]
# #print(nums[1:3])  # number 1 and three digit
# # print(nums[:2])
# # print(nums[2:])
# # print(nums[-2])


# # Adding Removing in List

# List = ["msg1", "msg2"]
# #print(List)
# # List.append("msg3") // Add to end
# # print(List)
# # List.remove("msg1")# Remove by value..
# # print(List)
# # last = List.pop() #remove Return the last 

# # print(List)


# # 3.8 =>
# # intents = ["greeting", "fees"]
# # intents.append("timing")
# # print(intents)
# # print(intents[2])


# # 3.9 =>
# # nums = [10, 20, 30, 40, 50]
# # print(nums[1:4])
# # print(nums[:2])
# # print(nums[2:])


# #3.10 => Start with queue = ["msg1", "msg2"]. Append "msg3", remove "msg1", then print the final list.
# queue = ["msg1", "msg2"]
# queue.append("msg3")
# queue.remove("msg1")
# #print(queue)

# # 3.11 => Loop over models = ["gpt", "claude", "gemini"] and print Loading <model>... for each.
# models = ["gpt", "claude", "gemini"]
# for model in models:
#  # print(f"loading {model} ........")



# # 3.12 => Use range to print Retry 1, Retry 2, Retry 3.
#  #for i in range(1,4):
#     #print(f"retry {i}")


# # 3.14 => Print a numbered menu of intents = ["greeting", "fees", "timing"] as 1. greeting, etc.
# # intents = ["greeting", "fees", "timing"]
# # for i,intent in enumerate(intents, start=1):
# #     print(f"{i}. {intent}")


# # 3.15 => Given scores = [85, 40, 92, 55, 30, 78], count how many are passing (>= 50). Print the count.
# # scores = [85, 40, 92, 55, 30, 78]
# # count = 0
# # for score in scores:
# #   if score >= 50:
# #     count += 1
# # print(count)


# 3.16 =>Given latencies = [120, 340, 90, 500, 250] (ms), compute the total and the average using a loop.
latencies = [120, 340, 90, 500, 250]
total = 0
for num in latencies:
  total += num
avarage = total/num
print("total:", total,"ms")
print("Avarage", avarage, "ms")

# 3.27 =>