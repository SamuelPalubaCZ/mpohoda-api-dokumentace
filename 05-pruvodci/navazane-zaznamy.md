# Navázané záznamy

## 1. Co je navázaný záznam?

Navázaným záznamem se rozumí například forma úhrady, bankovní účet, zásoba ze skladu nebo odběratel, které chceme uvést na vytvářené vydané faktuře. Každý záznam má v aplikaci mPohoda své unikátní id a pro uvedení požadovaného záznamu na dokladu je nutné se na daný záznam odkázat právě přes jeho id.

V sekci [Reference](../04-endpointy/README.md) je uveden seznam záznamů, se kterými lze v rámci API pracovat. Id konkrétního záznamu se získá prostřednictvím příslušné API metody pro stažení seznamu záznamů a následně se doplní do těla vytvářeného požadavku.

## 2. Získání id navázaného záznamu

Na příkladu vydané faktury si ukážeme získání id adresy odběratele (`DocumentAddressWithAddressBookLink`). Obdobným způsobem bychom pak postupovali i v případě získání id dalších záznamů, na které se chceme v těle požadavku na vytvoření vydané faktury odkázat.

### Získání id odběratele

Pomocí příslušné API metody získáme seznam odběratelů. V těle odpovědi v části `Data.Items` vyhledáme námi požadovaného odběratele 'STORMWARE s.r.o.' a zjistíme jeho id `9423064b-5842-450d-9d31-cca121b8e034`.

### Použití id v těle požadavku

Id odběratele `9423064b-5842-450d-9d31-cca121b8e034` zadáme v těle požadavku pro vytvoření vydané faktury v položce `DocumentAddressWithAddressBookLink`:

```json
{
  "Text": "Text faktúry",
  "IssueDate": "2023-01-18T13:05:11.148Z",
  "DueDate": "2023-02-01T13:05:11.148Z",
  "TaxDate": "2023-01-18T13:05:11.148Z",
  "PaymentMethodId": "e9001046-a210-49fe-bb5d-ee463b88ca9d",
  "BankAccountId": "b61898b3-3ed1-4cb5-b099-475ea32d79fe",
  "BusinessPartnerAddress": {
    "DocumentAddressWithAddressBookLink": {
      "Id": "9423064b-5842-450d-9d31-cca121b8e034"
    }
  },
  "Items": [
    {
      "TextItem": {
        "Text": "Polozka faktury 1",
        "Quantity": 1,
        "Unit": "ks",
        "UnitPrice": 100,
        "UnitPriceType": "WithoutVat",
        "VatRateType": "ZeroVatRate"
      }
    },
    {
      "TextItem": {
        "Text": "Polozka faktury 2",
        "Quantity": 2,
        "Unit": "ks",
        "UnitPrice": 50,
        "UnitPriceVatType": "WithVat",
        "VatRateType": "BasicVatRate"
      }
    }
  ]
}
```

Obdobným způsobem se získalo id záznamu pro formu úhrady Převodem a uvedlo se v těle požadavku v položce `PaymentMethodId` a id pro bankovní účet KB a uvedlo se v položce `BankAccountId`.

Po odeslání požadavku na API se v aplikaci mPohoda vytvoří nová faktura, na které bude uveden odběratel 'STORMWARE s.r.o.', forma úhrady Převodem, bankovní účet KB a dvě textové položky.
