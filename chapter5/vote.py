voted = {}

def check_voter(name):
  if voted.get(name):
    print("Kick them out!")
  else:
    voted[name] = True
    print("Let them vote!")

print(check_voter('tom'))
print(check_voter('mike'))
print(check_voter('mike'))
