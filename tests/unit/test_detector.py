import pytest
from src.vision.detector import ObjectDetector

def test_detector_initialization():
    detector = ObjectDetector()
    assert detector.camera is None

def test_detect_objects_empty():
    detector = ObjectDetector()
    frame = None  # Mock frame
    objects = detector.detect_objects(frame)
    assert isinstance(objects, list)
    assert len(objects) == 0
