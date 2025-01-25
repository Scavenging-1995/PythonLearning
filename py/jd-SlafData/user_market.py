from colorama.ansi import set_title

from data_pretreatment import data, pd, np, plt

# 人与场，研究负利润客户主要所在市场
user_amount = data.groupby(['客户名称', '市场'])['利润'].sum().sort_values(ascending=False).reset_index()

user_amount['amount_cumsum'] = user_amount['利润'].cumsum()

amount_total = user_amount['amount_cumsum'].max()


# percentage  百分比
user_amount['percentage'] = user_amount['amount_cumsum'] / amount_total

minus_profit_market = user_amount.loc[user_amount['利润'] <= 0]['市场'].value_counts().sort_values()


ax = minus_profit_market.plot.barh(color='skyblue', edgecolor='black')

for index, value in enumerate(minus_profit_market):
    ax.text(value + 0.5, index, str(value), va='center', ha='left', fontsize=10)

ax.set_title('不同市场中利润小于等于0的次数', fontsize=14)

plt.tight_layout()

plt.show()
