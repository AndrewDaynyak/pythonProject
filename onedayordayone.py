from collections import deque
from re import search

graph ={}
graph['you']=['Alice', 'Bob', 'Claire']
graph['Bob']=['Anuj', 'Peggy']
graph['Alice']=['Peggy']
graph['Claire']=['Tom', 'Jonny']
graph['Anuj']=[]
graph['Peggy']=[]
graph['Tom']=[]
graph['Jonny']=[]


def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False
def person_is_seller(name):
    return name[-1]=='m'
search('you')


