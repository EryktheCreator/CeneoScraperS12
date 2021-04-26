from os import listdir
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

print(*listdir("opinions"), sep="\n")

product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

average_score = opinions.stars.mean().round(2)

stars_count = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value=0)

stars_count.plot.bar()
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.show()

# pros_count i cons_count do ogarniecia

print(opinions)
print(average_score)
print(stars_count)