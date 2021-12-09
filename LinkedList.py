class node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next
        
class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        new_node = node(data,self.head)
        self.head=new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next = node(data,None)
        
    

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        llstr=' '
        while itr:
            llstr+=str(itr.data) + "---->"
            itr=itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr=itr.next
        return count

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head = self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            
            itr=itr.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invalid index ")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                new_node = node(data,itr.next)
                itr.next = new_node
                break

            itr=itr.next
            count +=1  
    
    def remove_by_value(self,data):
        if self.head is None:
            print("linked list is empty")
            return

        if data == self.head.data:
            self.head=self.head.next
            return

        itr=self.head
        while itr.next:
            if data == itr.next.data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def insert_after_value(self,prev,data):
        if self.head is None:
            print("linked list is empty")
            return
        
        if self.head.data == prev:
            self.head.next=node(data,self.head.next)
            return
        
        itr=self.head
        while itr.next:
            if prev==itr.data:
                itr.next = node(data,itr.next)

            itr = itr.next

        



if __name__=='__main__':
    ll=linked_list()
    ll.insert_at_begining(23)
    ll.insert_at_begining(35)
    ll.insert_at_begining(89)
    ll.insert_at_end(2)
    ll.insert_at_end(45)
    ll.insert_values(["hello","python","linked","list","code"," *_* "])
    ll.print()
    ll.remove_at(2)
    ll.insert_at(2,6)
    ll.remove_by_value("hello")
    ll.insert_after_value("code","(❁´◡`❁)")
    ll.print()
