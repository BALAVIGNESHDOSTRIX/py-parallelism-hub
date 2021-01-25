from multiprocessing import Pool
import time 

work_tuple = (["A", 2], ["B", 4], ["C", 3])

def work_job(work_l):
    print("work %s waiting %s seconds" % (work_l[0], work_l[1]))
    time.sleep(work_l[1])
    print("work %s Finished" % (work_l[0]))

def main():
    p = Pool(2)
    p.map(work_job, work_tuple)

if __name__ == '__main__':
    main()