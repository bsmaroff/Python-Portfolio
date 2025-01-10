print ("Answer the questions to see your dream vacation spot!")
print ("Answer with the phrase in the parantheses")
ans = input("Blue(B) or Red(R)")
if ans=="B":
    ans = input("Waffles(W) or Pancakes(P)")
    if ans == "W":
        ans = input("Beaches(B) or Mountains(M)")
        if ans == "B":
            print("You should visit Miami!")
        else:
            print("You should visit Denver!")
    if ans == "P":
        ans = input("Rainy(Rain) or Sunny(Sun)")
        if ans == "Rain":
            print("You should visit Seattle!")
        else:
            print("You should visit Dallas!")
if ans=="R":
    ans = input("Sausage(S) or Bacon(B)")
    if ans == "S":
        ans = input("West(W) or East(E)")
        if ans == "W":
            print("You should visit Los Angeles!")
        else:
            print("You should visit New York City!")
    if ans == "B":
        ans = input("Hot(H) or Cold(C)")
        if ans == "H":
            print("You should visit Phoenix!")
        else:
            print("You should visit Toronto!")
