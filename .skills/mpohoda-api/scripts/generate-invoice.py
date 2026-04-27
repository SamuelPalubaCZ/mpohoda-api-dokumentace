#!/usr/bin/env python3
"""
mPohoda API - Generátor faktury
===============================
Generuje JSON strukturu pro vytvoření faktury v mPohoda API.

Použití:
    python generate-invoice.py --partner-id "uuid" --items "Polozka 1,100,2" --output faktura.json
    python generate-invoice.py --partner-id "uuid" --items "Polozka 1,100,2;Polozka 2,50,1" --payment-method "uuid" --bank-account "uuid"
    
Parametry:
    --partner-id         ID odběratele (UUID)
    --items              Položky ve formátu "Nazev,Cena,Mnozstvi;..."
    --payment-method     ID formy úhrady (UUID)
    --bank-account       ID bankovního účtu (UUID)
    --issue-date         Datum vystavení (YYYY-MM-DD, výchozí: dnes)
    --due-date           Datum splatnosti (YYYY-MM-DD, výchozí: +14 dní)
    --text               Text faktury
    --output             Výstupní soubor (výchozí: stdout)
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Any


def parse_items(items_string: str) -> List[Dict[str, Any]]:
    """
    Parsuje položky ze stringu.
    Formát: "Nazev,Cena,Mnozstvi;Nazev2,Cena2,Mnozstvi2"
    """
    items = []
    
    for item_str in items_string.split(';'):
        parts = item_str.strip().split(',')
        
        if len(parts) < 2:
            raise ValueError(f"Neplatný formát položky: {item_str}. Očekáváno: 'Nazev,Cena,Mnozstvi'")
        
        name = parts[0].strip()
        price = float(parts[1].strip())
        quantity = float(parts[2].strip()) if len(parts) > 2 else 1.0
        
        items.append({
            "TextItem": {
                "Text": name,
                "Quantity": quantity,
                "Unit": "ks",
                "UnitPrice": price,
                "UnitPriceType": "WithoutVat",
                "VatRateType": "BasicVatRate"
            }
        })
    
    return items


def generate_invoice(
    partner_id: str,
    items: List[Dict[str, Any]],
    payment_method_id: str = None,
    bank_account_id: str = None,
    issue_date: str = None,
    due_date: str = None,
    text: str = "Faktura za zboží a služby"
) -> Dict[str, Any]:
    """
    Generuje JSON strukturu faktury.
    
    Args:
        partner_id: UUID odběratele
        items: Seznam položek
        payment_method_id: UUID formy úhrady (volitelné)
        bank_account_id: UUID bankovního účtu (volitelné)
        issue_date: Datum vystavení (volitelné, výchozí dnes)
        due_date: Datum splatnosti (volitelné, výchozí +14 dní)
        text: Text faktury
        
    Returns:
        Dict s JSON strukturou faktury
    """
    # Výchozí data
    today = datetime.now()
    issue = datetime.strptime(issue_date, "%Y-%m-%d") if issue_date else today
    due = datetime.strptime(due_date, "%Y-%m-%d") if due_date else (issue + timedelta(days=14))
    
    invoice = {
        "Text": text,
        "IssueDate": issue.strftime("%Y-%m-%d"),
        "DueDate": due.strftime("%Y-%m-%d"),
        "TaxDate": issue.strftime("%Y-%m-%d"),
        "BusinessPartnerAddress": {
            "DocumentAddressWithAddressBookLink": {
                "Id": partner_id
            }
        },
        "Items": items
    }
    
    # Přidání volitelných polí
    if payment_method_id:
        invoice["PaymentMethodId"] = payment_method_id
    
    if bank_account_id:
        invoice["BankAccountId"] = bank_account_id
    
    return invoice


def main():
    parser = argparse.ArgumentParser(
        description='Generátor JSON struktury faktury pro mPohoda API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Příklady:
  # Jednoduchá faktura s jednou položkou
  %(prog)s --partner-id "550e8400-e29b-41d4-a716-446655440000" --items "Polozka 1,1000,2"
  
  # Faktura s více položkami a úhradou
  %(prog)s --partner-id "550e8400-e29b-41d4-a716-446655440000" \\
    --items "Zidle,2500,4;Stul,4500,1" \\
    --payment-method "e9001046-a210-49fe-bb5d-ee463b88ca9d" \\
    --bank-account "b61898b3-3ed1-4cb5-b099-475ea32d79fe"
  
  # Faktura s vlastními daty
  %(prog)s --partner-id "550e8400-e29b-41d4-a716-446655440000" \\
    --items "Sluzba,5000,1" \\
    --issue-date "2024-01-15" \\
    --due-date "2024-01-29" \\
    --text "Faktura za konzultace" \\
    --output faktura.json
        """
    )
    
    parser.add_argument('--partner-id', '-p', required=True,
                        help='ID odběratele (UUID)')
    parser.add_argument('--items', '-i', required=True,
                        help='Položky: "Nazev,Cena,Mnozstvi;Nazev2,Cena2,Mnozstvi2"')
    parser.add_argument('--payment-method', '-pm',
                        help='ID formy úhrady (UUID)')
    parser.add_argument('--bank-account', '-ba',
                        help='ID bankovního účtu (UUID)')
    parser.add_argument('--issue-date',
                        help='Datum vystavení (YYYY-MM-DD, výchozí: dnes)')
    parser.add_argument('--due-date',
                        help='Datum splatnosti (YYYY-MM-DD, výchozí: +14 dní)')
    parser.add_argument('--text', '-t', default="Faktura za zboží a služby",
                        help='Text faktury')
    parser.add_argument('--output', '-o',
                        help='Výstupní soubor (výchozí: stdout)')
    parser.add_argument('--pretty', action='store_true', default=True,
                        help='Formátovaný JSON výstup')
    
    args = parser.parse_args()
    
    try:
        # Parsování položek
        items = parse_items(args.items)
        
        # Generování faktury
        invoice = generate_invoice(
            partner_id=args.partner_id,
            items=items,
            payment_method_id=args.payment_method,
            bank_account_id=args.bank_account,
            issue_date=args.issue_date,
            due_date=args.due_date,
            text=args.text
        )
        
        # Formátování JSON
        indent = 2 if args.pretty else None
        json_output = json.dumps(invoice, ensure_ascii=False, indent=indent)
        
        # Výstup
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"✅ Faktura uložena do: {args.output}")
        else:
            print(json_output)
        
        # Statistika
        total = sum(
            item.get("TextItem", {}).get("UnitPrice", 0) * 
            item.get("TextItem", {}).get("Quantity", 1)
            for item in items
        )
        print(f"\n📊 Přehled faktury:")
        print(f"   Počet položek: {len(items)}")
        print(f"   Celková částka (bez DPH): {total:.2f} Kč")
        print(f"   Datum vystavení: {invoice['IssueDate']}")
        print(f"   Datum splatnosti: {invoice['DueDate']}")
        
    except ValueError as e:
        print(f"❌ Chyba: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Neočekávaná chyba: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
