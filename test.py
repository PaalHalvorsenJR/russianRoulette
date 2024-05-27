import random 

def russian_rullet():
    gun = 5 # 5 chambers
    bullets_left = 5
    random_number = random.randint(0, 4)
    for i in range(gun):
        if random_number == i:
            result = "You are dead!"
            bullets_left -= 1
            print(f"Bullets left: {bullets_left}")
        else:
            result = False
    return result


print(russian_rullet())