# SDK

## C# SDK

Pro vývojáře je k dispozici SDK pro C#.

### Instalace

```bash
dotnet add package Mph.OpenApi.Sdk
```

### Použití

```csharp
var client = ClientProvider.CreateClient()
    .WithApiKey("your-api-key")
    .Build();

// nebo s tokenem
var client = ClientProvider.CreateClient()
    .WithClientCredentials("clientId", "clientSecret")
    .Build();

// nebo s vlastním tokenem
var client = ClientProvider.CreateClient()
    .WithBearerToken(async token => await GetToken())
    .Build();
```

### IoC kontejner

```csharp
serviceCollection.AddMphOpenApiClient()
    .WithApiKey("your-api-key")
    .Build();
```

> Při konzumaci klienta s IoC kontejnerem je možné injectovat samotný `MphApiClient` či jednotlivé klienty podle typu např. `IBanksClient`.

### Doporučení

Při konzumaci klienta bez IoC kontejneru doporučujeme vytvořeného klienta cachovat a následně používat ideálně jako jednu instanci (singleton).

### ClientOptions

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

### Dynamické získání klienta

```csharp
var getClient = client.FindClient<IGetClient<BusinessPartnerDto>>();
```
