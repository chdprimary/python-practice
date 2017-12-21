import matplotlib.pyplot as plt

POTENTIAL_HOURS = range(1,41)
HOURLY_PAY = 10
AVG_MEAL_PRICE = 15

def calculate_pay(num_hours, hourly_pay=HOURLY_PAY, avg_meal_price=AVG_MEAL_PRICE, adjusted=False):
    pay = (num_hours * hourly_pay)
    if adjusted:
        pay += (num_hours//4 * avg_meal_price)
    return pay

def print_pay_data(num_hours, unadjusted_pay, adjusted_pay, pretty_print=False):
    if pretty_print:
        print('Working {0} hours:\n'.format(num_hours), 
                '\tUnadjusted pay: ${0:.2f} USD\n'.format(unadjusted_pay[num_hours-1]), 
                '\tAdjusted pay: ${0:.2f} USD\n'.format(adjusted_pay[num_hours-1]), 
                '\tUnadjusted pay/hr: ${0:.2f} USD\n'.format(unadjusted_pay[num_hours-1]/num_hours), 
                '\tAdjusted pay/hr: ${0:.2f} USD'.format(adjusted_pay[num_hours-1]/num_hours)
                )
    else:
        print(num_hours, 
            unadjusted_pay[num_hours-1], 
            adjusted_pay[num_hours-1], 
            unadjusted_pay[num_hours-1]/num_hours, 
            adjusted_pay[num_hours-1]/num_hours
            )

def make_plots(unadjusted_pay, adjusted_pay):
    subplot = plt.figure().add_subplot(111)

    subplot.plot(POTENTIAL_HOURS, 
        unadjusted_pay, 
        'ro-', 
        label='unadjusted pay', 
        linewidth=3)

    subplot.plot(POTENTIAL_HOURS, 
        adjusted_pay, 
        'go-', 
        label='adjusted pay', 
        linewidth=3)

    x_fudge = -0.5
    y_fudge = 8
    for i in POTENTIAL_HOURS:
        subplot.annotate(
            str(unadjusted_pay[i-1]), 
            xy=(i + x_fudge, unadjusted_pay[i-1] + y_fudge)
            )
        subplot.annotate(
            str(adjusted_pay[i-1]), 
            xy=(i + x_fudge, adjusted_pay[i-1] + y_fudge)
            )

    plt.legend()
    return plt

unadjusted_pay = [calculate_pay(num_hours) for num_hours in POTENTIAL_HOURS]
adjusted_pay = [calculate_pay(num_hours, adjusted=True) for num_hours in POTENTIAL_HOURS]

for num_hours in POTENTIAL_HOURS:
    print_pay_data(num_hours, unadjusted_pay, adjusted_pay)

final_plot = make_plots(unadjusted_pay, adjusted_pay)
final_plot.show()