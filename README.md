## Zadanie

Powyższe dane przedstawiają szereg czasowy średnich kwartalnych jednostkowych cen transakcyjnych metra kwadratowego mieszkań na rynku pierwotnym w segmencie 7 dużych miast (Warszawa, Kraków, Wrocław, Poznań, Gdańsk, Gdynia, Łódź) - źródło CBN.
Dodatkowo, przedstawiono przykładowy zestaw wskaźników dotyczących zmiennych reprezentujących kategorie mogące mieć potencjalny wpływ na kształtowanie się cen nieruchomości mieszkaniowych.

ZADANIE - przedstaw koncepcję budowy modelu predykcyjnego cen transakcyjnych metra kwadratowego mieszkania na rynku pierwotnym w segmencie 7 dużych miast 
(jeśli dysponujesz narzędziem by taki model stworzyć, to mile wiedziane będzie przedstawienie prognozy na 4Q2024 oraz na 4Q2025 na podstawie wskazania tego modelu)																	

- metoda analizy, postać modelu - dowolne ;
- w modelu można - choć nie trzeba - wykorzystać dowolny zestaw zmiennych objaśniających egzogenicznych (można uwzględnić dane przedstawione pod szeregiem czasowym cen albo inne dostępne dane)

UWAGA! Gwałtowny wzrost popytu na kredyty i nieruchomości mieszkaniowe w drugiej połowie 2023 wynika z uruchomienia rządowego programu kredytów z preferencyjnym oprocentowaniem Bezpieczny Kredyt 2% (program był aktywny w okresie 01-07-2023 do 31-12-2023). Powyższe miało wpływ na dynamikę zmian cen w okresie 3Q2023 - 1Q2024. 
Program Bezpieczny Kredyt 2% został wygaszony z końcem 2023 roku. Na dzień dzisiejszy nie wiadomo czy zostanie wdrożony nowy program wsparcia dla kredytobiorców, dlatego należy przyjąć założenie, że w okresie objętym prognozą żadna forma wsparcia nie będzie funkcjonować.																	

## Dodatkowe faktory

1. stopy procentowe Centralnego Banku Europejskiego
2. stopy procentowe FED
3. budownictwo mieszkaniowe w Polsce
4. Dlugoterminowe
-  sytuacja demograficzna (liczba zgonow, licba urodzeń, liczba domów dla seniorów, migracja)
-  realne wynagrodzenia w Polsce (nie nominalne)
-  tempo rozwoju gospodarki
  5. 


##

> __Czy gdyby podaż nieruchomości przewyższała popyt, można spodziewać się obniżek cen?__? Deweloperzy są w tak dobrej kondycji po ostatnich bardzo dobrych dla nich latach, że w sytuacji, gdyby wysoka podaż wywierała presję na obniżkę ceny, mogą ten moment przeczekać - mają bowiem silne bilanse i stać ich na czekanie - stwierdza Gołębiewski.

> Trendu bocznego w cenach średnich w dużych miastach. Lekkiego spadku cen (powolnego) w małych miastach. __Wyspowych głośnych dowodów na spadki i na wzrosty__ - to znaczy w zależności od tezy - będzie można znaleźć dane potwierdzające zarówno spadki (w wybranych segmentach, metrażach, rynek pierwotny versus rynek wtórny, miastach, etc.), jak i wzrosty.

> __Coraz mniejszy sens będzie miało patrzenie na średnie ceny__ dla Polski, a coraz ważniejsze będzie patrzenie przez pryzmat poszczególnych segmentów.

> __cały czas będzie silny, choć nie rosnący, trend inwestowania w mieszkania na wynajem__.

> __Nic nie wskazuje, by czekało nas załamanie, ani dalsza koniunktura jak ostatnio__. Musimy pamiętać, że jesteśmy po latach rekordowych pod wieloma względami i kolejne lata będą na ich tle wzbudzały emocje.

# Korelacja

<style type="text/css">
#T_875bc_row0_col0, #T_875bc_row1_col1, #T_875bc_row2_col2, #T_875bc_row3_col3, #T_875bc_row4_col4, #T_875bc_row5_col5, #T_875bc_row6_col6, #T_875bc_row7_col7, #T_875bc_row8_col8, #T_875bc_row9_col9, #T_875bc_row10_col10 {
  background-color: #b40426;
  color: #f1f1f1;
}
#T_875bc_row0_col1 {
  background-color: #ee8468;
  color: #f1f1f1;
}
#T_875bc_row0_col2, #T_875bc_row4_col6 {
  background-color: #f6a586;
  color: #000000;
}
#T_875bc_row0_col3, #T_875bc_row1_col3, #T_875bc_row2_col5 {
  background-color: #e46e56;
  color: #f1f1f1;
}
#T_875bc_row0_col4, #T_875bc_row4_col5 {
  background-color: #a5c3fe;
  color: #000000;
}
#T_875bc_row0_col5, #T_875bc_row1_col5, #T_875bc_row5_col0, #T_875bc_row5_col1 {
  background-color: #d55042;
  color: #f1f1f1;
}
#T_875bc_row0_col6, #T_875bc_row2_col8 {
  background-color: #5d7ce6;
  color: #f1f1f1;
}
#T_875bc_row0_col7, #T_875bc_row1_col10, #T_875bc_row2_col6 {
  background-color: #4f69d9;
  color: #f1f1f1;
}
#T_875bc_row0_col8, #T_875bc_row6_col3 {
  background-color: #3d50c3;
  color: #f1f1f1;
}
#T_875bc_row0_col9, #T_875bc_row0_col10, #T_875bc_row1_col6, #T_875bc_row1_col7, #T_875bc_row3_col4, #T_875bc_row5_col8, #T_875bc_row6_col1, #T_875bc_row6_col2, #T_875bc_row7_col3, #T_875bc_row8_col0, #T_875bc_row8_col5 {
  background-color: #3b4cc0;
  color: #f1f1f1;
}
#T_875bc_row1_col0 {
  background-color: #ee8669;
  color: #f1f1f1;
}
#T_875bc_row1_col2, #T_875bc_row5_col3 {
  background-color: #dc5d4a;
  color: #f1f1f1;
}
#T_875bc_row1_col4 {
  background-color: #3f53c6;
  color: #f1f1f1;
}
#T_875bc_row1_col8 {
  background-color: #4e68d8;
  color: #f1f1f1;
}
#T_875bc_row1_col9 {
  background-color: #3c4ec2;
  color: #f1f1f1;
}
#T_875bc_row2_col0 {
  background-color: #f59f80;
  color: #000000;
}
#T_875bc_row2_col1, #T_875bc_row3_col5 {
  background-color: #d95847;
  color: #f1f1f1;
}
#T_875bc_row2_col3, #T_875bc_row3_col2 {
  background-color: #f59d7e;
  color: #000000;
}
#T_875bc_row2_col4 {
  background-color: #6788ee;
  color: #f1f1f1;
}
#T_875bc_row2_col7 {
  background-color: #5673e0;
  color: #f1f1f1;
}
#T_875bc_row2_col9 {
  background-color: #88abfd;
  color: #000000;
}
#T_875bc_row2_col10 {
  background-color: #93b5fe;
  color: #000000;
}
#T_875bc_row3_col0 {
  background-color: #e36b54;
  color: #f1f1f1;
}
#T_875bc_row3_col1 {
  background-color: #e26952;
  color: #f1f1f1;
}
#T_875bc_row3_col6 {
  background-color: #516ddb;
  color: #f1f1f1;
}
#T_875bc_row3_col7, #T_875bc_row7_col1 {
  background-color: #445acc;
  color: #f1f1f1;
}
#T_875bc_row3_col8 {
  background-color: #7396f5;
  color: #f1f1f1;
}
#T_875bc_row3_col9 {
  background-color: #4358cb;
  color: #f1f1f1;
}
#T_875bc_row3_col10, #T_875bc_row4_col3, #T_875bc_row7_col2 {
  background-color: #4b64d5;
  color: #f1f1f1;
}
#T_875bc_row4_col0 {
  background-color: #bcd2f7;
  color: #000000;
}
#T_875bc_row4_col1 {
  background-color: #6485ec;
  color: #f1f1f1;
}
#T_875bc_row4_col2 {
  background-color: #799cf8;
  color: #f1f1f1;
}
#T_875bc_row4_col7 {
  background-color: #f7aa8c;
  color: #000000;
}
#T_875bc_row4_col8 {
  background-color: #aac7fd;
  color: #000000;
}
#T_875bc_row4_col9 {
  background-color: #dedcdb;
  color: #000000;
}
#T_875bc_row4_col10, #T_875bc_row9_col5 {
  background-color: #c3d5f4;
  color: #000000;
}
#T_875bc_row5_col2 {
  background-color: #e7745b;
  color: #f1f1f1;
}
#T_875bc_row5_col4 {
  background-color: #86a9fc;
  color: #f1f1f1;
}
#T_875bc_row5_col6 {
  background-color: #6384eb;
  color: #f1f1f1;
}
#T_875bc_row5_col7, #T_875bc_row6_col5 {
  background-color: #6180e9;
  color: #f1f1f1;
}
#T_875bc_row5_col9 {
  background-color: #7ea1fa;
  color: #f1f1f1;
}
#T_875bc_row5_col10 {
  background-color: #98b9ff;
  color: #000000;
}
#T_875bc_row6_col0 {
  background-color: #5875e1;
  color: #f1f1f1;
}
#T_875bc_row6_col4 {
  background-color: #f7b396;
  color: #000000;
}
#T_875bc_row6_col7, #T_875bc_row7_col6 {
  background-color: #b70d28;
  color: #f1f1f1;
}
#T_875bc_row6_col8 {
  background-color: #cad8ef;
  color: #000000;
}
#T_875bc_row6_col9 {
  background-color: #e0dbd8;
  color: #000000;
}
#T_875bc_row6_col10 {
  background-color: #c1d4f4;
  color: #000000;
}
#T_875bc_row7_col0 {
  background-color: #5470de;
  color: #f1f1f1;
}
#T_875bc_row7_col4 {
  background-color: #f7b497;
  color: #000000;
}
#T_875bc_row7_col5 {
  background-color: #688aef;
  color: #f1f1f1;
}
#T_875bc_row7_col8 {
  background-color: #c5d6f2;
  color: #000000;
}
#T_875bc_row7_col9 {
  background-color: #edd2c3;
  color: #000000;
}
#T_875bc_row7_col10 {
  background-color: #d7dce3;
  color: #000000;
}
#T_875bc_row8_col1 {
  background-color: #506bda;
  color: #f1f1f1;
}
#T_875bc_row8_col2 {
  background-color: #4a63d3;
  color: #f1f1f1;
}
#T_875bc_row8_col3 {
  background-color: #6282ea;
  color: #f1f1f1;
}
#T_875bc_row8_col4 {
  background-color: #8caffe;
  color: #000000;
}
#T_875bc_row8_col6 {
  background-color: #ccd9ed;
  color: #000000;
}
#T_875bc_row8_col7 {
  background-color: #c0d4f5;
  color: #000000;
}
#T_875bc_row8_col9 {
  background-color: #a2c1ff;
  color: #000000;
}
#T_875bc_row8_col10 {
  background-color: #7da0f9;
  color: #f1f1f1;
}
#T_875bc_row9_col0 {
  background-color: #8badfd;
  color: #000000;
}
#T_875bc_row9_col1 {
  background-color: #92b4fe;
  color: #000000;
}
#T_875bc_row9_col2 {
  background-color: #bed2f6;
  color: #000000;
}
#T_875bc_row9_col3 {
  background-color: #85a8fc;
  color: #f1f1f1;
}
#T_875bc_row9_col4 {
  background-color: #efcebd;
  color: #000000;
}
#T_875bc_row9_col6 {
  background-color: #f5c0a7;
  color: #000000;
}
#T_875bc_row9_col7 {
  background-color: #f7b79b;
  color: #000000;
}
#T_875bc_row9_col8 {
  background-color: #d8dce2;
  color: #000000;
}
#T_875bc_row9_col10 {
  background-color: #d44e41;
  color: #f1f1f1;
}
#T_875bc_row10_col0 {
  background-color: #9dbdff;
  color: #000000;
}
#T_875bc_row10_col1 {
  background-color: #b2ccfb;
  color: #000000;
}
#T_875bc_row10_col2 {
  background-color: #d1dae9;
  color: #000000;
}
#T_875bc_row10_col3 {
  background-color: #9fbfff;
  color: #000000;
}
#T_875bc_row10_col4 {
  background-color: #e6d7cf;
  color: #000000;
}
#T_875bc_row10_col5 {
  background-color: #dcdddd;
  color: #000000;
}
#T_875bc_row10_col6 {
  background-color: #f0cdbb;
  color: #000000;
}
#T_875bc_row10_col7 {
  background-color: #f5c4ac;
  color: #000000;
}
#T_875bc_row10_col8 {
  background-color: #cedaeb;
  color: #000000;
}
#T_875bc_row10_col9 {
  background-color: #d1493f;
  color: #f1f1f1;
}
</style>
<table id="T_875bc">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_875bc_level0_col0" class="col_heading level0 col0" >rynek</th>
      <th id="T_875bc_level0_col1" class="col_heading level0 col1" >inflacja_r</th>
      <th id="T_875bc_level0_col2" class="col_heading level0 col2" >inflacja_q</th>
      <th id="T_875bc_level0_col3" class="col_heading level0 col3" >stopa_procentowa</th>
      <th id="T_875bc_level0_col4" class="col_heading level0 col4" >liczba_kredytow</th>
      <th id="T_875bc_level0_col5" class="col_heading level0 col5" >tempo_wzrostu</th>
      <th id="T_875bc_level0_col6" class="col_heading level0 col6" >ufnosc</th>
      <th id="T_875bc_level0_col7" class="col_heading level0 col7" >duze_zakupy</th>
      <th id="T_875bc_level0_col8" class="col_heading level0 col8" >bezrobocie</th>
      <th id="T_875bc_level0_col9" class="col_heading level0 col9" >spr_detaliczna</th>
      <th id="T_875bc_level0_col10" class="col_heading level0 col10" >pkb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_875bc_level0_row0" class="row_heading level0 row0" >rynek</th>
      <td id="T_875bc_row0_col0" class="data row0 col0" >1.000</td>
      <td id="T_875bc_row0_col1" class="data row0 col1" >0.657</td>
      <td id="T_875bc_row0_col2" class="data row0 col2" >0.558</td>
      <td id="T_875bc_row0_col3" class="data row0 col3" >0.751</td>
      <td id="T_875bc_row0_col4" class="data row0 col4" >-0.023</td>
      <td id="T_875bc_row0_col5" class="data row0 col5" >0.840</td>
      <td id="T_875bc_row0_col6" class="data row0 col6" >-0.517</td>
      <td id="T_875bc_row0_col7" class="data row0 col7" >-0.535</td>
      <td id="T_875bc_row0_col8" class="data row0 col8" >-0.678</td>
      <td id="T_875bc_row0_col9" class="data row0 col9" >-0.266</td>
      <td id="T_875bc_row0_col10" class="data row0 col10" >-0.182</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row1" class="row_heading level0 row1" >inflacja_r</th>
      <td id="T_875bc_row1_col0" class="data row1 col0" >0.657</td>
      <td id="T_875bc_row1_col1" class="data row1 col1" >1.000</td>
      <td id="T_875bc_row1_col2" class="data row1 col2" >0.812</td>
      <td id="T_875bc_row1_col3" class="data row1 col3" >0.756</td>
      <td id="T_875bc_row1_col4" class="data row1 col4" >-0.477</td>
      <td id="T_875bc_row1_col5" class="data row1 col5" >0.837</td>
      <td id="T_875bc_row1_col6" class="data row1 col6" >-0.708</td>
      <td id="T_875bc_row1_col7" class="data row1 col7" >-0.648</td>
      <td id="T_875bc_row1_col8" class="data row1 col8" >-0.582</td>
      <td id="T_875bc_row1_col9" class="data row1 col9" >-0.258</td>
      <td id="T_875bc_row1_col10" class="data row1 col10" >-0.099</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row2" class="row_heading level0 row2" >inflacja_q</th>
      <td id="T_875bc_row2_col0" class="data row2 col0" >0.558</td>
      <td id="T_875bc_row2_col1" class="data row2 col1" >0.812</td>
      <td id="T_875bc_row2_col2" class="data row2 col2" >1.000</td>
      <td id="T_875bc_row2_col3" class="data row2 col3" >0.587</td>
      <td id="T_875bc_row2_col4" class="data row2 col4" >-0.286</td>
      <td id="T_875bc_row2_col5" class="data row2 col5" >0.737</td>
      <td id="T_875bc_row2_col6" class="data row2 col6" >-0.591</td>
      <td id="T_875bc_row2_col7" class="data row2 col7" >-0.499</td>
      <td id="T_875bc_row2_col8" class="data row2 col8" >-0.504</td>
      <td id="T_875bc_row2_col9" class="data row2 col9" >0.035</td>
      <td id="T_875bc_row2_col10" class="data row2 col10" >0.134</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row3" class="row_heading level0 row3" >stopa_procentowa</th>
      <td id="T_875bc_row3_col0" class="data row3 col0" >0.751</td>
      <td id="T_875bc_row3_col1" class="data row3 col1" >0.756</td>
      <td id="T_875bc_row3_col2" class="data row3 col2" >0.587</td>
      <td id="T_875bc_row3_col3" class="data row3 col3" >1.000</td>
      <td id="T_875bc_row3_col4" class="data row3 col4" >-0.502</td>
      <td id="T_875bc_row3_col5" class="data row3 col5" >0.811</td>
      <td id="T_875bc_row3_col6" class="data row3 col6" >-0.580</td>
      <td id="T_875bc_row3_col7" class="data row3 col7" >-0.596</td>
      <td id="T_875bc_row3_col8" class="data row3 col8" >-0.394</td>
      <td id="T_875bc_row3_col9" class="data row3 col9" >-0.230</td>
      <td id="T_875bc_row3_col10" class="data row3 col10" >-0.113</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row4" class="row_heading level0 row4" >liczba_kredytow</th>
      <td id="T_875bc_row4_col0" class="data row4 col0" >-0.023</td>
      <td id="T_875bc_row4_col1" class="data row4 col1" >-0.477</td>
      <td id="T_875bc_row4_col2" class="data row4 col2" >-0.286</td>
      <td id="T_875bc_row4_col3" class="data row4 col3" >-0.502</td>
      <td id="T_875bc_row4_col4" class="data row4 col4" >1.000</td>
      <td id="T_875bc_row4_col5" class="data row4 col5" >-0.152</td>
      <td id="T_875bc_row4_col6" class="data row4 col6" >0.521</td>
      <td id="T_875bc_row4_col7" class="data row4 col7" >0.514</td>
      <td id="T_875bc_row4_col8" class="data row4 col8" >-0.130</td>
      <td id="T_875bc_row4_col9" class="data row4 col9" >0.373</td>
      <td id="T_875bc_row4_col10" class="data row4 col10" >0.302</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row5" class="row_heading level0 row5" >tempo_wzrostu</th>
      <td id="T_875bc_row5_col0" class="data row5 col0" >0.840</td>
      <td id="T_875bc_row5_col1" class="data row5 col1" >0.837</td>
      <td id="T_875bc_row5_col2" class="data row5 col2" >0.737</td>
      <td id="T_875bc_row5_col3" class="data row5 col3" >0.811</td>
      <td id="T_875bc_row5_col4" class="data row5 col4" >-0.152</td>
      <td id="T_875bc_row5_col5" class="data row5 col5" >1.000</td>
      <td id="T_875bc_row5_col6" class="data row5 col6" >-0.482</td>
      <td id="T_875bc_row5_col7" class="data row5 col7" >-0.445</td>
      <td id="T_875bc_row5_col8" class="data row5 col8" >-0.693</td>
      <td id="T_875bc_row5_col9" class="data row5 col9" >-0.003</td>
      <td id="T_875bc_row5_col10" class="data row5 col10" >0.152</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row6" class="row_heading level0 row6" >ufnosc</th>
      <td id="T_875bc_row6_col0" class="data row6 col0" >-0.517</td>
      <td id="T_875bc_row6_col1" class="data row6 col1" >-0.708</td>
      <td id="T_875bc_row6_col2" class="data row6 col2" >-0.591</td>
      <td id="T_875bc_row6_col3" class="data row6 col3" >-0.580</td>
      <td id="T_875bc_row6_col4" class="data row6 col4" >0.521</td>
      <td id="T_875bc_row6_col5" class="data row6 col5" >-0.482</td>
      <td id="T_875bc_row6_col6" class="data row6 col6" >1.000</td>
      <td id="T_875bc_row6_col7" class="data row6 col7" >0.983</td>
      <td id="T_875bc_row6_col8" class="data row6 col8" >0.040</td>
      <td id="T_875bc_row6_col9" class="data row6 col9" >0.384</td>
      <td id="T_875bc_row6_col10" class="data row6 col10" >0.296</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row7" class="row_heading level0 row7" >duze_zakupy</th>
      <td id="T_875bc_row7_col0" class="data row7 col0" >-0.535</td>
      <td id="T_875bc_row7_col1" class="data row7 col1" >-0.648</td>
      <td id="T_875bc_row7_col2" class="data row7 col2" >-0.499</td>
      <td id="T_875bc_row7_col3" class="data row7 col3" >-0.596</td>
      <td id="T_875bc_row7_col4" class="data row7 col4" >0.514</td>
      <td id="T_875bc_row7_col5" class="data row7 col5" >-0.445</td>
      <td id="T_875bc_row7_col6" class="data row7 col6" >0.983</td>
      <td id="T_875bc_row7_col7" class="data row7 col7" >1.000</td>
      <td id="T_875bc_row7_col8" class="data row7 col8" >0.014</td>
      <td id="T_875bc_row7_col9" class="data row7 col9" >0.454</td>
      <td id="T_875bc_row7_col10" class="data row7 col10" >0.384</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row8" class="row_heading level0 row8" >bezrobocie</th>
      <td id="T_875bc_row8_col0" class="data row8 col0" >-0.678</td>
      <td id="T_875bc_row8_col1" class="data row8 col1" >-0.582</td>
      <td id="T_875bc_row8_col2" class="data row8 col2" >-0.504</td>
      <td id="T_875bc_row8_col3" class="data row8 col3" >-0.394</td>
      <td id="T_875bc_row8_col4" class="data row8 col4" >-0.130</td>
      <td id="T_875bc_row8_col5" class="data row8 col5" >-0.693</td>
      <td id="T_875bc_row8_col6" class="data row8 col6" >0.040</td>
      <td id="T_875bc_row8_col7" class="data row8 col7" >0.014</td>
      <td id="T_875bc_row8_col8" class="data row8 col8" >1.000</td>
      <td id="T_875bc_row8_col9" class="data row8 col9" >0.125</td>
      <td id="T_875bc_row8_col10" class="data row8 col10" >0.063</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row9" class="row_heading level0 row9" >spr_detaliczna</th>
      <td id="T_875bc_row9_col0" class="data row9 col0" >-0.266</td>
      <td id="T_875bc_row9_col1" class="data row9 col1" >-0.258</td>
      <td id="T_875bc_row9_col2" class="data row9 col2" >0.035</td>
      <td id="T_875bc_row9_col3" class="data row9 col3" >-0.230</td>
      <td id="T_875bc_row9_col4" class="data row9 col4" >0.373</td>
      <td id="T_875bc_row9_col5" class="data row9 col5" >-0.003</td>
      <td id="T_875bc_row9_col6" class="data row9 col6" >0.384</td>
      <td id="T_875bc_row9_col7" class="data row9 col7" >0.454</td>
      <td id="T_875bc_row9_col8" class="data row9 col8" >0.125</td>
      <td id="T_875bc_row9_col9" class="data row9 col9" >1.000</td>
      <td id="T_875bc_row9_col10" class="data row9 col10" >0.893</td>
    </tr>
    <tr>
      <th id="T_875bc_level0_row10" class="row_heading level0 row10" >pkb</th>
      <td id="T_875bc_row10_col0" class="data row10 col0" >-0.182</td>
      <td id="T_875bc_row10_col1" class="data row10 col1" >-0.099</td>
      <td id="T_875bc_row10_col2" class="data row10 col2" >0.134</td>
      <td id="T_875bc_row10_col3" class="data row10 col3" >-0.113</td>
      <td id="T_875bc_row10_col4" class="data row10 col4" >0.302</td>
      <td id="T_875bc_row10_col5" class="data row10 col5" >0.152</td>
      <td id="T_875bc_row10_col6" class="data row10 col6" >0.296</td>
      <td id="T_875bc_row10_col7" class="data row10 col7" >0.384</td>
      <td id="T_875bc_row10_col8" class="data row10 col8" >0.063</td>
      <td id="T_875bc_row10_col9" class="data row10 col9" >0.893</td>
      <td id="T_875bc_row10_col10" class="data row10 col10" >1.000</td>
    </tr>
  </tbody>
</table>

Kolumny _ufność_ i _duże zakupy_ mają dużą korelacją, dlatego jedna z nich może być usunięta z modeli. Następny kandendat na usunięcie jadna kolumna z pary _sprzedaż detaliczna_ i _PKB_.


# Linki
 1. [www.rmf24.pl/ekonomia](https://www.rmf24.pl/ekonomia/news-wzrost-spadek-czy-stabilizacja-7-ekspertow-o-przyszlosci-cen,nId,7754944#crp_state=1)
 2. [legalbusiness.pl/rosnie-popyt-na-domy-dla-seniorow-w-polsce-jest-ich-niemal-najmniej-w-europie-raport-cbre-i-greenberg-traurig/](https://legalbusiness.pl/rosnie-popyt-na-domy-dla-seniorow-w-polsce-jest-ich-niemal-najmniej-w-europie-raport-cbre-i-greenberg-traurig/)