'''
ASSIGNMENT 2 - Wednesday, September 11th
1. Create an empty list called “friends”. Create a function that adds a friend to the friends list and
    a function that removes a friend from the friends list. Both of the functions should take one parameter
    which is the name of the person that will be added or removed.

2. Use the functions you created in step 1 to add 5 people to your friends list using your function.
    Then remove two friends from your list using your remove function. If the friend is not in the list,
    print a message that says the friend is not in the list and can’t be removed. Finally, print out your final 
    friend list.
'''
#Create an empty list called "friends".
friends = []

#Create a function that adds a friend to the friends list.
def add_friend(add_name):
    friends.append(add_name)

#a function that removes a friend from the friends list.
def remove_friend(remove_name):
    if remove_name in friends:
        friends.remove(remove_name)
    else:
        print("Not in friends list")

j = 1
while(j<=5):
    name = input(f"What's your friend's name {j}")
    add_friend(name)
    j = j+1

print(friends)

k = 1
while(k<=2):
    name = input ("what friend you want to remove from the list?")
    remove_friend(name)
    k = k+1

print(f"Your friends list is... {friends}")
