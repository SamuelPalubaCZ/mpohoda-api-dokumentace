# Způsoby autentizace

API mPohoda podporuje dva způsoby autentizace:

1. **API klíč**
2. **Přístupový token (access token)**

> Z hlediska větší bezpečnosti doporučujeme použít přístup pomocí přístupového tokenu.

---

## 1. API klíč

Api klíč je unikátní identifikátor sloužící k identifikaci uživatele a firmy. Jedná se o tajnou informaci a je tedy nutné ho uchovat na bezpečném místě, podobně jako např. hesla.

### Použití

Api klíč je nutné vložit do hlavičky každého požadavku. Tím se zároveň definuje, pro jakého uživatele a firmu se požadavek provádí.

| Název | Typ | Popis |
| --- | --- | --- |
| `Api-Key` | string | API klíč vygenerovaný v agendě API |

```http
Api-Key: 4bef30e89dcd352e8371da053b16f0cf6faf27c31f780f52c3a3cb7604a81a85
```

### Vygenerování API klíče

Nový API klíč vygenerujete v [agendě API](https://app.mpohoda.cz/otevrene-api) kliknutím na tlačítko Nový klíč v sekci Přístup pomocí API klíče, zadáním názvu klíče a potvrzením kliknutím na tlačítko Vytvořit.

Klíč se zobrazí v dialogovém okně. Jedná se o tajnou informaci, kterou je nutné uložit na bezpečném místě mimo aplikaci mPohoda.

> Po zavření dialogu nelze z bezpečnostních důvodů klíč znovu zobrazit.

---

## 2. Token

Token rovněž slouží k identifikaci uživatele a firmy, jeho platnost je však časově omezená. Klient obdrží přístupový token po úspěšné autentizaci na autentizačním serveru, s využitím OAuth2 a Client Credentials Grant Type.

### Použití

Token je nutné vložit do hlavičky každého požadavku:

| Název | Typ | Popis |
| --- | --- | --- |
| `Authorization` | string | Token ve tvaru `Bearer {token}` |

```http
Authorization: Bearer eyJhbGciOi...
```

### Získání tokenu

Získání tokenu probíhá dle standardu OAuth2 s využitím Client Credentials Grant Type.

> Tento typ je vhodný pouze pro aplikace, které umožňují bezpečné uložení autentizačních údajů Client Id a Client Secret, zejména serverové. Zároveň je vhodný pouze pro aplikace, kde uživatel (i firma) může být pevně specifikován a není tak vyžadováno přihlášení různých uživatelů.

#### Vygenerování klienta

Nového klienta vytvoříte v [agendě API](https://app.mpohoda.cz/otevrene-api) kliknutím na tlačítko Nový klient v sekci Přístup pomocí přístupového tokenu, zadáním názvu klienta a potvrzením kliknutím na tlačítko Vytvořit.

Pro přístup pomocí tokenu se vytvoří Client Id a Client Secret, které se zobrazí v dialogovém okně.

> Po zavření dialogu nelze z bezpečnostních důvodů Client Secret znovu zobrazit.

#### Získání tokenu z autentizačního serveru

```bash
curl -X POST "https://ucet.pohoda.cz/connect/token"   -H "Content-Type: application/x-www-form-urlencoded"   -d "grant_type=client_credentials"   -d "client_id=váše-client-id"   -d "client_secret=váš-client-secret"   -d "scope=Mph.OpenApi.Access.Cz"
```

#### Odpověď:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```
