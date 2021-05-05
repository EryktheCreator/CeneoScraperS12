from os import listdir
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

print(*listdir("opinions"), sep="\n")
product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

average_score = opinions.stars.mean()
opinions_count = opinions.shape[0]
pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()
print(f"""O produkcie dostępnych jest {opinions_count} opinii.
Dla {pros_count} opinii podana została lista zalet, a dla {cons_count} lista wad.
Średnia ocena produktu wyznaczona na podstawie liczby gwiazdek wynosi {average_score:.2f}.""")

stars_count = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value=0)
stars_count.plot.bar(color = "lightskyblue")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.title("Częstośc występowania poszczególnych ocen produktu")
plt.savefig(f"./figures/{product_id}_stars.png")
plt.close()

recommendations = opinions.recomendation.value_counts(dropna = False).reindex([True, False, float("NaN")], fill_value=0)
recommendations.plot.pie(
    label = "",
    labels = ["Polecam", "Nie polecam", "Nie mam zdania"],
    autopct = "%1.1f%%",
    pctdistance = 1.2,
    labeldistance = 1.4,
    colors = ["forestgreen", "crimson", "orange"]
    )
plt.title("Udział poszczególnych rekomendacji w ogólnej liczbie opinii")
plt.legend(bbox_to_anchor = (1.0,1.0))
plt.tight_layout()
plt.savefig(f"./figures/{product_id}_rcmd.png", bbox_inches = "tight")
plt.close()

stars_recommendations = pd.crosstab(opinions.stars, opinions.recomendation)
print(stars_recommendations)