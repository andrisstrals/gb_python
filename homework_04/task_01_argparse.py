import argparse


def salary_calc(hours, rate, bonus):
    return hours * rate + bonus

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Salary calculator')
    parser.add_argument('-hours', required=True, help='Working hours logged', type=float)
    parser.add_argument('-rate', required=True, help='Hourly pay rate', type=float)
    parser.add_argument('-bonus', default=0.0, help='Additional bonus', type=float)

    args = parser.parse_args()

    print(f'Calculate salary: {salary_calc(args.hours, args.rate, args.bonus)}')