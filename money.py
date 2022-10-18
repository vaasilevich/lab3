from datetime import datetime as dt
from datetime import timedelta


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.today()
        else:
            self.date = dt.strptime(date, '%d.%m.%Y')


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.today()
        self.week_ago = self.today - timedelta(7)

    def add_record (self, record):
        self.records.append(record)

    def get_today_stats (self):
        day_stats = 0
        for record in self.records:
            if record.date == self.today:
                day_stats += record.amount
        return day_stats

    def get_week_stats(self):
        week_stats = 0
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats += record.amount
        return week_stats

    def get_today_limit_balance(self):
        current_balance = self.limit - self.get_today_stats()
        return current_balance


class CashCalculator(Calculator):
    USD_RATE = 61.76
    EUR_RATE = 60.56
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE),
                      'eur': ('EURO', CashCalculator.EUR_RATE)}
        name, rate = currencies[currency]
        cash_remained = round(self.get_today_limit_balance() / rate, 2)
        if cash_remained == 0:
            print('Денег нет!')
        elif cash_remained > 0:
            print(f'У вас ещё есть:  {cash_remained} {name}  на сегодня')
        else:
            print(f'Денег нет, ваш долг: {abs(cash_remained)} {name}!')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.get_today_limit_balance()
        if calories_remained > 0:
            print('Сегодня можно съесть еще что-нибудь, но общей 'f'калорийностью не более {calories_remained} калорий')
        else:
            print('Хватит есть!')


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=200, comment="Сендвич с кофе"))
cash_calculator.add_record(Record(amount=350, comment="Обед в столовой"))
cash_calculator.add_record(Record(amount=500, comment="Ужин в кафе", date="18.10.2022"))
cash_calculator.get_today_cash_remained("rub")

calories_calculator = CaloriesCalculator(1500)
calories_calculator.add_record(Record(amount=300, comment="Завтрак"))
calories_calculator.add_record(Record(amount=650, comment="Обед"))
calories_calculator.add_record(Record(amount=800, comment="Ужин", date="18.10.2022"))
calories_calculator.get_calories_remained()