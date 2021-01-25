from multiprocessing import Manager

def execute_queue():
    colors = ['red', 'green', 'white', 'blue', 'orange']

    que_obj = Manager().Queue()

    for x in colors:
        print("Adding: {x} - color".format(x=x))
        que_obj.put(x)

    while not que_obj.empty():
        print("Getting: {x} - color".format(x=que_obj.get()))


if __name__ == '__main__':
    execute_queue()