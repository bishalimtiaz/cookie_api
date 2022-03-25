import pandas as pd

from app.models.units_model import Units
from app.models.minerals_model import Minerals
from app.models.vitamins_model import Vitamins
from app.models.food_model import Food
from app.secuirity.database import Session

df = pd.read_csv('app/files/food_data.csv', delimiter=',', encoding='unicode_escape', header=0)

food_list = []

for i in range(df.shape[0]):
    units = Units(unit_name=df.iloc[i, :]['Unit'])

    minerals = Minerals(
        calciumMg=df.iloc[i, :]['Calcium mg'],
        copperMg=df.iloc[i, :]['Copper mg'],
        ironMg=df.iloc[i, :]['Iron mg'],
        magnesiumMg=df.iloc[i, :]['Magnesium mg'],
        manganeseMg=df.iloc[i, :]['Manganese mg'],
        phosphosusMg=df.iloc[i, :]['Phosphosus mg'],
        potassiumMgval=df.iloc[i, :]['Potassium mg'],
        seleniumMicg=df.iloc[i, :]['Selenium mg'],
        sodiumMg=df.iloc[i, :]['Sodium mg'],
        zincMg=df.iloc[i, :]['Zinc mg'],
    )

    vitamins = Vitamins(
        b1ThiamineMg=df.iloc[i, :]['B1(Thiamine) mg'],
        b2RiboflavinMg=df.iloc[i, :]['B2 (Riboflavin) mg'],
        b3NiacinMg=df.iloc[i, :]['B3 (Niacin) mg'],
        b5PantothenicAcidMg=df.iloc[i, :]['B5 (Pantothenic Acid) mg'],
        b6PyridoxineMg=df.iloc[i, :]['B6 (Pyridoxine) mg'],
        b12CobalaminMicg=df.iloc[i, :]['B12 (Cobalamin) mg'],
        b7BiotinMg=df.iloc[i, :]['B7 (Biotin) mg'],
        b8CholineMg=df.iloc[i, :]['B8 (Choline) mg'],
        b9FolateMicg=df.iloc[i, :]['B9 (Folate) mg'],
        vitaminAIU=df.iloc[i, :]['Vitamin A IU'],
        vitaminCMg=df.iloc[i, :]['Vitamin C mg'],
        vitaminDIU=df.iloc[i, :]['Vitamin D IU'],
        vitaminEMg=df.iloc[i, :]['Vitamin E mg'],
        vitaminKMicg=df.iloc[i, :]['Vitamin K mg'],

    )

    food = Food(
        name=df.iloc[i, :]['Food Item'],
        quantity=df.iloc[i, :]['Quantity'],
        fat=df.iloc[i, :]['Fat'],
        protein=df.iloc[i, :]['Protein'],
        carb=df.iloc[i, :]['Carb'],
        fiber=df.iloc[i, :]['Fiber'],
        netCarb=df.iloc[i, :]['Net Carb'],
        calories=df.iloc[i, :]['Calories'],
        units=units,
        vitamins=vitamins,
        minerals=minerals
    )
    food_list.append(food)

with Session() as db:
    db.add_all(food_list)
    db.commit()
