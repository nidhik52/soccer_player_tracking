import cv2
import numpy as np
from collections import deque

class Player:
    def __init__(self, id, bbox, frame_id, crop, feature=None):
        self.id = id
        self.bbox = bbox
        self.last_seen = frame_id
        self.crop = crop
        self.feature = feature

    def update(self, bbox, frame_id, crop, feature=None):
        self.bbox = bbox
        self.last_seen = frame_id
        self.crop = crop
        if feature is not None:
            self.feature = feature

def iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA) * max(0, yB - yA)
    if interArea == 0:
        return 0.0
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    return interArea / float(boxAArea + boxBArea - interArea)

def compare_players(p1, p2):
    return iou(p1.bbox, p2.bbox)

