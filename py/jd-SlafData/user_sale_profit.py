from data_pretreatment import data,np,plt


# 客户维度分析
user_sale = data.groupby('客户细分类型')['销售额'].sum() / data['销售额'].sum()
user_profit = data.groupby('客户细分类型')['利润'].sum() / data['利润'].sum()

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
user_sale.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('不同客户类型销售额占比')

plt.subplot(1, 2, 2)
user_profit.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('不同客户类型贡献利润占比')

plt.tight_layout()

plt.show()