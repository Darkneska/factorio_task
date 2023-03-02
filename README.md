# (EDA)Exploration Data Analysis
# Analýza datových souborů anonymizovaných záznamů příchozích pacientů na pohotovostní příjem

Tasks:
- Proveďte prvotní analýzu datové sady (EDA) a své nálezy zdokumentujte- viz. jednotlivé body:
- Vytvořte prediktivní model příchodu pacientů na základě těchto dat.
- Ověřte a prezentujte jeho vlastnosti (jeden graf může vydat za mnoho slov).
- Aplikaci s prediktivním modelem dockerizujte.

1) Data analyzována pomocí pandas a Matplotlib. Načtení dat -pip install requirements.txt
2) Počet řádků a sloupců. Informace o sloupcích. Sloupec "lékař" má 84 NULL hodnot. Je zde (5051 řádku, 7 sloupců)
3) Nejvyšší x nejmenší příchozí ročníky: 46. Nejméně příchozí ročník: 20.
4) Kam byli pacienti odesláni nejčastěji - domácí ošetření: 3357.
5) Kdo měl nejvíce služeb. Nejvíce směn měla paní MUDr. Kamila Devátá: 608 směn.
6) V jakých dnech/hodinách/měsicích za rok 2020 chodili pacienti nejčastěji => graf

![image](https://user-images.githubusercontent.com/84958830/222539850-1b2d364c-2498-481a-83e5-ce698968c1da.png)
![image](https://user-images.githubusercontent.com/84958830/222540036-5caafc3d-c57d-439c-862a-2ca569a2fa95.png)
![image](https://user-images.githubusercontent.com/84958830/222540183-be443a79-db7c-4623-900c-dea4a5bf2290.png)
