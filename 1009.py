# @Jbj Zeehad

sellers_name = input()
fixed_salary = float(input())
sales_per_month = float(input())
total = format(((sales_per_month * 0.15) + fixed_salary), "0.2f")
print("TOTAL = R$ " + str(total))
