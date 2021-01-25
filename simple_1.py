from multiprocessing import Process

def get_continent_name(contin='Asia'):
    print("Continent Name: ", contin)


def create_parllalism():
    process_l = []
    proc = Process(target=get_continent_name)
    process_l.append(proc)
    proc.start()

    # with argument
    cont_l = ['Australia', 'Africa', 'America', 'Artic']
    for x in cont_l:
        prox = Process(target=get_continent_name, args=(x,))
        process_l.append(prox)
        prox.start()

    for y in process_l:
        y.join()
    
if __name__ == '__main__':
    create_parllalism()