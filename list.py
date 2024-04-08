# 3-1
list=["Anvit", "Parth", "Lucky"]
print(list[0])
print(list[1])
print(list[2])

# 3-2
list=["Anvit", "Parth", "Lucky"]
print(f"Hey {list[0]}, how are you")
print(f"Hey {list[1]}, how are you")
print(f"Hey {list[2]}, how are you")

# 3-3
list=["Porsche", "BMW", "Audi"]
print(f"I would like to own a {list[0]}")


list=["bugati", "porsche", "honda"]
list[2]="maruti"
print(list)

list=["bugati", "porsche", "honda"]
list.append("maruti")
print(list)

list=["bugati", "porsche", "honda"]
list.insert(0,"audi")
print(list)

list=["bugati", "porsche", "honda"]
del list[2]
print(list)

list=["bugati", "porsche", "honda"]
list.pop()
print(list)

list=["bugati", "porsche", "honda"]
list.pop(0)
print(list)

list=["bugati", "porsche", "honda"]
list.remove("honda")
print(list)

# 3-4
guest_list=["anvit", "parth", "lucky"]
print(f"I would like {guest_list[2]} to invite to dinner")
print(f"I would like {guest_list[1]} to invite to dinner")
print(f"I would like {guest_list[0]} to invite to dinner")

# 3-5
guest_list=["anvit", "parth", "lucky"]
print(f"I would like {guest_list[2]} to invite to dinner")
print(f"I would like {guest_list[1]} to invite to dinner")
print(f"I would like {guest_list[0]} to invite to dinner")
print(f"{guest_list[0]} cant come to dinner")
guest_list[0]="Sohin"
print(f"I would like {guest_list[0]} to invite to dinner")
print(guest_list)

# 3-6
guest_list=["anvit", "parth", "lucky"]
guest_list.insert(0,"sukrant")
guest_list.insert(2,"valia")
guest_list.append("kartik")
print(guest_list)

# 3-7
guest_list=['sukrant', 'anvit', 'valia', 'parth', 'lucky', 'kartik']
print(f"{guest_list[5]} sorry i can't invite ypu to dinner")
guest_list.pop()
print(f"{guest_list[4]} sorry i can't invite ypu to dinner")
guest_list.pop()
print(f"{guest_list[3]} sorry i can't invite ypu to dinner")
guest_list.pop()
print(f"{guest_list[2]} sorry i can't invite ypu to dinner")
guest_list.pop()
print(f"{guest_list[1]} you are still invited")
print(f"{guest_list[0]} you are still invited")
del guest_list[1]
del guest_list[0]
print(guest_list)

car=["audi", "bmw", "toyota", "safari"]
car.sort()
print(car)

car=["audi", "bmw", "toyota", "safari"]
car.sort(reverse=True)
print(car)

car=["audi", "bmw", "toyota", "safari"]
car.reverse()
print(car)

car=["audi", "bmw", "toyota", "safari"]
print(len(car))

