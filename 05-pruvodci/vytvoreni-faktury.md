# Vytvoření faktury

Tento průvodce vám pomůže s vytvořením faktury s textovými a skladovými položkami.

## Použitá API metoda

```http
POST https://api.mpohoda.cz/v1/IssuedInvoices
```

## Zadání faktury

Vydaná faktura na firmu 'ZET s.r.o.', s formou úhrady 'Převodem' na účet 'KB' bude obsahovat tři položky prodané v prodejní ceně 'Sleva 4':

- skladovou zásobu typu Karta - položka Židle Z220 (cena bez DPH 21 %)
- skladovou zásobu typu Komplet - položka Firemní kancelářská souprava (položky v ceně bez DPH 21 %)
- textovou položku - položka Montáž (cena s DPH 15 %)

## Tělo požadavku

V těle požadavku se uvedou id záznamů pro formu úhrady (`PaymentMethodId`), bankovní účet (`BankAccountId`) a odběratele (`DocumentAddressWithAddressBookLink`).

V části `Items` se vypíše seznam položek faktury:

- V případě **skladových položek** je nutné uvést jejich id a dále pak stačí už jen zadat požadované množství - ostatní údaje jako je cena či sazba DPH se na fakturu vloží automaticky dle údajů uvedených u dané skladové položky v ceníku.
- U **textových položek** se zadává kromě množství také měrná jednotka, cena, sazba DPH a způsob výpočtu DPH.
- U všech typů položek je možné uvést i doplňující údaje jako je poznámka nebo středisko.

```json
{
  "Text": "Fakturujeme Vám zboží dle Vaší objednávky:",
  "IssueDate": "2023-08-30",
  "DueDate": "2023-09-13",
  "TaxDate": "2023-08-30",
  "PaymentMethodId": "f3cadefb-ec10-48e1-a27f-0113deb71522",
  "BankAccountId": "11e9034b-45cd-4e98-b04d-4514ae33dadd",
  "SellingPriceCode": "Sleva 4",
  "BusinessPartnerAddress": {
    "DocumentAddressWithAddressBookLink": {
      "Id": "9423064b-5842-450d-9d31-cca121b8e034"
    }
  },
  "Items": [
    {
      "PriceListItem": {
        "PriceListItemId": "5bed760c-ac9d-451c-bb2d-96c353319d01",
        "Quantity": 4
      }
    },
    {
      "PriceListItem": {
        "PriceListItemId": "81f78320-ab97-44fe-b89a-416e42932080",
        "Quantity": 1
      }
    },
    {
      "TextItem": {
        "Text": "Montáž",
        "Quantity": 2,
        "UnitPrice": 380,
        "UnitPriceType": "WithVat",
        "Unit": "hod",
        "VatRateType": "FirstReducedVatRate",
        "CentreId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "ActivityId": "0db3b3b2-0e51-4213-b662-692e4c9dafd6"
      }
    }
  ]
}
```
