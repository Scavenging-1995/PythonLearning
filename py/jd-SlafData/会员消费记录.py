import pandas as pd
import  numpy as np
from IPython.display import display_html

# html = f"""
# <html>
# <head>
#     <style>
#         div{{
#             background-color: rgba(224, 255, 255, 0.03); /* 包裹表格的 div 背景色 */
#         }}
#         th{{
#             background-color: #79CDCD; /* 表头背景色 */
#             color: black; /* 表头文字颜色 */
#         }}
#     </style>
# </head>
# </html>
# """
# display_html(html, raw=True)

# vip_consume  会员消费
# 会员信息
#

vip_consume_data = pd.read_csv('D:\Repository\Python\Self\Data sources\会员消费记录\会员消费表.csv')
vip_information_data = pd.read_csv('D:\Repository\Python\Self\Data sources\会员消费记录\会员信息表.csv')
stores_information_data = pd.read_csv('D:\Repository\Python\Self\Data sources\会员消费记录\门店信息表.csv')
order_data = pd.read_csv('D:\Repository\Python\Self\Data sources\会员消费记录\全国订单表.csv')
# print(vip_consume_data.info())
# 无缺失
# print(vip_consume_data.value_counts().sum())
# 无重复
print(vip_information_data.head())
# 无缺失
# print(vip_information_data.info())
# 无重复
# print(vip_information_data.value_counts().sum())


