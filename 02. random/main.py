import random

print("Random seed ", random.random())

print("Random int ", random.randint(3, 9))

x = random.randrange(1, 10, 4)
print("random range", x)  # randrange batter then Random with 3rd argument

x = [2, 7, 4, 6]
random.shuffle(x)
print(x)

x = ["apple", "banana", "kiwi", "papaya"]
print("random choice from list", random.choice(x))
print("random choices from list", random.choices(x, weights=[1, 1, 1, 10], k=2))
# weights= elements picking provability

