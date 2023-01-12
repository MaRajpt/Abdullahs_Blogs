from concurrent.futures import thread
import threading

def print_one():
    for i in range(2):
        print(1)
        
def print_two():
    print(2)
    
if__name__=="__main__"
t1 = thread.thread(target=print_one)
t2 = thread.thread(target=print_two)
    