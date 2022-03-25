import pandas as pd

from app.models.units_model import Units

df = pd.read_csv('../files/food_data.csv', delimiter=',', encoding='unicode_escape', header=0)

# print(df.shape)
print(df.iloc[0, :]['Calcium mg'])

# units = Units(unit_name=df.iloc[0, :]['Unit'])
# minerals = Minerals(
#
# )
