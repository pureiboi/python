import keyboard  # using module keyboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        # if keyboard.read_key():
        #     print(keyboard.read_key() + " is pressed ")
        # else:
        #     print("nothing presses")
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            print("nothing presses")
    except:
        break  # if user pressed a key other than the given key the loop will break
