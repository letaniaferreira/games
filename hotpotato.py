
from class import Queue

n = 7
namelist = ["Paul", "Dilma", "Sergio", "Jay", "Kim", "Breck"]

def hotPotato(namelist, n):

    q = Queue()

    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(n):
            passer = q.dequeue()
            q.enqueue(passer)
            print("{} passed it".format(passer))

        is_out = q.dequeue()
        print("{} is out".format(is_out))

    return q.dequeue()

result = hotPotato(namelist, n)
print result