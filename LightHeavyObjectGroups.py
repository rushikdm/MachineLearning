from enum import Enum

class ObjectGroup(Enum):
    LIGHT = 1
    HEAVY = 2

def train(light_objects, heavy_objects, model_parameter):
    wl = 0
    wh = 10e6
    for obj in light_objects:
        if wl < obj:
            wl = obj
    for obj in heavy_objects:
        if obj < wh:
            wh = obj
    model_parameter = (wl + wh) / 2.0

def execute(weight, model_parameter):
    if(weight <= model_parameter):
        return ObjectGroup.LIGHT
    return ObjectGroup.HEAVY

