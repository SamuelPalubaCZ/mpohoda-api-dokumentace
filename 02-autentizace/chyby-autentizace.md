# Chyby autentizace

Při zpracování požadavků mohou nastat různé chyby z důvodu nesprávných autentizačních údajů.

## 1. Požadavky na API

V případě chybných autentizačních údajů uvedených v požadavku API vrátí následující odpověď:

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

Chybnými autentizačními údaji mohou být např. nesprávný či chybějící API klíč nebo token.

## 2. Požadavky na získání tokenu

Při získávání tokenu se v případě chybných údajů v požadavku mohou v odpovědi objevit různé chybové hlášky.

### Neplatný grant_type

```json
{
  "error": "unsupported_grant_type"
}
```

V požadavku byla chybně uvedena hodnota pole `grant_type`. Zkontrolujte, zda pole obsahuje hodnotu `client_credentials`.

### Neplatné client_id nebo client_secret

```json
{
  "error": "unsupported_grant_type"
}
```

V požadavku byla chybně uvedena hodnota pole `client_id` a/nebo `client_secret`. Zkontrolujte, zda jste zadali správné údaje.

### Neplatný scope

```json
{
  "error": "unsupported_grant_type"
}
```

V požadavku byla chybně uvedena hodnota pole `scope`. Zkontrolujte, zda jste zadali hodnotu `Mph.OpenApi.Access.Cz`.
