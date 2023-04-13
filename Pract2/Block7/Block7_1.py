import re

with open('maze.txt', 'r', encoding="utf-8") as f:
    maze_data = f.read() + "\n"

rooms_data = re.findall(r"## \[(.*?)\]\(#(\d+)\)\n\n(.*?)\n\n((?:\* .*\[.{1,}?\]\(#.{1,}?\)\n)+)", maze_data)

rooms = []
for room in rooms_data:
    room_name = room[0]
    room_label = room[1]
    room_description = room[2]
    actions_data = re.findall(r'\* (.*?) \[(.*?)\]\(#(.{1,}?)\)\n', room[3])
    actions = [(action[0], action[1], action[2]) for action in actions_data]
    rooms.append((room_name, room_label, room_description, actions))

'''for i in rooms:
    print(i)'''
n = 0
# print(rooms[14][3])
while (True):
    print(rooms[n][0])
    print(rooms[n][2])
    ways = []
    s = ""
    l = 0
    str = rooms_data[n][3]
    for k in range(len(str) - 1):
        regex = "^[a-zа-яА-ЯёЁ]+$"
        pattern = re.compile(regex)
        if pattern.search(str[k]) is not None:
            s += str[k]
        if str[k + 1].istitle() == True:
            s += " "
            l += 1
        if str[k] == " ":
            s += " "
        if str[k].isdigit() and str[k + 1].isdigit():
            ways.append(str[k] + str[k + 1])
        elif str[k].isdigit() and not str[k + 1].isdigit() and not str[k - 1].isdigit():
            ways.append(str[k])
    print(s)
    # print(ways)
    find = []
    for i in range(1, len(s) - 2):
        if l > 1:
            if s[i] == " " and s[i + 1] == " " and s[i + 2].isupper() == True:
                find.append(i)
    # print(find)
    if len(find) > 0:
        print("1." + s[:find[0]:])
        if len(find) == 1:
            for i in range(len(find)):
                print(f'{i + 2}.{s[find[i]::]}')
        if len(find) > 1:
            for i in range(len(find) - 1):
                print(f'{i + 2}.{s[find[i]:find[i + 1]:]}')
                if i == len(find) - 2:
                    print(f'{i + 3}.{s[find[len(find) - 1]::]}')
    else:
        print("1." + s)
    if (n == 14) and int(input()) == 2:
        break
    n = int(input())
    n = (int(ways[n - 1])) - 1
