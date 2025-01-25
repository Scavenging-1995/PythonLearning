from data_pretreatment import data, np, pd, plt

user_amount = data.groupby('客户名称')['利润'].sum().sort_values(ascending=False).reset_index()
# amount金额  total  总额
# print(user_amount,type(user_amount))

user_amount['amount_cumsum'] = user_amount['利润'].cumsum()  # 累计利润
amount_total = user_amount['amount_cumsum'].max()
# print(user_amount.get('amount_cumsum'))

# 计算百分比
user_amount['percentage'] = user_amount['amount_cumsum'] / amount_total

plt.figure(figsize=(8,6))

plt.plot(user_amount['percentage'])
plt.grid(color='grey', linestyle='--', linewidth=1, alpha=0.6)
plt.title('利润占比')
plt.ylabel('累计比率')




plt.show()