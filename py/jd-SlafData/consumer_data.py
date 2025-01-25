from idlelib.sidebar import get_widget_padding

from prompt_toolkit.utils import get_cwidth

from data_pretreatment import data, plt,pd,np

# 可知Consumer客户类型利润占比最大，下一步着重分析该类型客户，看哪种产品利润额度最大
consumer_data = data.loc[data['客户细分类型'] == 'Consumer']
consumer_profit = consumer_data.groupby('产品类别')['利润'].sum() / consumer_data['利润'].sum()
plt.figure(figsize=(14, 8))
plt.subplot(1, 4, 1)
consumer_profit.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('comsumer客户不同产品利润占比')
plt.tight_layout()
# 可见consumer客户中technology产品利润占比45.17%
# 针对consumer客户的technology产品中子产品进行详细分析


consumer_profit_sub = consumer_data.groupby('子类别')['利润'].sum() / consumer_data['利润'].sum()



plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
consumer_profit.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('消费者不同产品利润额占比')

plt.subplot(1, 2, 2)

# consumer_profit_sub.sort_values().plot(kind='barh')
# plt.bar(consumer_profit_sub.sort_values())


values2 = consumer_profit_sub.sort_values().values
index2 = consumer_profit_sub.sort_values().index
barhs = plt.barh(index2,values2)

print(type(values2))

# print(barhs)

for barh in barhs:
    height = barh.get_height()
    plt.text(barh.get_x()+0.5/2,height,f'{height}',ha = 'center',va = 'bottom')


plt.title('各子类别利润占总利润的比例')
plt.xlabel('占比')
plt.ylabel('子类别')
plt.tight_layout()

plt.show()
