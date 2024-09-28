import requests
import json

def fetch_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd'
    response = requests.get(url)
    return response.json()

def update_readme(prices):
    with open('README.md', 'r') as file:
        readme_content = file.readlines()

    for i, line in enumerate(readme_content):
        if line.startswith('## Crypto Prices'):
            readme_content[i + 1] = f'| Bitcoin | Ethereum | Litecoin |\n| ------- | -------- | -------- |\n| ${prices["bitcoin"]["usd"]} | ${prices["ethereum"]["usd"]} | ${prices["litecoin"]["usd"]} |\n'

    with open('README.md', 'w') as file:
        file.writelines(readme_content)

def main():
    prices = fetch_crypto_prices()
    update_readme(prices)

if __name__ == '__main__':
    main()
