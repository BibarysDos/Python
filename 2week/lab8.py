def add(bank_account, a):
    bank_account += a
    return bank_account


def sub(bank_account, a):
    bank_account -= a
    return bank_account


def change(money, ex_form, ex_to):
    match ex_form, ex_to:
        case 'USD', 'KZT':
            return money * 470
        case 'KZT', 'USD':
            return money/470
