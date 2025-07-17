# Step 2: Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def chatbot():
    print("Welcome to CryptoBuddy! Ask me about cryptocurrencies.")
    while True:
        user_query = input("You: ").lower()

        if "exit" in user_query:
            print("CryptoBuddy: Goodbye! Remember, always research before investing!")
            break

        # Step 3 & 4: Chatbot Logic & Advice Rules
        if "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
        
        elif "trending" in user_query or "rising" in user_query:
            # Prioritize coins with price_trend = "rising" and market_cap = "high"
            rising_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
            if rising_coins:
                print(f"CryptoBuddy: {rising_coins[0]} is trending up and has a strong market cap! 🚀")
            else:
                print("CryptoBuddy: No top trending coins found right now.")
        
        elif "buy" in user_query or "growth" in user_query:
            # Recommend coin with rising price and high sustainability
            best_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["sustainability_score"] > 0.5]
            if best_coins:
                print(f"CryptoBuddy: {best_coins[0]} is trending up and has a top-tier sustainability score! 🚀")
            else:
                print("CryptoBuddy: Consider doing more research, no top picks currently.")
        
        else:
            print("CryptoBuddy: Sorry, I didn’t understand that. Try asking about sustainability or trending coins.")

if __name__ == "__main__":
    chatbot()
