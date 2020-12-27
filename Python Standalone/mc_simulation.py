import joblib
from sklearn.ensemble import RandomForestRegressor
import numpy as np


class MCSimulation:
    def __init__(self, inputs, material, distribution, lower, upper, mode):
        modelOptimised = None
        modelRationalised = None
        if (material == "Steel"):
            modelOptimised = joblib.load("models/steel_optimised.joblib")
            modelRationalised = joblib.load("models/steel_rationalised.joblib")
        elif (material == "Reinforced Concrete"):
            modelOptimised = joblib.load("models/concrete_optimised.joblib")
            modelRationalised = joblib.load("models/concrete_rationalised.joblib")
        else:
            modelOptimised = joblib.load("models/glulam_optimised.joblib")
            modelRationalised = modelOptimised
        
        optimised = modelOptimised.predict([inputs])
        rationalised = modelRationalised.predict([inputs])
        
        # In case rationalised is greater than optimised make them equal
        if (optimised > rationalised):
            optimised = rationalised
        
        finalList = []
        
        if (distribution == "Uniform"):
            finalList = np.random.uniform(rationalised, optimised, 5000) * np.random.uniform(lower, upper, 5000)
        elif (distribution == "Gaussian"):
            finalList = np.random.uniform(rationalised, optimised, 5000) * np.random.normal(lower, upper, 5000)
        else:
            finalList = np.random.uniform(rationalised, optimised, 5000) * np.random.triangular(lower, mode, upper, 5000)
        self.finalList = finalList
        
    def getList(self):
        return self.finalList