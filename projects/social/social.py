import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.add_friend_counter = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

        self.add_friend_counter += 1

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
	        self.add_user(f"User {i}")

        # Create friendships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        order = Queue()
        order.enqueue([user_id])

        while order.size() > 0:
            path = order.dequeue()
            last_user = path[-1]

            if last_user not in visited:
                visited[last_user] = path

                for i in self.friendships[last_user]:
                    if i not in visited:
                        new_path = path.copy()
                        new_path.append(i)
                        order.enqueue(new_path)
    
        return visited

    def average_degree(self):

        final_average = []

        for i in self.users:
            visited = self.get_all_social_paths(i)

            for j in visited:
                average = []
                average.append(len(visited[j]))

                average_degree = sum(average) / len(average)

                final_average.append(average_degree)
        
        return sum(final_average) / len(final_average)

    def percent_network(self):

        total_connections = 0

        for i in self.users:
            visited = self.get_all_social_paths(i)

            total = 0
            for user_id in visited:
                total += len(visited[user_id]) - 1
            total_connections += len(visited)

        network = total_connections / len(self.users)
        return network / len(self.users)


if __name__ == '__main__':
    print('\n+++++++++++++++++++++++++++++++++Part 1+++++++++++++++++++++++++++++++++\n')

    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    print('\n+++++++++++++++++++++++++++++++++Part 2+++++++++++++++++++++++++++++++++\n')
    # Answer 1
    answer1 = SocialGraph()
    answer1.populate_graph(100, 10)
    answerQ1 = f'''For a network of 100 users with an average of 10 friends each,
                 I would need to call add_friend() {answer1.add_friend_counter} times.
                 This is because the number of users,
                 times the average number of friends,
                 floored by 2, is consistent.'''

    for line in answerQ1.splitlines():
        print(line.strip())

    # Answer 2
    answer2 = SocialGraph()
    answer2.populate_graph(1000, 5)
    
    answerQ2 = f'''\nFor a network of 1000 users with an average of 5 freinds each,
                  the average degrees of seperation would be {answer2.average_degree(): .2f},
                  the percentage of the total network that person is connected to is {answer2.percent_network(): .2%}.'''
    for line in answerQ2.splitlines():
        print(line.strip())




