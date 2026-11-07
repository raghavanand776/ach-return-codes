"""
ach-return-codes / codes.py
Author:  Raghav Anand
Created: 2026-11-06

The data: common NACHA ACH return codes, explained in plain English.
Each code maps to a small dictionary of facts a support or ops team needs.
"""

# Reusable answers, so the same rule is worded the same way everywhere.
RETRY_FUNDS = "Yes: up to 2 more times, within 180 days of the original settlement date"
RETRY_NEW_AUTH = "No: only with a new authorization from the customer"
RETRY_NO = "No: fix the account details first"

CODES = {
    "R01": {
        "title": "Insufficient Funds",
        "meaning": "The account didn't have enough money to cover the debit.",
        "retry": RETRY_FUNDS,
        "window": "2 banking days",
        "customer_message": "Your payment didn't go through because of insufficient funds. We'll try again soon.",
    },
    "R02": {
        "title": "Account Closed",
        "meaning": "The customer closed the account.",
        "retry": RETRY_NO,
        "window": "2 banking days",
        "customer_message": "The bank account on file is closed. Please add a new account.",
    },
    "R03": {
        "title": "No Account / Unable to Locate Account",
        "meaning": "The account number doesn't match any account at that bank.",
        "retry": RETRY_NO,
        "window": "2 banking days",
        "customer_message": "We couldn't find that bank account. Please check the account number.",
    },
    "R04": {
        "title": "Invalid Account Number",
        "meaning": "The account number isn't a valid format for that bank.",
        "retry": RETRY_NO,
        "window": "2 banking days",
        "customer_message": "The account number looks incorrect. Please re-enter it.",
    },
    "R05": {
        "title": "Unauthorized Debit to Consumer Account Using Corporate SEC Code",
        "meaning": "A consumer account was debited using a business-only entry type, without the consumer's authorization.",
        "retry": RETRY_NEW_AUTH,
        "window": "60 calendar days",
        "customer_message": "Your bank reported this payment as unauthorized. Please contact us to set it up again.",
    },
    "R06": {
        "title": "Returned per ODFI's Request",
        "meaning": "The sender's own bank asked for the entry back, usually to fix an error.",
        "retry": "Depends: confirm with your bank why it was recalled",
        "window": "Varies",
        "customer_message": "This payment was recalled to correct an error. No action needed from you.",
    },
    "R07": {
        "title": "Authorization Revoked by Customer",
        "meaning": "The customer told their bank they withdrew permission for this debit.",
        "retry": RETRY_NEW_AUTH,
        "window": "60 calendar days",
        "customer_message": "You've revoked authorization for this payment. Contact us if you'd like to restart it.",
    },
    "R08": {
        "title": "Payment Stopped",
        "meaning": "The customer placed a stop payment on this specific debit.",
        "retry": RETRY_NEW_AUTH,
        "window": "2 banking days",
        "customer_message": "A stop payment was placed on this debit. Contact us if this was a mistake.",
    },
    "R09": {
        "title": "Uncollected Funds",
        "meaning": "The balance was there, but the money wasn't available yet (for example, a deposit still on hold).",
        "retry": RETRY_FUNDS,
        "window": "2 banking days",
        "customer_message": "Your funds weren't available yet. We'll try again soon.",
    },
    "R10": {
        "title": "Customer Advises Originator Is Not Known or Not Authorized",
        "meaning": "The customer says they don't recognize the sender or never authorized the debit.",
        "retry": RETRY_NEW_AUTH,
        "window": "60 calendar days",
        "customer_message": "Your bank reported this payment as unauthorized. Please contact us.",
    },
    "R11": {
        "title": "Entry Not in Accordance with the Terms of the Authorization",
        "meaning": "The customer authorized a debit, but this one didn't match what they agreed to (wrong amount or date).",
        "retry": "Yes, once corrected: fix the error and resend within 60 days",
        "window": "60 calendar days",
        "customer_message": "This payment didn't match what you authorized. We're correcting it.",
    },
    "R16": {
        "title": "Account Frozen / Entry Returned per OFAC Instruction",
        "meaning": "The account is frozen, by the bank, legal action or a sanctions instruction.",
        "retry": "No: the account can't be used",
        "window": "2 banking days",
        "customer_message": "Your bank account is currently unavailable. Please add a different account.",
    },
    "R20": {
        "title": "Non-Transaction Account",
        "meaning": "The account type doesn't allow these transactions (for example, some savings accounts).",
        "retry": RETRY_NO,
        "window": "2 banking days",
        "customer_message": "This account type can't be used for payments. Please add a checking account.",
    },
    "R29": {
        "title": "Corporate Customer Advises Not Authorized",
        "meaning": "A business account holder says they didn't authorize the debit.",
        "retry": RETRY_NEW_AUTH,
        "window": "2 banking days",
        "customer_message": "Your business bank reported this payment as unauthorized. Please contact us.",
    },
}