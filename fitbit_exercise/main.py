import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from utils import *


def format_date(date):
    """
    Format a YYYY-MM-DD date into a DD/MM/YYYY date
    """
    return f"{date[8:10]}/{date[5:7]}/{date[0:4]}"


# read data from csv file in the same directory
dir = os.path.dirname(__file__)


df = pd.read_csv(os.path.join(dir, 'data\data.csv'))

df["time"] = df["time"].apply(func=format_date)

# configure the plot's style
plt.style.use('classic')


df.plot(x="time", y="TotalSteps", kind="bar",
        color="blue", label="TotalSteps", figsize=(190, 13))

plt.savefig(os.path.join(dir, 'data\TotalSteps.png'))
