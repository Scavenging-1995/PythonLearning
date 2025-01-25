from data_pretreatment import data,plt,pd

import data_pretreatment

# 分析不同客户类型的主要消费产品（人与货），利润可直接修改为销售额。
# Cousumer；消费者
Consumer_Category_data = data.loc[data['客户细分类型'] == 'Consumer']
data1 = Consumer_Category_data.groupby('产品类别')['数量'].sum() / Consumer_Category_data['数量'].sum()

# Corporate；企业
Corporate_Category_data = data.loc[data['客户细分类型'] == 'Corporate']
data2 = Corporate_Category_data.groupby('产品类别')['数量'].sum() / Corporate_Category_data['数量'].sum()

# HomeOffice；家庭办公室
HomeOffice_Category_data = data.loc[data['客户细分类型'] == 'Home Office']
data3 = HomeOffice_Category_data.groupby('产品类别')['数量'].sum() / HomeOffice_Category_data['数量'].sum()

plt.figure(figsize=(14, 8))

plt.subplot(1, 3, 1)
data1.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Consumer客户中不同产品类型销售量占比')

plt.subplot(1, 3, 2)
data2.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Corporate客户中不同产品类型销售量占比')

plt.subplot(1, 3, 3)
data3.plot.pie(autopct='%1.1f%%', startangle=90)
plt, title('HomeOffice客户中不同产品类型销售量占比')
plt.tight_layout()
plt.show()