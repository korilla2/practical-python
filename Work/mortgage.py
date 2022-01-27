# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
count = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    count += 1
    if extra_payment_start_month <= count <= extra_payment_end_month:
        payment = 3684.11
    else:
        payment = 2684.11

    if principal >= payment:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
    else:
        total_paid = total_paid + principal
        principal = 0

    print('Total paid', f'{round(total_paid, 2):,}', end='\n')
    print('Principal', principal, end='\n')
    print('Months', count)
