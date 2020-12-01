import keyboard

print("Press esc to escape")
previous = ''
while 1:
    name = keyboard.read_key()
    if name == previous:
        continue
    if name == 'esc':
        break
    print(name)
    previous = name