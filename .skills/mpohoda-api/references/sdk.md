---
name: mpohoda-api-sdk
description: |
  C# SDK pro mPohoda API - NuGet balíčky, instalace, příklady použití,
  IoC kontejner, ClientOptions. 
  Použij tento skill při dotazech na C# SDK, NuGet, Mph.OpenApi,
  integraci do .NET aplikace, klienta pro mPohoda.
---

# mPohoda API - C# SDK

## Přehled

Pro vývojáře je k dispozici oficiální **C# SDK**, které zjednodušuje práci s API.

SDK je dostupné přes NuGet ve dvou balíčcích:
- **Mph.OpenApi.Client** — HTTP klient
- **Mph.OpenApi.Dto** — Data Transfer Objects (modely)

## Instalace

### NuGet balíčky

```bash
# Klient
dotnet add package Mph.OpenApi.Client

# DTO (datové modely)
dotnet add package Mph.OpenApi.Dto
```

### NuGet.org odkazy

- [Mph.OpenApi.Client](https://www.nuget.org/packages/Mph.OpenApi.Client/)
- [Mph.OpenApi.Dto](https://www.nuget.org/packages/Mph.OpenApi.Dto/)

---

## Použití bez IoC kontejneru

### S API klíčem

```csharp
var client = ClientProvider.CreateClient()
    .WithApiKey("your-api-key")
    .Build();

// Použití klienta
var invoices = await client.IssuedInvoices.GetAsync(pageSize: 10, pageNumber: 1);
```

### S OAuth2 (Client Credentials)

```csharp
var client = ClientProvider.CreateClient()
    .WithClientCredentials("your-clientId", "your-clientSecret")
    .Build();
```

### S vlastním tokenem

```csharp
var client = ClientProvider.CreateClient()
    .WithBearerToken(async token => await GetTokenFromYourStorage())
    .Build();
```

> **Doporučení:** Při konzumaci klienta bez IoC kontejneru doporučujeme 
> vytvořeného klienta cachovat a následně používat ideálně jako jednu 
> instanci (singleton) dle [Microsoft HttpClient guidelines](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests).

---

## Použití s IoC kontejnerem (IServiceCollection)

```csharp
services.AddMphOpenApiClient()
    .WithApiKey("your-api-key")
    .Build();

// Nebo s tokenem
services.AddMphOpenApiClient()
    .WithClientCredentials("your-clientId", "your-clientSecret")
    .Build();
```

### Injectování klienta

```csharp
public class InvoiceService
{
    private readonly IIssuedInvoicesClient _invoicesClient;
    
    public InvoiceService(IIssuedInvoicesClient invoicesClient)
    {
        _invoicesClient = invoicesClient;
    }
    
    public async Task<InvoiceDto> CreateInvoiceAsync(CreateInvoiceRequest request)
    {
        return await _invoicesClient.CreateAsync(request);
    }
}
```

> **Info:** Při konzumaci klienta s IoC kontejnerem je možné injectovat 
> samotný `MphApiClient` či jednotlivé klienty podle typu 
> např. `IBanksClient`, `IIssuedInvoicesClient`.

---

## Konfigurace klienta (ClientOptions)

```csharp
var options = new ClientOptions(
    usePredefinedPolicies: true,
    innerHandler: null,
    timeout: TimeSpan.FromSeconds(30)
);

var client = ClientProvider.CreateClient()
    .WithApiKey("your-api-key")
    .Build(options);
```

| Parametr | Typ | Výchozí | Popis |
|----------|-----|---------|-------|
| `usePredefinedPolicies` | bool | true | Použít předdefinované retry politiky |
| `innerHandler` | HttpMessageHandler | null | Vlastní HTTP handler |
| `timeout` | TimeSpan | 30s | Timeout požadavku |

---

## Příklady použití

### Vytvoření faktury

```csharp
var request = new CreateIssuedInvoiceRequest
{
    Text = "Faktura za zboží",
    IssueDate = DateTime.Now,
    DueDate = DateTime.Now.AddDays(14),
    BusinessPartnerAddress = new DocumentAddressWithAddressBookLink
    {
        Id = Guid.Parse("9423064b-5842-450d-9d31-cca121b8e034")
    },
    Items = new List<InvoiceItem>
    {
        new InvoiceItem
        {
            TextItem = new TextItem
            {
                Text = "Polozka 1",
                Quantity = 1,
                UnitPrice = 1000,
                UnitPriceType = UnitPriceType.WithoutVat,
                VatRateType = VatRateType.BasicVatRate
            }
        }
    }
};

var invoice = await client.IssuedInvoices.CreateAsync(request);
```

### Stažení seznamu faktur

```csharp
var response = await client.IssuedInvoices.GetAsync(
    pageSize: 50, 
    pageNumber: 1
);

foreach (var invoice in response.Data.Items)
{
    Console.WriteLine($"{invoice.Id}: {invoice.Text}");
}
```

### Stažení PDF

```csharp
var pdfBytes = await client.IssuedInvoices.GetPdfAsync(
    id: Guid.Parse("550e8400-e29b-41d4-a716-446655440000"),
    language: Language.Cz
);

await File.WriteAllBytesAsync("faktura.pdf", pdfBytes);
```

### Přenos objednávky na fakturu

```csharp
var invoice = await client.ReceivedOrders.TransferToIssuedInvoiceFullyAsync(
    id: Guid.Parse("550e8400-e29b-41d4-a716-446655440000")
);
```

---

## Dynamické získání klienta

```csharp
var getClient = client.FindClient<IGetClient<BusinessPartnerDto>>();
var partners = await getClient.GetAsync(pageSize: 10);
```

---

## Dokumentace a odkazy

- [Redoc dokumentace](https://api.mpohoda.cz/redoc) — Ukázky použití u jednotlivých endpointů
- [NuGet Client](https://www.nuget.org/packages/Mph.OpenApi.Client/)
- [NuGet DTO](https://www.nuget.org/packages/Mph.OpenApi.Dto/)
- [Swagger UI](https://api.mpohoda.cz/swagger/index.html)

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Autentizace](../references/autentizace.md) — Jak se přihlásit
- [Endpointy](../references/endpointy.md) — Seznam všech API metod
- [Průvodci](../references/pruvodci.md) — Návody krok za krokem
- [Struktura dat](../references/struktura-dat.md) — Formáty, chybové kódy

---

**Synchronizováno s:** api.mpohoda.cz/doc/guides/general/libraries  
**Verze:** 1.0.0
