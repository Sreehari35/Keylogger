from pynput.mouse import Listener

def mouseposition(x,y):
    print("Mouse position=({0},{1})".format(x,y))

with Listener(on_move=mouseposition) as m:
    m.join()