import requests
from datetime import datetime
from pathlib import Path

# --- Configuration ---
COIN_IDS = ['bitcoin', 'ethereum', 'litecoin', 'solana', 'cardano']
README_FILE = Path("README.md")
START_MARKER = ""
END_MARKER = ""

def fetch_crypto_prices(coin_ids):
    """Fetches prices for a list of cryptocurrencies from CoinGecko."""
    print(f"Fetching prices for: {', '.join(coin_ids)}")
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(coin_ids),
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices from API: {e}")
        return None

def generate_price_table(prices, coin_ids):
    """Generates a Markdown table from the price data."""
    if not prices:
        return ""

    # Create the header
    header = "| " + " | ".join([coin.capitalize() for coin in coin_ids]) + " |"
    separator = "| " + " | ".join(["-------"] * len(coin_ids)) + " |"

    # Create the price row, handling missing data gracefully
    price_cells = []
    for coin in coin_ids:
        price = prices.get(coin, {}).get('usd')
        price_cells.append(f"${price:,.2f}" if price else "N/A")
    price_row = "| " + " | ".join(price_cells) + " |"
    
    # Get the timestamp
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    timestamp = f"\n**Last Updated:** {current_time}"

    return "\n".join([header, separator, price_row, timestamp])

def update_readme(table_content):
    """Updates the README.md file with the new table."""
    try:
        content = README_FILE.read_text()
        
        # Find the markers
        start_index = content.find(START_MARKER)
        end_index = content.find(END_MARKER)

        if start_index == -1 or end_index == -1:
            print("Error: Could not find the markers in README.md. Please add them.")
            return

        # Build the new README content
        new_content = (
            content[:start_index + len(START_MARKER)] +
            "\n" +
            table_content +
            "\n" +
            content[end_index:]
        )

        README_FILE.write_text(new_content)
        print("README.md updated successfully.")

    except FileNotFoundError:
        print(f"Error: {README_FILE} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the script."""
    prices = fetch_crypto_prices(COIN_IDS)
    if prices:
        price_table = generate_price_table(prices, COIN_IDS)
        if price_table:
            update_readme(price_table)

if __name__ == '__main__':
    main()
