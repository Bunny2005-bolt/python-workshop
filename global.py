#1
score=0 #global score
def increase_score(points):
    global score
    score+=points

increase_score(10)
print("score :",score)

#2
def start_adventure():
    hero_name=input("Enter your name:")
    print(f"Welcome,{hero_name} you ambark on an apic adventure")

start_adventure()