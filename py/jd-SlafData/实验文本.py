import  matplotlib.pyplot as plt
import numpy as np
index1 = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25,40,30,55]

print(type(values))

# plt.figure(figsize=(10,6))
# bars = plt.bar(index1,values)
#
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2,height,
#              f'{height}',
#              ha = 'center',va = 'bottom')
#
# plt.title('data')
# plt.xlabel('index1')
# plt.ylabel('values')
# plt.show()

# import matplotlib.pyplot as plt
#
# for x in x1：    #遍历x在x1中
#     #设定一个wd函数，
#     wd = x.get_width()#读取ed的宽度
#     plt.text(wa,rect,get_y()+0.5/2,str(wd),va='center')