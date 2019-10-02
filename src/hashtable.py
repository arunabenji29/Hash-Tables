# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        
        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #code for collision
        index = self._hash_mod(key)
        print(f'\n\nindex is {index}, key is {key}')
        pair = self.storage[index]

        if pair is None:
            self.storage[index] = LinkedPair(key,value)
        else:            

            while pair.next is not None:
                print(f'insert: else: while')
                if key == pair.key:
                    pair.value = value
                    break
                pair = pair.next

            if pair.next is None:
                if key == pair.key:
                    pair.value = value
                else:
                    print(f'insert: else: else: insert key,value')
                    pair.next = LinkedPair(key,value)

                
        pair1 = self.storage[index]
        print(f'key: {pair1.key}, value is {pair1.value}')
        while pair1.next is not None:
            pair1 = pair1.next
            print(f'key: {pair1.key}, value is {pair1.value}')
            


        # code for without collision
        # if self.count >= self.capacity:
        #     self.resize()

        # index = self._hash_mod(key)

        # print(f'for key:{key}, index is {index}')

        # for i in range(self.count,index,-1):
        #     self.storage[i] = self.storage[i-1]

        # self.storage[index] = (key,value)
            
        # self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        pair = self.storage[index]

        while pair.next is not None:
                print(f'insert: else: while')
                temp = pair.next
                if key == pair.key:

                    pair.key = None
                    pair.value = None
                    break
                pair = temp

        if pair.next is None:
            if key == pair.key:
                pair.key = None
                pair.value = None



        # code without collision
        # index = self._hash_mod(key)

        # if self.storage[index] is None:
        #     print('key not found')
        #     return
        # else:
        #     self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        
        #code for with collision
        index = self._hash_mod(key)
        print(f'\nindex is {index}, key is {key}')

        pair = self.storage[index]

        if pair is None:
            return None
        else:            

            while pair.next is not None:
                if key == pair.key:
                    print('else: while: if: key matched')
                    return pair.value
                pair = pair.next

            if pair.key is not None:
                if key == pair.key:
                    print(f'else: if: key matched')
                    return pair.value
        
        



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        
        Fill this in.
        '''
        self.capacity *= 2
        temp = list(self.storage)
        new_storage = [None] * self.capacity
        self.storage = new_storage

        for index in range(len(temp)):
            if temp[index] is not None:
                pair = temp[index]
                while pair is not None:
                    self.insert(pair.key,pair.value)
                    pair= pair.next
                   


        print(f'storage array is {self.storage}')



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test remove 
#     # print(ht.remove("line_3"))
#     # print(ht.remove("line_3"))

#     # # Test resizing
#     print(f'old array is : {ht.storage}')

#     old_capacity = len(ht.storage)
#     print(f'old capacity: {old_capacity}')
#     ht.resize()
#     print(f'new array is : {ht.storage}')

#     new_capacity = len(ht.storage)
#     print(f'new capacity: {new_capacity}')

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")

