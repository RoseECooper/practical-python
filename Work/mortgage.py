# mortgage.py
#
# Exercise 1.7
principal=500000.0
rate=0.05
payment=2684.11
total_paid=0.0
month=0

extra_payment_start_month=61
extra_payment_end_month=108
extra_payment=1000

while principal>0:
    month=month+1
    principal=principal*(1+rate/12)-payment
    total_paid=total_paid+payment

    if month>=extra_payment_start_month and month<=extra_payment_end_month:
        principal=principal-extra_payment
        total_paid=total_paid+extra_payment

    if 0<principal<payment:
        final_payment=payment-principal
        total_paid=total_paid+final_payment

    #print('Months repaying:', month, 'Principal amount remaining:', round(principal,2), 'Total paid to date:', round(total_paid,2))
    print(f'{round(total_paid,2):<10} | {round(principal,2):<10} | {month:<10}')

print(f'Paid a total of {round(total_paid,2)} over {month} months')