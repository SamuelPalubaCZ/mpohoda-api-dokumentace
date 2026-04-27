# Vytvoření faktury z objednávky

Tento průvodce vám pomůže s vytvořením vydané faktury z přijaté objednávky.

## Použitá API metoda

```http
POST https://api.mpohoda.cz/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully
```

## Zadání dokladu

Před vytvořením vydané faktury z přijaté objednávky je zapotřebí, aby byla přijatá objednávka vytvořena v aplikaci mPohoda. Při vytváření faktur se z objednávky přenesou všechny potřebné údaje do faktur.

> **Upozornění:** Pro přenos přijaté objednávky do vydané faktury, musí mít objednávka stav: **Nevyřízená**.

> **Info:** Přijatá objednávka se do vydané faktury přenáší úplně. Aktuálně není podporován částečný přenos položek objednávky do faktury.

## Tělo požadavku

Tělo požadavku zůstává v tomto případě prázdné, protože v URL API metody je uvedeno `{Id}` přijaté objednávky, která se kompletně přenese do vydané faktury.

```json
{}
```

## Příklad volání

```bash
curl -X POST "https://api.mpohoda.cz/v1/ReceivedOrders/{id}/Transfer/ToIssuedInvoice/Fully" \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d "{}"
```

Kde `{id}` je identifikátor přijaté objednávky, kterou chcete přenést do vydané faktury.
