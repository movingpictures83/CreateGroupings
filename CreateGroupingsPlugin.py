# Create random grouping to ensure that differential analysis is accuratee

import pandas as pd
import numpy as np

np.random.seed(7272)

class CreateGroupingsPlugin:
    def input(self, inputfile):
       self.samples_annotations = inputfile
    def run(self):
       pass
    def output(self, outputfile):
       df = pd.read_csv(self.samples_annotations)
       df['random'] = np.random.randint(0, 2, df.shape[0])

       df.to_csv(outputfile, index=False)
       print(df)
