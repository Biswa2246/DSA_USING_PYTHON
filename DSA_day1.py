

class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top#3
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size
ball_stack=stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack=stack(5)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("size of the stack",ball_stack.get_max_size())
print("the element deleted",ball_stack.pop())
print("after deleting the element")
ball_stack.display()
print("size of the stack",ball_stack.get_max_size())

#-----
Is it empty True
Is it empty True
8
7
6
size of the stack 5
the element deleted 8
after deleting the element
7
6
size of the stack 5


#-----------------------------------------------------------------------------------------

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data=self.__elements[self.__front]
            self.__front-=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
                
    def get_max_size(self):
        return self.__max_size
queue1=Queue(10)
print("Is it full",queue1.is_full())

print("Is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()

print("the element deleted",queue1.dequeue())
queue1.display()

#-----
Is it full False
Is it empty True
100
100
200
300
400
100
200
300
400
500
the element deleted 100
None
100
200
300
400
500

#--------------------------------------------------------------------------------------

def get_evenly_divisible_numbers(queue):
    
    new_queue = []
    for num in queue:
        if all(num % i == 0 for i in range(1, 11)):
            new_queue.append(num)
    return new_queue
queue = [13983, 10080, 18080, 7113, 2520, 2500]
new_queue = get_evenly_divisible_numbers(queue)
print(new_queue)  

#-----
[10080, 2520]

#------------------------------------------------------------------------------------------

def merge_list(list1,list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if(list[i] is None):
            list[i]=""
        if(list2[i] is None):
            list2[i]=""
        merged_data+=str(list[i])+str(list2[i])+" "
    return merged_data[:-1]
list1=['T','sk',None,'bl']
list2=['ue','is','y','he']
merged_data=merge_list(list1,list2)
print(merged_data)
#-----
list[0]he list[1]y list[2]is list[3]ue

#--------------------------------------------------------------------------------------------

queue1=[3,6,8]
queue2=['b','y','u','t','r','o']
merge_queue=[]
for i in range(max(len(queue1),len(queue2))):
    if i<len(queue1):
        merge_queue.append(queue1[i])
    if i<len(queue2):
        merge_queue.append(queue2[i])
print(merge_queue)
#-----
[3, 'b', 6, 'y', 8, 'u', 't', 'r', 'o']


#----------------------------------------------------------------------------------------------

#traversing a linked list
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3=Node("Wed")
list.headval.nextval = e2
e2.nextval =e3
list.listprint()
#-----
Mon
Tue
Wed

