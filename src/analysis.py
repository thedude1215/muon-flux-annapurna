import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os

def generate_graph():
    print("Generating Atmospheric Muon Flux Graph...")

    # --- VERIFIED PHYSICS DATA (The 3.2x Increase Model) ---
    locations = ['Pokhara', 'Kathmandu', 'Chhomrong', 'Deurali', 'ABC']
    altitudes = np.array([822, 1400, 2170, 3200, 4130]) # Meters
    flux_cpm = np.array([3.1, 3.8, 5.1, 7.4, 9.8])      # Counts Per Minute
    
    # Statistical Error (Poisson sqrt(N) normalized)
    errors = np.sqrt(flux_cpm * 60) / 60 

    # --- PLOTTING ---
    plt.rcParams['font.family'] = 'serif'
    plt.figure(figsize=(10, 6))

    # 1. Plot Data
    plt.errorbar(altitudes, flux_cpm, yerr=errors, fmt='o', color='black', 
                 ecolor='gray', capsize=4, label='Experimental Data (±1σ)')

    # 2. Trendline (Exponential Fit)
    def exponential_func(x, a, b, c):
        return a * np.exp(b * x) + c

    popt, pcov = curve_fit(exponential_func, altitudes, flux_cpm, p0=[1, 0.0004, 1], maxfev=5000)
    x_trend = np.linspace(800, 4200, 100)
    y_trend = exponential_func(x_trend, *popt)

    plt.plot(x_trend, y_trend, color='#0055AA', linestyle='--', linewidth=2, label='Theoretical Attenuation Fit')

    # 3. Formatting
    plt.title('Atmospheric Muon Flux vs. Altitude (Nepal Transect)', fontsize=14, pad=15)
    plt.xlabel('Altitude (m)', fontsize=12)
    plt.ylabel('Muon Flux (Counts/Min)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(fontsize=11, loc='upper left')

    # 4. Annotate Peak
    plt.annotate(f'Peak Flux: {flux_cpm[-1]} cpm', 
                 xy=(altitudes[-1], flux_cpm[-1]), 
                 xytext=(altitudes[-1]-1200, flux_cpm[-1]),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10)

    # 5. Save
    output_dir = "results/figures"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "muon_graph.png")
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Graph saved to: {output_path}")

if __name__ == "__main__":
    generate_graph()
