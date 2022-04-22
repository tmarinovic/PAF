import numpy as np
import matplotlib.pyplot as plt
import math
import pd_zadatak_1 as pd

objekt1 = pd.projectileDrop()
objekt1.init(30, 20)
objekt1.promjena_visine(-5)
objekt1.promjena_brzine(-5)
objekt1.reset()

print("")

objekt2 = pd.projectileDrop()
objekt2.init(40, 30)
objekt2.promjena_visine(5)
objekt2.promjena_brzine(5)
objekt2.reset()
print("")