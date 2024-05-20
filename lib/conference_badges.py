def badge_maker(name):
    result = f'Hello, my name is {name}.'
    return result

def batch_badge_creator(names):
    badge_names = []
    for name in names:
        badge_names.append(f'Hello, my name is {name}.')
    return badge_names

def assign_rooms(names):
    room_num = 1
    badge_names = []
    for name in names:
        badge_names.append(f'Hello, {name}! You\'ll be assigned to room {room_num}!')
        room_num += 1
    return badge_names

def printer(names):
    for name in batch_badge_creator(names):
        print(name)
    for name in assign_rooms(names):
        print(name)
