import torch
from models.common import DetectMultiBackend

def load_model():
    model = DetectMultiBackend('yolov5s.pt') 
    return model