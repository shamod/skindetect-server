from fastai import *
from fastai.vision import *
import os
import matplotlib.pyplot as plt

path = ('/home/craig/Final_Files/')

learner = load_learner(path, 'export2')

img = ('/home/craig/Downloads/moles/melanoma.jpeg')


plt.show(y=learner.predict(img)[0])
