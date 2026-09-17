import numpy as np

#Преобразование данных в массив
#task 1
t1 = np.array([10, 20 ,30])
print(t1)
#task 2
t2 = np.asanyarray([1, 2, 3, 4, 5])
print(t2)
#task 3
t3 = np.ascontiguousarray([1, 2, 3, 4])
print(t3)
#task 4
t4 = np.asmatrix([[1, 2], [3, 4]])
print(t4)
#task 5
t6 = np.copy(t4)
t6[0] = 12
print(t6)
#task 6
t7 = np.fromfile('prog.py', sep=',')
print(t7)
#task 7
print(t7)