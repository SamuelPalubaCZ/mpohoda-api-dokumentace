# Struktura odpovědi

## Úspěšná odpověď

Seznamy entit vracejí paginovanou odpověď:

```json
{
  "data": [...],
  "pageSize": 10,
  "pageNumber": 1,
  "totalCount": 150,
  "totalPages": 15
}
```

## Chybová odpověď

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401,
  "traceId": "00-775c67cbb830c73c55490d8b0b397f81-f4e8fd56f1c2f1cb-00"
}
```

## Validace

```json
{
  "errors": {
    "PageNumber": [
      "'PageNumber' must be greater than '0'."
    ],
    "PageSize": [
      "'PageSize' must be greater than '0'."
    ]
  },
  "type": "https://httpstatuses.io/422",
  "title": "Unprocessable Entity",
  "status": 422,
  "traceId": "00-..."
}
```
