import random

# random_Int = random.randint(1, 6)
#
# print(random_Int)
#
# random_float = random.random()# 0.0 <= random_float < 1.0
# print(random_float)
#
# random_float1 = random.random() * 100 # 0.0 <= random_float < 100.0
# print(random_float1)
#
# random_float2 = random.uniform(1, 100) # 1.0 <= random_float < 100.0
# print(random_float2)

random_num = random.randint(0, 1)
if random_num == 0:
    print("Heads")
else:
    print("Tails")
