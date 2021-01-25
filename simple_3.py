from multiprocessing import Queue, Lock, Process, current_process
import queue, time

''' 
    where we are adding tasks to the queue, then creating processes and starting them, then using join() to complete the processes. Finally we are printing the log from the second queue
'''

def doJob(task_to_complete_queue, task_done_queue):
    while True:
        try:
            task = task_to_complete_queue.get_nowait()
        except queue.Empty:
            break
        else:
            print(task)
            task_done_queue.put(task + " done by " + current_process().name)
            time.sleep(.5)
    return True



def main():
    number_of_task = 20
    number_of_proc = 5
    process_l = []
    task_to_complete_queue = Queue()
    task_done_queue = Queue()

    for task in range(1, number_of_task):
        task_to_complete_queue.put("Task - " + str(task))

    for procs in range(1, number_of_proc):
        prx = Process(target=doJob, args=(task_to_complete_queue, task_done_queue))
        process_l.append(prx)
        prx.start()

    for pross in process_l:
        pross.join()

    while not task_done_queue.empty():
        print(task_done_queue.get())



if __name__ == '__main__':
    main()