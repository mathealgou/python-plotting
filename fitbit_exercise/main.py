import pandas as pd
import os
import matplotlib.pyplot as plt
from utils import *

# read data from csv file in the same directory
dir = os.path.dirname(__file__)


df = pd.read_csv(os.path.join(dir, 'data\data.csv'))
# configure the plot's style
plt.style.use('classic')

df.plot(x="time", y="TotalSteps", kind="line",
        color="blue", label="TotalSteps", figsize=(90, 5))

plt.savefig(os.path.join(dir, 'data\TotalSteps.png'))
