# class DynamicArray:
#     def __init__(self, capacity=0):
#         self.index = 0
#         self.length = 0
#         self.capacity = capacity
#         self.arr = [None for _ in range(self.capacity)]

#     def __len__(self): return self.length

#     def isEmpty(self):
#         return self.length == 0

#     def __getitem__(self, index):
#         # if -self.length <= index < self.length:
#         #     raise IndexError('index out of range')
#         #     # print(index, self.length, 'this is test')
#         return self.arr[index]

#     def __setitem__(self, index, elem):
#         self.arr[index] = elem

#     def clear(self):
#         for i in range(self.capacity):
#             self.arr[i] = None
#         self.length = 0

#     def append(self, elem):
#         if self.length+1 >= self.capacity:
#             if self.capacity == 0:
#                 self.capacity = 1
#             else:
#                 self.capacity *= 2
#             new_arr = DynamicArray(self.capacity)
#             for i in range(self.length):
#                 new_arr[i] = self.arr[i]
#             self.arr = new_arr
#         self.arr[self.length] = elem
#         print(self.length, 'check before')
#         self.length += 1
#         print(self.length, 'check after')

#     def __delitem__(self, rm_index):
#         if rm_index >= self.length and rm_index < 0:
#             raise IndexError
#         data = self.arr[rm_index]
#         new_arr = DynamicArray(self.length-1)
#         i = 0
#         j = 0
#         while i < self.length:
#             if i == rm_index:
#                 j -= 1
#             else:
#                 new_arr[j] = self.arr[i]
#             i += 1
#             j += 1
#         self.arr = new_arr
#         self.length -= 1
#         return data

#     def remove(self, obj):
#         index = self.find(obj)
#         if index == -1:
#             return False
#         self.__delitem__(index)
#         return True

#     def find(self, elem):
#         for i in range(self.length):
#             if elem == self.arr[i]:
#                 return i
#         return -1

#     def contains(self, obj):
#         return self.find(obj) != -1

#     def __iter__(self):
#         self

#     def __next__(self):
#         pass

#     def __str__(self):
#         if self.length == 0:
#             return '[]'
#         else:
#             st = '['
#             for i in range(self.length - 1):
#                 st += str(self.arr[i] + ', ')
#             st += str(self.arr[self.length - 1]) + ']'
#         return st


# new_r = DynamicArray(10)
# new_r.append(10)
# new_r[0] = 8
# print(new_r[0])
# # new_r.append(20)
# # print(new_r)
# # print(len(new_r))
# print(new_r.find(8))

n = 10

for i in range(n, 0 - 1):
    print(i)
