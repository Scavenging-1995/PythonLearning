import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from matplotlib.pyplot import title
# plt.rcParams['font.sans-serif'] = ['SinHei']

# %matplotlib inline

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

filename = 'D:\Repository\Python\Self\Data sources\国际电商分析\SuperStore.xlsx'
data = pd.read_excel(filename, names=["序列ID",
                                      "订单ID",
                                      "运输模式",
                                      "客户ID",
                                      "客户名称",
                                      "客户细分类型",
                                      "城市",
                                      "地区",
                                      "国家",
                                      "邮政编码",
                                      "市场",
                                      "主地区",
                                      "产品ID",
                                      "产品类别",
                                      "子类别",
                                      "产品名称",
                                      "售价",
                                      "数量",
                                      "折扣",
                                      "利润",
                                      "运费",
                                      "订单优先级",
                                      "订单日期",
                                      "订单月份",
                                      "订单月份(num)",
                                      "订单年份"])
# print(data.head())

# print(data.isnull().sum())

# print(data[data.duplicated()].count())

summary = {
    '运输模式': list(data['运输模式'].unique()),  # unique  输出不同值的详细数据
    '客户细分类型': list(data['客户细分类型'].unique()),
    '国家': [data['国家'].nunique()],  # nunique  输出不同值的个数
    '主地区': list(data['主地区'].unique()),
    '市场': list(data['市场'].unique()),
    '订单优先级': list(data['订单优先级'].unique()),
    '订单年份': list(data['订单年份'].unique()),
    '产品类别': list(data['产品类别'].unique()),
    '子类别': list(data['子类别'].unique()),
    '折扣': list(data['折扣'].unique()),
    '客户名称': [data['客户名称'].nunique()]
}
df = pd.DataFrame.from_dict(summary, orient='index').T
df = df.fillna('')
# df.to_excel('分组表.xlsx',index=False)

df.to_csv('分组信息.csv')

# print(df)
data['折扣'] = data['折扣'].replace(0.0, 1.0)
data['销售额'] = data['售价'] * data['数量'] * data['折扣'] + data['运费']
data = data[["订单ID", "运输模式", '客户ID', "客户名称", "客户细分类型",
             "城市", "地区", "国家", "市场", "主地区", "产品类别", "子类别",
             "产品名称", "售价", "数量", "折扣", "利润", "运费", "订单优先级",
             "订单日期", "订单月份", "订单月份(num)", "订单年份", '销售额']]
data.to_csv('data.csv')



