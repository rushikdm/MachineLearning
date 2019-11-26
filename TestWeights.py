from WeightClassifier import WeightClassifier
from WeightClassifier import WeightType

heavy_objects = [10, 11, 10.5, 10.5]
light_objects = [1, 1.2, 2.5, 2.25, 3.2]

wc = WeightClassifier()
wc.train(light_objects, heavy_objects)

print("w = ", wc.w)

print("12 class = ", wc.classify(12))
print("2.5 class = ", wc.classify(2.5))
