import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_csv(filename):
    # Read the CSV file
    df = pd.read_csv(filename)
    
    # Ensure there are at least two columns
    if df.shape[1] < 2:
        print("Error: CSV file must have at least two columns.")
        return
    
    # Extract the first two columns
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    
    # Compute the first and second derivatives
    dy_dx = np.gradient(y, x)
    d2y_dx2 = np.gradient(dy_dx, x)
    
    # Plot the original data
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='.', markersize=3, linestyle='-', label='Original Data')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title("CSV Data Plot")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Plot the first derivative
    plt.figure(figsize=(8, 5))
    plt.plot(x, dy_dx, marker='.', markersize=3, linestyle='--', label='First Derivative')
    plt.xlabel(df.columns[0])
    plt.ylabel(f"d({df.columns[1]})/d({df.columns[0]})")
    plt.title("First Derivative Plot")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Plot the second derivative
    plt.figure(figsize=(8, 5))
    plt.plot(x, d2y_dx2, marker='.', markersize=3, linestyle='-.', label='Second Derivative')
    plt.xlabel(df.columns[0])
    plt.ylabel(f"d²({df.columns[1]})/d({df.columns[0]})²")
    plt.title("Second Derivative Plot")
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    filename = input("Enter the CSV file path: ")
    plot_csv(filename)
