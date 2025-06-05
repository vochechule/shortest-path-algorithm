

### **1. Úvod do grafů**

**Graf** je matematická struktura, která slouží k modelování vztahů mezi objekty. Skládá se z **vrcholů (uzlů)** a **hran (spojení mezi vrcholy)**.

#### Typy grafů:

* **Neorientovaný graf** – hrany nemají směr, spojení je obousměrné.
* **Orientovaný graf (digraf)** – hrany mají směr, spojení jde jen jedním směrem.
* **Ohodnocený graf** – každá hrana má přiřazenou váhu (např. vzdálenost, čas, náklady).

#### Kostra grafu:

**Kostra grafu** je podmnožina hran, která propojuje všechny vrcholy grafu bez vytvoření cyklů. Nejčastěji se používá v **síťovém návrhu** (např. minimální množství kabeláže).

#### Matice sousednosti vs. seznam sousedů:

* **Matice sousednosti** – 2D pole, kde `matice[i][j]` značí existenci (a případně váhu) hrany mezi vrcholy `i` a `j`. Je rychlá na čtení, ale náročná na paměť.
* **Seznam sousedů** – každý vrchol má seznam vrcholů, na které vede hrana. Úspornější pro **řídké grafy**.

#### Reálné využití grafů:

* **Navigace a mapy** – hledání nejrychlejší nebo nejkratší cesty
* **Počítačové sítě** – směrování dat mezi zařízeními
* **Plánování projektů** – závislosti mezi úkoly
* **Sociální sítě** – propojení mezi lidmi nebo účty

