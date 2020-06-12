from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from collections import deque

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


"""'''visited = {}

previous_room = 0

def moving():
    global previous_room
    direction = {}
    current_room = player.current_room.id
    for i in player.current_room.get_exits():
        direction[i] = '?'
        visited[player.current_room.id] = direction

    print(current_room, previous_room)
    previous_room = current_room'''

my_graph = dict(room_graph)

for k, v in my_graph.items():
    del v[0]
    

def search(start_point):
    search_queue = []
    search_queue.append([i for i in my_graph[start_point][0]])
    print(search_queue)
    searched = []
    while len(searched) != 500:
        room = search_queue.pop()
        if not room in searched:
            search_queue.append(my_graph[room][0])
            searched.append(room)

    return searched

my_list = search(player.current_room.id)"""

def bfs(start):
    traversal_path = []
    opposites = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    order = Stack()

    visited = {}
    order.push((start, None))

    while order.size() > 0:
        current = order.stack[-1]
        room = current[0]
        direction_taken = current[1]

        if room.id not in visited:
            visited[room.id] = set()

        if direction_taken:
            visited[room.id].add(direction_taken)
        
        unexplored = [] 

        for i in room.get_exits():
            if i not in visited[room.id]:
                unexplored.append(i)

        if len(unexplored_paths) > 0:
            direction = random.choice(unexplored_paths)
            visited[room.id].add(direction)
            order.push((room.get_room_in_direction(direction), opposites[direction]))
            traversal_path.append(direction)
        else:
            traversal_path.append(direction_taken)
            order.pop()

    return traversal_path

traversal_path = bfs(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
# 
#     moving()
#     for k, v in visited.items():
#         print(k, v)