import numpy as np
# a=np.array([[45,67,87],
#            [56,78,89]])

# b=np.array([[34,56,67],
#             [56,57,58]])
# c=a+b
# d=a-b
# e=a*b
# f=2*a
# print(c)
# print(d)
# print(e)
# print(*f)

# a=np.array([[45,67,87]
#            [56,78,89]])

# b=np.array([[34,56,67]
#             [56,57,58]])
# c=a+b
# print(c) # TypeError: list indices must be integers or slices, not tuple

# a=np.eye(3)
# a=np.eye(3,dtype=bool)
# a=np.eye(3,dtype=int)
# a=np.eye(3,dtype=int)
# a=np.eye(50)
# print(a)

# a=np.array([x for x in range(16)])
# i=a.reshape((4,4))
# print(i)


# b=np.array([[3.4,5.6,6.7],
#             [5.6,5.7,5.8]])

# b=np.array([[34,56,67],
#             [56,57,58]])
# a=b.astype('float')
# print(a)
# b=np.array([[0,1],[1,0]])
# c=b.astype('bool')
# print(c)

# a=np.array([[45,67,87],
#            [56,78,89]])

# b=np.array([[34,56,67],
#             [56,57,58]])
# c=np.hstack((a,b))
# print(c)

# a=np.array([[45,67,87],
#            [56,78,89]])

# b=np.array([[34,56,67],
#             [56,57,58]])
# c=np.vstack((a,b))
# print(c)

# a=[x for x in range(2,56,2)]
# u=np.array(a)
# print(u)

# u=np.arange(2,45,3)
# print(u)

# a=np.array([1,2,3,4,5])
# b=np.array([0,2,1,4,5])
# print(np.where(a==b))

# a=np.full((4,4),7)
# print(a)

# a=np.array([[45,67,87],
#            [56,78,89],
#            [1,2,3]])

# b=np.array([[34,56,67],
#             [56,57,58],
#             [1,2,3]])

# # c=a@b
# d=np.matmul(a,b)
# # print(c)
# print(d)


# a=~4
# b=a+4
# print(b)

b=np.array([['a','b','c'],
    ['a','b','c']])
a=np.array([['a','b','c'],
    ['a','b','c']])
print(a+b)