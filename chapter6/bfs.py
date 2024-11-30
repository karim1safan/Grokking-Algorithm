from collections import deque

graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# This function checks whether the person’s name ends with the letter m
# If it does, they’re a mango seller.
def person_is_seller(name):
  return name[-1] == 'm'

def bfs(name):
  # create new empty queue
  search_queue = deque()

  # first degree connection [Adds all of your neighbors to the search queue]
  search_queue += graph[name]

  # keep track of which people you’ve searched before
  searched = []

  # while the queue isn't empty
  while search_queue: 
    # grabs the first person off the queue
    person = search_queue.popleft()

    if not person in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        # Add all of this person's friends to search queue
        search_queue += graph[person]

        # Marks this person as searched
        searched.append(person)
  return False


bfs('you')


# running time: O(no. people + no. edge) => O(V + E)
# V -> no. vertices
# E -> no. edges