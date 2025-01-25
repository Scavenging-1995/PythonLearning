from shutil import COPY_BUFSIZE
from sys import orig_argv
from traceback import print_tb
from unittest.mock import inplace

import numpy as np
import pandas as pd
from pandas import value_counts

# 读取数据，命名为original(原始数据）
original_data = pd.read_excel('D:\Repository\Python\Self\practice\jd-SaleData\Data files\京东消费者分析数据.xlsx')

# obj.head()  读取数据前5行
original_data.head()

# 复制数组
cleaned_data = original_data.copy()

# dataframe.sample(n)  随机抽取n行数据
# cleaned_data.sample(5)

# 打印DataFrame 摘要，包含所有列的列表及其数据类型以及每列中非空值的数量
# print(cleaned_data.info())

# 统计店铺注册时间缺失总数
# print(cleaned_data['age_range'].isnull())
#  删除空值的行
dropna_age_range = cleaned_data.dropna()

# 计算除去空值后的age_range 平均数  mean（）平均数
mean_age_range = dropna_age_range['age_range'].mean()
# 填充平均数，fillna（）填充数据   inplace = Ture  改变原有表格数据
cleaned_data.fillna(mean_age_range, inplace=True)
# city_level 用中位数替代  mode()中位数
x1 = cleaned_data['city_level'].mode()
cleaned_data.fillna(x1, inplace=True)
# 把几行数据类型转换为字符串类型  astype('需要转换的列':'数据类型')
cleaned_data = cleaned_data.astype({'customer_id': 'string', 'product_id': 'string',
                                    'action_id': 'string', 'shop_id': 'string',
                                    'vender_id': 'string'})

# 查找重复数据  duplicated().sun()
cleaned_data.duplicated().sum()

# 查询各列数量  value_counts()  计数
# print(cleaned_data['type'].value_counts())

# 删除错误数据
cleaned_data1 = cleaned_data.query('gender != "U"')
print(cleaned_data1.gender.value_counts())
#
# cleaned_data['brand'] = cleaned_data['brand'.replace('Chando ','Chando'),
# (cleaned_data)['brand'] == 'Chando '.sum()]