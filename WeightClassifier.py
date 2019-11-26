from enum import Enum

class WeightType(Enum):
    LIGHT = 1
    HEAVY = 2

class WeightClassifier:

    def __init__(self):
        self.w = 0

    def train(self, light_objects, heavy_objects):
        wl = max(light_objects)
        wh = min(heavy_objects)
        self.w = (wl + wh) / 2.0

    def classify(self, weight):
        if weight <= self.w:
            return WeightType.LIGHT
        return WeightType.HEAVY
