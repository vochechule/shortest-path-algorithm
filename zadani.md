

## **Zadání: Grafové algoritmy pro hledání nejkratší cesty**

**Termín odevzdání:** 19. června 2025 v 7:00

### **Co máš udělat:**

### 1. **Teoretická část**

Vypracuj stručný a přehledný úvod do problematiky grafů:

* Vysvětli, co je to **graf**, jaké existují typy (orientovaný, neorientovaný, ohodnocený).
* Popiš pojem **kostra grafu**.
* Porovnej **matici sousednosti** a **seznam sousedů**.
* Uveď **příklady reálného využití** grafů (např. navigace, počítačové sítě, plánování tras atd.).

### 2. **Popiš problém hledání nejkratší cesty**

* Vysvětli, co znamená „nejkratší cesta“ v grafu.
* Zmín, jak **negativní (záporné) hrany** ovlivňují algoritmy.

### 3. **Přehled vybraných algoritmů**

Pro každý z těchto algoritmů napiš:

* **Princip fungování**
* **Výhody a nevýhody**
* **Časovou složitost**

#### a) **Dijkstrův algoritmus**

* Greedy přístup, využití prioritní fronty.
* Neumí pracovat s negativními hranami.

#### b) **Bellman-Fordův algoritmus**

* Využívá relaxaci hran.
* Funguje i s negativními hranami.
* Umí detekovat záporné cykly.

#### c) **Floyd-Warshallův algoritmus**

* Funguje pro všechny dvojice vrcholů.
* Používá dynamické programování.

---

### 4. **Praktická část – implementace**

* Vyber si **jeden z výše uvedených algoritmů** (např. Dijkstra nebo Bellman-Ford).
* Napiš **funkční implementaci** v jazyce dle vlastního výběru (např. Python, C++, Java).
* Vstup: graf zadaný jako **seznam hran nebo matice**.
* Výstup: nejkratší cesty z daného startovního vrcholu ke všem ostatním.

---

### 5. **Závěr**

* Shrň, co ses naučil.
* Uveď možnosti rozšíření (např. A\*, Johnsonův algoritmus).

---

### 6. **Odevzdání na GitHub**

Repozitář by měl obsahovat:

* Teoretickou část (body 1–3)
* Kód algoritmu
* Testovací data
* Grafy nebo vizualizace výsledků

