import pandas as pd
print("Hello World")

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)

data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

fechas = pd.date_range(start="2021-05-01", end="2021-05-12")
print(fechas)

my_series = pd.Series([2, 4, 6, 8, 10])

print(my_series.apply(lambda x: x / 2))

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=["Brand","Model","Color"])
print(df)

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
     {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]

df = pd.DataFrame(data)
print(df)

df_pokemon = pd.DataFrame(data_frame)
print(df_pokemon.iloc[133, 6])

print(df_pokemon.head(3))

print(df_pokemon.tail(3))

print(df_pokemon[["Name","Type 1"]][0:10])

print(df_pokemon.loc[df_pokemon["Attack"] > 80])

print(len(df_pokemon.loc[df_pokemon["Legendary"] == True]))

bb_names = pd.read_csv(".learn/assets/us_baby_names_right.csv")

print(bb_names.head(5))

new_bb_names = bb_names.drop("Unnamed: 0", axis=1)

print(new_bb_names.head(5))

print(new_bb_names.value_counts("Gender"))

suma = new_bb_names.groupby("Name")

print(len(suma.sum()))
