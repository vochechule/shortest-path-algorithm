
### **2. Problém hledání nejkratší cesty**

**Nejkratší cesta** mezi dvěma vrcholy v grafu je taková cesta, která má nejnižší celkovou váhu (nebo náklad), když sečteme váhy všech hran, přes které vede.

#### Co znamená „nejkratší“?

* V **neohodnoceném** grafu je to cesta s **nejmenším počtem hran**.
* V **ohodnoceném** grafu je to cesta s **nejnižším součtem vah hran**.

#### Záporné váhy:

* **Záporné hrany** se používají např. pro reprezentaci slev, vrácení peněz nebo časových zkratek.
* Některé algoritmy (např. **Dijkstra**) si s nimi **neumí poradit** a dávají špatné výsledky.
* Jiné algoritmy (např. **Bellman-Ford**) jsou navržené tak, aby s **negativními hranami pracovaly správně**.

#### Záporné cykly:

**Záporný cyklus** je smyčka v grafu, kde součet všech hran je záporný.

* Když po něm budeme procházet opakovaně, můžeme **snižovat celkový náklad do nekonečna**.
* V takovém případě **nemá nejkratší cesta smysl**, protože „nejkratší“ cesta vlastně **neexistuje**.
* Algoritmus Bellman-Ford dokáže **detekovat záporné cykly** a oznámit, že **nelze spočítat správné řešení**.


