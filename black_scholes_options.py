import math

def calc_call_price(S, K, r, q, T, sigma):
    """calc the price of a European call option using BSF."""
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)

def calc_put_price(S, K, r, q, T, sigma):
    """calc the price of a European put option using BSF."""
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)

def norm_cdf(x):
    """normalcdf ptsd"""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def main():
    while True:
        print("\nWhat would you like to calculate?")
        print("1. Call option price")
        print("2. Put option price")
        print("3. Arbitrage opportunity")
        print("4. Spread calculation")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            S = float(input("Enter the current stock price: "))
            K = float(input("Enter the option strike price: "))
            r = float(input("Enter the risk-free interest rate: "))
            q = float(input("Enter the dividend yield: "))
            T = float(input("Enter the time to expiration (in years): "))
            sigma = float(input("Enter the stock volatility: "))
            price = calc_call_price(S, K, r, q, T, sigma)
            print(f"The price of the call option is {price:.2f}")
        
        elif choice == "2":
            S = float(input("Enter the current stock price: "))
            K = float(input("Enter the option strike price: "))
            r = float(input("Enter the risk-free interest rate: "))
            q = float(input("Enter the dividend yield: "))
            T = float(input("Enter the time to expiration (in years): "))
            sigma = float(input("Enter the stock volatility: "))
            price = calc_put_price(S, K, r, q, T, sigma)
            print(f"The price of the put option is {price:.2f}")
        
        elif choice == "3":
            # TODO: Implement arbitrage opportunity calculation
            print("Arbitrage opportunity calculation is not yet implemented.")
        
        elif choice == "4":
            # TODO: Implement spread calculation
            print("Spread calculation is not yet implemented.")
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
