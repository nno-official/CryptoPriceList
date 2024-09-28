import requests
from datetime import datetime

def fetch_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,litecoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad status
    return response.json()

def update_readme(prices):
    with open('README.md', 'r') as file:
        lines = file.readlines()

    # Locate the line with the prices table
    for i, line in enumerate(lines):
        if line.strip().startswith('| Bitcoin') and 'Ethereum' in line and 'Litecoin' in line:
            # The next line is the separator (| ------- | ...)
            # The line after that is the price row
            price_line_index = i + 2
            new_price_line = f"| ${prices['bitcoin']['usd']} | ${prices['ethereum']['usd']} | ${prices['litecoin']['usd']} |\n"
            lines[price_line_index] = new_price_line

            # Update the timestamp
            timestamp_index = i + 3  # Assuming the timestamp is on the line after the price
            current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
            if timestamp_index < len(lines) and lines[timestamp_index].startswith('**Last Updated**'):
                lines[timestamp_index] = f"**Last Updated:** {current_time}\n"
            else:
                lines.insert(timestamp_index, f"**Last Updated:** {current_time}\n")

            break
    else:
        # If the table is not found, append it at the end
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
        lines.append("\n## Crypto Prices\n")
        lines.append("| Bitcoin | Ethereum | Litecoin |\n")
        lines.append("| ------- | -------- | -------- |\n")
        new_price_line = f"| ${prices['bitcoin']['usd']} | ${prices['ethereum']['usd']} | ${prices['litecoin']['usd']} |\n"
        lines.append(new_price_line)
        lines.append(f"**Last Updated:** {current_time}\n")

    with open('README.md', 'w') as file:
        file.writelines(lines)

def main():
    try:
        prices = fetch_crypto_prices()
        update_readme(prices)
        print(f"Updated prices: Bitcoin=${prices['bitcoin']['usd']}, Ethereum=${prices['ethereum']['usd']}, Litecoin=${prices['litecoin']['usd']}")
    except Exception as e:
        print(f"Error updating prices: {e}")

if __name__ == '__main__':
    main()
