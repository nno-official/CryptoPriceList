# 🚀 CryptoPriceList

A beautiful, automated cryptocurrency price tracker that displays live prices with trends, charts, and percentage changes directly in your README using GitHub Actions.

## Features

- 🚀 **Automated Updates**: Prices updated every 5-6 minutes using GitHub Actions
- 📊 **Enhanced Table**: Beautiful table with trends, 24h changes, and status indicators
- 📈 **Visual Trends**: Emoji indicators showing price movements and market status
- 🎯 **Smart Status**: HOT/COLD indicators based on price performance
- 💰 **Live Display**: Real-time prices shown directly in your repository README
- 🔧 **Customizable**: Easy to modify which cryptocurrencies to track
- 📱 **Mobile Friendly**: Responsive table design that works on all devices
- 🆓 **Free to Use**: No API keys required, runs entirely on GitHub

## Tracked Cryptocurrencies

- Bitcoin (BTC)
- Ethereum (ETH)
- Litecoin (LTC)
- Solana (SOL)
- Cardano (ADA)

<!-- PRICE_TABLE_START -->

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

<tr>
<td><strong>Bitcoin</strong></td>
<td align="right"><code>$108,235</code></td>
<td align="right" style="color: #ff0000"><strong>-3.75%</strong></td>
<td align="center">📉</td>
<td align="center">❄️ COLD</td>
</tr>

<tr>
<td><strong>Ethereum</strong></td>
<td align="right"><code>$4,336</code></td>
<td align="right" style="color: #ff0000"><strong>-3.40%</strong></td>
<td align="center">📉</td>
<td align="center">❄️ COLD</td>
</tr>

<tr>
<td><strong>Litecoin</strong></td>
<td align="right"><code>$109.03</code></td>
<td align="right" style="color: #ff0000"><strong>-3.15%</strong></td>
<td align="center">📉</td>
<td align="center">❄️ COLD</td>
</tr>

<tr>
<td><strong>Solana</strong></td>
<td align="right"><code>$202.60</code></td>
<td align="right" style="color: #ff0000"><strong>-4.74%</strong></td>
<td align="center">📉</td>
<td align="center">❄️ COLD</td>
</tr>

<tr>
<td><strong>Cardano</strong></td>
<td align="right"><code>$0.8134</code></td>
<td align="right" style="color: #ff0000"><strong>-4.84%</strong></td>
<td align="center">📉</td>
<td align="center">❄️ COLD</td>
</tr>

</tbody>
</table>

---

**📊 Market Summary:** 5/5 coins tracked | **📈 Avg 24h Change:** -3.98%  
**🕐 Last Updated:** 2025-08-29 19:09 UTC | **🔄 Auto-updates every ~5 minutes**

*Data provided by [CoinGecko API](https://www.coingecko.com/en/api) 🦎*

</div>

<!-- PRICE_TABLE_END -->

## 🚀 Quick Start - Fork This Repository

### Step 1: Fork the Repository

1. **Click the "Fork" button** at the top right of this repository
2. **Choose your GitHub account** as the destination
3. **Wait for the fork to complete** - you now have your own copy!

### Step 2: Enable GitHub Actions (IMPORTANT!)

⚠️ **This step is crucial for automatic price updates**

1. Go to **your forked repository** (not this one)
2. Click on the **"Actions" tab**
3. Click **"I understand my workflows, go ahead and enable them"**
4. The automation will start working immediately!

### Step 3: Verify It's Working

1. Go to the **"Actions" tab** in your fork
2. You should see the **"Update Crypto Prices"** workflow
3. Click on a completed workflow run to view the logs
4. If you see formatted price data in the logs, congratulations! 🎉

### Step 4: Customize Your Tracker (Optional)

**Want to track different cryptocurrencies?**

1. Edit the `update_prices.py` file in your fork
2. Find the `COIN_IDS` list (around line 6)
3. Replace with your preferred coins from [CoinGecko's list](https://api.coingecko.com/api/v3/coins/list)
4. Save and commit - GitHub Actions will handle the rest!

**Example customization:**

```python
COIN_IDS = ['bitcoin', 'ethereum', 'dogecoin', 'chainlink', 'polygon']
```

### Step 5: Manual Monitoring (Optional)

**Want to update prices immediately?**

1. Go to **Actions** → **"Update Crypto Prices"**
2. Click **"Run workflow"** → **"Run workflow"**
3. Wait for completion - your README will be updated with fresh prices!

---

## 🛠️ Troubleshooting

**Workflow not running?**

- ✅ Check if GitHub Actions are enabled
- ✅ Look for error messages in the Actions tab
- ✅ Verify the workflow completed successfully
- ✅ Check if the price table appears in your README

**Want to add more coins?**

- ✅ Use exact coin IDs from [CoinGecko API](https://api.coingecko.com/api/v3/coins/list)
- ✅ Keep the format: `['coin1', 'coin2', 'coin3']`

## How It Works

1. **GitHub Actions Workflow**: Runs automatically every 5-6 minutes
2. **API Call**: Fetches latest prices and 24h change data from CoinGecko
3. **Enhanced Processing**: Generates beautiful table with trends and status indicators
4. **README Update**: Automatically updates the price table in your README
5. **Price History**: Maintains recent price history for trend analysis
6. **Auto Commit**: Commits changes with timestamped messages

## Requirements

- No API keys needed
- No local setup required (runs on GitHub)
- Python 3.8+ (handled by GitHub Actions)

## 💻 Local Development

**Want to run this locally or contribute?**

```bash
# Clone your forked repository
git clone https://github.com/yourusername/CryptoPriceList.git
cd CryptoPriceList

# Install dependencies
pip install -r requirements.txt

# Run the script manually
python update_prices.py
```

**For development:**

- The script will display enhanced prices in your terminal AND update README.md
- Test your changes locally before pushing to GitHub
- GitHub Actions will run the price updates once you push changes
- Local runs will create/update `price_history.json` for trend analysis

## 📁 File Structure

```
CryptoPriceList/
├── .github/
│   └── workflows/
│       └── update_prices.yml    # 🤖 GitHub Actions automation
├── update_prices.py             # 🐍 Enhanced price tracker script
├── requirements.txt             # 📦 Python dependencies
├── price_history.json           # 📊 Price history for trend analysis
├── README.md                    # 📖 Documentation with live price table
└── LICENSE                      # ⚖️ MIT License
```

**Key Files:**

- `update_prices.py` - Enhanced script that fetches prices, generates beautiful table, and updates README
- `requirements.txt` - Lists Python dependencies (just `requests`)
- `.github/workflows/update_prices.yml` - Automates the price updates and commits changes
- `price_history.json` - Stores recent price history for trend analysis (auto-generated)
- `README.md` - Project documentation with live-updating enhanced price table

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [CoinGecko API](https://www.coingecko.com/en/api) for providing free cryptocurrency data
- GitHub Actions for free automation

---
