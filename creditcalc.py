#Credit Calculator for annuity loans
import math
import argparse


def check_err(args):
    if args.type == None or args.type != 'diff' and args.type != "annuity":
        return True
    elif args.interest == None:
        return True
    arguments = [args.principal, args.periods, args.interest, args.payment]
    arguments.remove(None)
    if None in arguments:
        return True
    if min(arguments) <0:
        return True
    else:
        return False


def calc_diff(i, n, p):
    # the calculation of differentiated payment.
    # To do this, the user may run the program specifying interest,
    # count of periods and credit principal.
    sum = 0
    for m in range(1,n +1):
        d = math.ceil( p / n + i * (p - p / n * (m - 1) ))
        sum += d
        print(f"Month {m }: paid out {d}")

    print(f"Overpayment = {sum - p}")


def calc_annuity(p, i, n):
    """
    calculate and print annuity payment
    arguments: p, i, n    where:

    p = credit principal,
    i = nominal (monthly) interest rate
    n = number of payments
    """
    x = i * (1+i) ** n
    y = (1 + i) ** n - 1

    result = math.ceil( p * x / y)
    #print( p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your annuity payment = {result}!")
    print(f"Overpayment = {result * n - p}")


def calc_principal(a, i, n):
    """
    calculate and return credit principal
    arguments: a, i, n    where:

    a = annuity payment
    i = nominal (monthly) interest rate
    n = number of payments
    """

    x = i * (1+i) ** n
    y = (1 + i) ** n - 1
    result =round(a / (x / y))

    # print(a / (i * (1 + i) ** n / ((1 + i) ** n - 1)))

    print(f"Your credit principal = {result}!")


def calc_months(a, i, p):
    """
    calculate and return number of payments
    arguments: a, i, p    where:

    a = annuity payment
    i = nominal (monthly) interest rate
    p = credit principal
    """
    x = a / (a - i * p)
    result = math.ceil(math.log(x, (1+i)))
    years = result // 12
    months = result % 12

    if years and months:
        print(f"You need {years} years and {result % 12} months to repay this credit!")
    elif years:
        print(f"You need {years} years to repay this credit!")
    elif months == 1:
        print(f"You need 1 month to repay this credit!")
    else:
        print(f"You need {result % 12} months to repay this credit!")

    print(f"Overpayment = {result * a - p}")


# argparse block
parser = argparse.ArgumentParser(description="Credit Calculator for annuity loans")
parser.add_argument("-t", "--type", type=str, choices=["diff", "annuity"],
                    help="choose between differential or annuity loan")
parser.add_argument("-p", "--principal", type=int,
                    help="Enter principal")
parser.add_argument("-n", "--periods", type=int,
                    help="Enter number of payments (months)")
parser.add_argument("-i", "--interest", type=float,
                    help="Annual interest rate")
parser.add_argument("-a", "--payment", type=float,
                    help="Monthly payments")


args = parser.parse_args()

#Errorchecking
debug = True
errors = check_err(args)


if not errors:
    i = args.interest / 1200

    if args.type == "diff":
        calc_diff(i, args.periods, args.principal)

    elif not args.periods:
        calc_months(args.payment, i, args.principal)

    elif not args.payment:
        calc_annuity(args.principal,i, args.periods)

    elif not args.principal:
        calc_principal(args.payment, i, args.periods)

else:
    print("Incorrect parameters")

