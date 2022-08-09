"""Create a text file containing current visitors at a hotel. We'll call it, guests.txt. The file will automatically populate with each initial guest's first name on its own line."""

guest = open('guest.txt', 'w')
initial_guest = ['Bob', 'Maria', 'José', 'Margarita']
for i in initial_guest:
    guest.write(i + '\n')
guest.close()

# check the contents of the newly created guests.txt file.
with open('guest.txt') as guest:
    for line in guest:
        print(line)
        
# update our file as guests check in.
new_guest = ['Oscar', 'Ana', 'Andrés']
with open('guest.txt', 'a') as guest:
    for i in new_guest:
        guest.write(i + '\n')


# check whether your code correctly added the new guests to the guests.txt file.
with open('guest.txt') as guest:
    for line in guest:
        print(line)
        
#remove the guests that have checked out already
checked_out = ['Ana', 'Oscar', 'Margarita']
temp_list = []
with open('guest.txt') as guest:
    for g in guest:
        temp_list.append(g.strip())
with open('guest.txt','w') as guest:
    for name in temp_list:
        if name not in checked_out:
            guest.write(name + '\n')
            
# check whether your code correctly removed 
with open('guest.txt') as guest:
    for line in guest:
        print(line)
        
# check whether Bob, María and Jose are still checked 
guest_to_check = ['Jose','Maria', 'Bob']
checked_in = []
with open('guest.txt') as guest:
    for g in guest:
        checked_in.append(g.strip())
    for check in guest_to_check:
        if check in checked_in:
            print(f'{check} is checked in.')
        else:
            print(f'{check} is not checked in')