
### **3. Přehled algoritmů**

#### **a) Dijkstrův algoritmus**

* Funguje na principu **greedy přístupu** – vybírá vždy nejlevnější vrchol z těch dosud nedosažených.
* Používá **prioritní frontu** pro efektivní výběr nejbližšího vrcholu.
* **Nevýhoda**: **nefunguje** správně, pokud graf obsahuje **záporné hrany**.
* **Časová složitost**:

  * S prioritní frontou (např. min-heap): `O((V + E) log V)`
  * V = počet vrcholů, E = počet hran

#### **b) Bellman-Fordův algoritmus**

* Postupně **uvolňuje (relaxuje) hrany** a hledá kratší cesty.
* Opakuje se až **V−1** krát (V = počet vrcholů), což zaručuje správné výsledky.
* Funguje i s **negativními hranami**.
* Navíc umí **detekovat záporné cykly**.
* **Časová složitost**: `O(V * E)`

#### **c) Floyd-Warshallův algoritmus**

* Používá **dynamické programování**.
* Vypočítá **nejkratší cesty mezi všemi dvojicemi vrcholů**.
* Hodí se pro menší nebo husté grafy, kde potřebujeme znát vzdálenosti mezi všemi body.
* **Časová složitost**: `O(V^3)`
