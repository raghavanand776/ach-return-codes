# ach-return-codes

[![tests](https://github.com/raghavanand776/ach-return-codes/actions/workflows/tests.yml/badge.svg)](https://github.com/raghavanand776/ach-return-codes/actions/workflows/tests.yml)

A small command-line bot that explains **ACH return codes** in plain English: what the code means, whether you can retry, the return window, and a customer-friendly message. Built for support and payment-ops teams at fintechs.

## Example
```
code> R01
R01: Insufficient Funds
  What it means:  The account didn't have enough money to cover the debit.
  Can you retry?  Yes: up to 2 more times, within 180 days of the original settlement date
  Return window:  2 banking days
  Tell customer:  "Your payment didn't go through because of insufficient funds. We'll try again soon."
```

## Run it
```bash
python3 ach.py          # interactive: type R01, 'list' or 'quit'
python3 ach.py r10      # one-shot lookup (input is case-insensitive)
python3 -m pytest -v    # 5 tests, including a guard on the retry rule
```

## Covered codes
R01–R11, R16, R20 and R29: the most common returns in consumer and business ACH.

## Notes
- Only **R01** and **R09** (insufficient or uncollected funds) may be re-presented without new authorization, up to 2 more times within 180 days. A test enforces this.
- Unauthorized returns (R05, R07, R10, R11) have a **60-day** window; most others are **2 banking days**.
- Educational reference, not legal or compliance advice. Check the current Nacha Operating Rules for production use.