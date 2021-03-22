# CeneoScraperS12

## Etap 1
### 1. analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion||
|Id opinii|["data-entry-id"]|opinion_id||
|Autor|span.user-post__author-name|author||
|Rekomendacja|span.user-post__author-recomendation > em|recommendation||
|Liczba gwiazdek|span.user-post__score-count|stars||
|Treść opinii|div.user-post__text|content||
|Lista zalet|div.review-feature__col:has(> div[class*="positives"]) > div.review-feature_item|pros|
|Lista wad|div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature_item|cons||
|Czy potwierdzona zakupem|div.review-pz|purchased||
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|submit_date||
|Data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||

### 2. pobranie składowych pojedynczej opinii
- pobranie kodu pojedynczej strony z opiniami
- wyodrębnienie z kodu strony kodu pojedynczej opinii
- pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie selektorów