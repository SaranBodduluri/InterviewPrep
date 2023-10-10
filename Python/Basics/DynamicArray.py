class DynamicArray:
    
    def __init__(self, capacity: int):
        ## use another varialbe "length" separate from capacity (duh)
        ### lets create a damn list for this class; call it arr 
        self.capacity = capacity
        self.length = 0
        self.arr = [0]* self.capacity
        
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        self.length+=1
    def pushback(self, n: int) -> None:
        ## check if there's capacity to still add things
        if self.length == self.capaciy
            self.resize()
        ## insert at next empty position
        self.arr[self.length] = n
        self.length +=1

    def popback(self) -> int:
        # .remove removes based on the VAlue. the first occurence.
        # .pop is based on index
        if self.length == 0 :
            pass
        if self.length ==1:
            self.arr.pop(0)
        self.length = self.length-1 
        self.capacity = self.capacity-1

        self.arr.pop(self.length-1)
        self.length = self.length-1
        self.capacity = self.capacity-1

    def resize(self) -> None:
        self.capacity=2*self.capacity
        new_arr= [0]*self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr= new_arr

    def getSize(self) -> int:
      return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
