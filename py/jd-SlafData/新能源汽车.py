import pandas as pd

newcar_data = pd.read_csv("D:\Repository\Python\Self\Data sources\新能源汽车\全国新能源汽车产销量（万辆）    .csv")
# print(newcar_data.head())
cleaned_data = newcar_data.copy()
print(cleaned_data.sample())
# print(cleaned_data.info())