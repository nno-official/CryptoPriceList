from datetime import timezone, datetime
import requests


def fetch_crypto_prices():
    """
        Fetches the crypto prices and returns results in json

    Args:
        None

    Returns:
        dict: Return values in json of the api.
    """
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,litecoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # Raise an error for bad status
    return response.json()

def update_readme(prices):
    """    Updates readme.md file with newly fetched prices

    Args:
        prices (dict): The dictionary of fetched prices

    Returns:
        None
    """
        
    with open('README.md', 'r', encoding='utf-8') as file:
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
            current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
            for index, line in enumerate(lines):
                if line.startswith("**Last Updated:**"):
                    lines[index] = f"**Last Updated:** {current_time}\n"
                    break

            break
    else:
        # If the table is not found, append it at the end
        current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        lines.append("\n## Crypto Prices\n")
        lines.append("| Bitcoin | Ethereum | Litecoin |\n")
        lines.append("| ------- | -------- | -------- |\n")
        new_price_line = f"| ${prices['bitcoin']['usd']} | ${prices['ethereum']['usd']} | ${prices['litecoin']['usd']} |\n"
        lines.append(new_price_line)
        lines.append(f"**Last Updated:** {current_time}\n")

    with open('README.md', 'w', encoding="utf-8") as file:
        file.writelines(lines)
    return

def main():
    try:
        prices = fetch_crypto_prices()
        update_readme(prices)
        print(f"Updated prices: Bitcoin=${prices['bitcoin']['usd']}, Ethereum=${prices['ethereum']['usd']}, Litecoin=${prices['litecoin']['usd']}")
    except Exception as e:
        print(f"Error updating prices: {e}")

if __name__ == '__main__':
    main()
