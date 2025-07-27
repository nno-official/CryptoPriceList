import requests
from datetime import datetime
from pathlib import Path
import json
import os

# --- Configuration ---
COIN_IDS = ['bitcoin', 'ethereum', 'litecoin', 'solana', 'cardano']
README_FILE = 'README.md'
START_MARKER = '<!-- PRICE_TABLE_START -->'
END_MARKER = '<!-- PRICE_TABLE_END -->'
PRICE_HISTORY_FILE = 'price_history.json'

def fetch_crypto_prices(coin_ids):
    """Fetches prices and 24h change data for cryptocurrencies from CoinGecko."""
    print(f"Fetching prices for: {', '.join(coin_ids)}")
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(coin_ids),
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices from API: {e}")
        return None



def load_price_history():
    """Load previous price data for trend calculation."""
    if os.path.exists(PRICE_HISTORY_FILE):
        try:
            with open(PRICE_HISTORY_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

def save_price_history(prices):
    """Save current prices to history file."""
    history = load_price_history()
    timestamp = datetime.utcnow().isoformat()
    
    for coin, data in prices.items():
        if coin not in history:
            history[coin] = []
        
        # Keep only last 10 entries to avoid file bloat
        if len(history[coin]) >= 10:
            history[coin] = history[coin][-9:]
        
        history[coin].append({
            'timestamp': timestamp,
            'price': data.get('usd', 0),
            'change_24h': data.get('usd_24h_change', 0)
        })
    
    with open(PRICE_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def get_trend_indicator(change_24h):
    """Get trend indicator based on 24h change."""
    if change_24h > 5:
        return "🚀", "#00ff00"  # Strong up
    elif change_24h > 0:
        return "📈", "#90EE90"  # Up
    elif change_24h > -5:
        return "📉", "#FFB6C1"  # Down
    else:
        return "💥", "#ff0000"  # Strong down

def generate_enhanced_table(prices, coin_ids):
    """Generate an enhanced HTML table with trends and styling."""
    if not prices:
        return "<p>❌ No price data available</p>"
    
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    
    # Table header with enhanced styling
    table_html = f"""
<div align="center">

### 💰 Live Cryptocurrency Prices

<table>
<thead>
<tr>
<th align="left">🪙 Cryptocurrency</th>
<th align="right">💵 Price (USD)</th>
<th align="right">📊 24h Change</th>
<th align="center">📈 Trend</th>
<th align="center">🎯 Status</th>
</tr>
</thead>
<tbody>
"""
    
    for coin in coin_ids:
        coin_data = prices.get(coin, {})
        price = coin_data.get('usd')
        change_24h = coin_data.get('usd_24h_change', 0)
        
        # Format coin name
        coin_name = coin.replace('-', ' ').title()
        
        if price:
            # Format price with appropriate precision
            if price >= 1000:
                price_str = f"${price:,.0f}"
            elif price >= 1:
                price_str = f"${price:,.2f}"
            else:
                price_str = f"${price:.4f}"
            
            # Format 24h change
            change_str = f"{change_24h:+.2f}%" if change_24h else "0.00%"
            change_color = "#00ff00" if change_24h > 0 else "#ff0000" if change_24h < 0 else "#888888"
            
            # Get trend indicator
            trend_emoji, trend_color = get_trend_indicator(change_24h)
            
            # Status indicator
            if change_24h > 2:
                status = "🔥 HOT"
            elif change_24h > 0:
                status = "✅ UP"
            elif change_24h > -2:
                status = "⚡ STABLE"
            else:
                status = "❄️ COLD"
            
            table_html += f"""
<tr>
<td><strong>{coin_name}</strong></td>
<td align="right"><code>{price_str}</code></td>
<td align="right" style="color: {change_color}"><strong>{change_str}</strong></td>
<td align="center">{trend_emoji}</td>
<td align="center">{status}</td>
</tr>
"""
        else:
            table_html += f"""
<tr>
<td><strong>{coin_name}</strong></td>
<td align="right"><code>N/A</code></td>
<td align="right">--</td>
<td align="center">❓</td>
<td align="center">⚠️ ERROR</td>
</tr>
"""
    
    # Table footer with timestamp and stats
    total_coins = len([c for c in coin_ids if prices.get(c, {}).get('usd')])
    avg_change = sum([prices.get(c, {}).get('usd_24h_change', 0) for c in coin_ids if prices.get(c, {}).get('usd_24h_change')]) / max(1, total_coins)
    
    table_html += f"""
</tbody>
</table>

---

**📊 Market Summary:** {total_coins}/{len(coin_ids)} coins tracked | **📈 Avg 24h Change:** {avg_change:+.2f}%  
**🕐 Last Updated:** {current_time} | **🔄 Auto-updates every ~5 minutes**

*Data provided by [CoinGecko API](https://www.coingecko.com/en/api) 🦎*

</div>
"""
    
    return table_html

def update_readme(table_content):
    """Update README.md with the new price table."""
    try:
        with open(README_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find markers
        start_index = content.find(START_MARKER)
        end_index = content.find(END_MARKER)
        
        if start_index == -1 or end_index == -1:
            print(f"Error: Could not find markers {START_MARKER} and {END_MARKER} in {README_FILE}")
            return False
        
        # Replace content between markers
        new_content = (
            content[:start_index + len(START_MARKER)] + 
            "\n" + table_content + "\n" +
            content[end_index:]
        )
        
        with open(README_FILE, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"✅ Successfully updated {README_FILE} with enhanced price table")
        return True
        
    except FileNotFoundError:
        print(f"Error: {README_FILE} not found")
        return False
    except Exception as e:
        print(f"Error updating {README_FILE}: {e}")
        return False

def display_prices(prices, coin_ids):
    """Display current cryptocurrency prices to console."""
    if not prices:
        print("No price data available.")
        return
    
    print("\n" + "="*60)
    print("🚀 ENHANCED CRYPTOCURRENCY PRICE TRACKER 🚀")
    print("="*60)
    
    for coin in coin_ids:
        coin_data = prices.get(coin, {})
        price = coin_data.get('usd')
        change_24h = coin_data.get('usd_24h_change', 0)
        coin_name = coin.replace('-', ' ').title()
        
        if price:
            trend_emoji, _ = get_trend_indicator(change_24h)
            change_str = f"({change_24h:+.2f}%)"
            print(f"{trend_emoji} {coin_name:<12}: ${price:>10,.2f} {change_str}")
        else:
            print(f"❓ {coin_name:<12}: {'N/A':>10} (--%)")
    
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    print(f"\n🕐 Last Updated: {current_time}")
    print("="*60 + "\n")

def main():
    """Main function to run the script."""
    prices = fetch_crypto_prices(COIN_IDS)
    
    if prices:
        # Save price history for trend analysis
        save_price_history(prices)
        
        # Generate enhanced table
        table_content = generate_enhanced_table(prices, COIN_IDS)
        
        # Update README with the table
        update_readme(table_content)
        
        # Also display to console
        display_prices(prices, COIN_IDS)
    else:
        print("❌ Failed to fetch price data")

if __name__ == '__main__':
    main()
