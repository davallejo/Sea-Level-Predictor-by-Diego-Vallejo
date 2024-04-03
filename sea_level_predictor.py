#sea_level_predictor.py
#Autor: Diego Armando Vallejo Vinueza

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Generate some example data for testing
  years = np.arange(1880, 2014)
  sea_levels = np.sin(
      (years - 1880) / 100) * 3 + np.random.normal(0, 0.1, len(years))

  fig, ax = plt.subplots()
  ax.scatter(years, sea_levels, label='Data Points', color='blue')

  # Fit a polynomial of degree 3 to the data
  coeffs = np.polyfit(years - 1880, sea_levels, 3)
  fit = np.polyval(coeffs, years - 1880)
  ax.plot(years, fit, label='Polynomial Fit', color='red')

  ax.set_title("Rise in Sea Level")
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
  ax.set_xticks(np.arange(1850, 2100, 25))

  plt.legend()
  plt.savefig('sea_level_plot.png')  # Save the plot as a PNG file
  plt.show()

  return ax
