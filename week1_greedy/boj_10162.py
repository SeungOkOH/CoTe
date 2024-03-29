# import psutil
# 
# 
# def memory_usage():
#   process = psutil.Process()
#   memory_info = process.memory_info()
#   return memory_info.rss / 1024 / 1024
# 
# 
# initial_memory = memory_usage()

t = int(input())
button_list = [300, 60, 10]
answer = []

if t % 10 == 0:
  for button in button_list:
    count = t // button
    t %= button
    answer.append(count)
  print(answer[0], answer[1], answer[2])
else:
  print(-1)

# final_memory = memory_usage()
# memory_used = final_memory - initial_memory
# print(f"Memory used: {memory_used} MB")