import numpy as np
import scipy.stats as si

S = float(input("Enter the current stock price: "))
K = float(input("Enter the option strike price: "))
r = float(input("Enter the risk-free interest rate: "))
t = float(input("Enter the time to maturity (in years): "))
sigma = float(input("Enter the volatility: "))
N = int(input("Enter the number of simulations: "))
option_type = input("Enter the option type (call or put): ")

# mc sim
def monte_carlo_simulation(S, K, r, t, sigma, N, option_type):
    dt = t / 365.0
    S_sim = np.zeros((N, 1))
    for i in range(N):
        S_sim[i] = S * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.normal())
    if option_type == "call":
        payoff = np.maximum(S_sim - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - S_sim, 0)
    else:
        print("Invalid option type")
        return None
    discount_factor = np.exp(-r * t)
    option_price = discount_factor * np.mean(payoff)
    return option_price

# bs form
# https://www.quantconnect.com/tutorials/introduction-to-options/black-scholes-merton-formula
# TODO: try to make this more readable
def black_scholes_formula(S, K, r, t, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    if option_type == "call":
        option_price = S * si.norm.cdf(d1) - K * np.exp(-r * t) * si.norm.cdf(d2)
    elif option_type == "put":
        option_price = K * np.exp(-r * t) * si.norm.cdf(-d2) - S * si.norm.cdf(-d1)
    else:
        print("Invalid option type")
        return None
    return option_price

monte_carlo_price = monte_carlo_simulation(S, K, r, t, sigma, N, option_type)
black_scholes_price = black_scholes_formula(S, K, r, t, sigma, option_type)

print("Monte Carlo price: ", monte_carlo_price)
print("Black-Scholes price: ", black_scholes_price)
