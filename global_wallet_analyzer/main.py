from requests import get
from json import load

class ExchangeRateProvider:
    def __init__(self):
        url = 'http://api.nbp.pl/api/exchangerates/tables/A?format=json'
        response = get(url)
        self.data = response.json()

    def get_rate(self, currency_code: str):
        for info in self.data[0]['rates']:
            if info['code'] == currency_code:
                return info['mid']

        return None

class DataManager:
    def __init__(self):
        with open('baskets.json') as file:
            self.open_file = load(file)

class ReportGenerator:
    def __init__(self, data_manager, exchange_report):
        self.data_manager = data_manager
        self.exchange_report = exchange_report
        self.currency_dict = {}

    def get_currency(self):
        for _ in self.data_manager.open_file:
            wallet = _['currency']
            for currency_name, amount in wallet.items():
                self.currency_dict[currency_name] = self.currency_dict.get(currency_name, 0) + amount

        return self.currency_dict

class FinalReport(ReportGenerator):
    def __init__(self, data_manager, exchange_report):
        super().__init__(data_manager, exchange_report)

    def final_inventory(self):
        if not self.currency_dict:
            self.get_currency()

        print('Portfolio assets: ')

        for currency, amount in self.currency_dict.items():
            print(f'{currency.upper()}: {amount:.2f}')

    def final_valuation(self, show_details=True):

        if not self.currency_dict:
            self.get_currency()

        total_pln = 0

        if show_details:
            print('Value of assets in PLN: \n')

        for currency, amount in self.currency_dict.items():
            if currency.lower() == 'pln':
                total_pln += amount
            else:
                rate = self.exchange_report.get_rate(currency.upper())

                if rate is not None:
                    current_value = amount * rate
                    total_pln += current_value
                    if show_details:
                        print(f'{self.currency_dict["eur"]} {currency.upper()} -> {current_value:.2f} PLN (rate: {rate})\n')
                else:
                    if show_details:
                        print(f'{currency.upper()}: {amount}: Exchange rate not found')

        return total_pln

    def impact_analysis(self):
        total_wealth = self.final_valuation(show_details=False)

        print('Percentage currency allocation in the portfolio. \n')

        if total_wealth == 0:
            print('Your portfolio is empty.')
            return

        for currency, amount in self.currency_dict.items():
            if currency.lower() == 'pln':
                current_pln_value = amount
            else:
                rate = self.exchange_report.get_rate(currency.upper())
                current_pln_value = amount * rate if rate else 0

            percentage = (current_pln_value / total_wealth) * 100

            print(f'{currency}: {percentage:.2f}')



my_data = DataManager()
my_rate = ExchangeRateProvider()
my_report = ReportGenerator(data_manager=my_data, exchange_report=my_rate)
final = FinalReport(data_manager=my_data, exchange_report=my_rate)

final.final_inventory()
print("\n" + "="*40 + "\n")
final.final_valuation(show_details=True)
print("\n" + "="*40 + "\n")
final.impact_analysis()