import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy_detection(self):
        """Test dominant emotion 'joy'"""
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

    def test_anger_detection(self):
        """Test dominant emotion 'anger'"""
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

    def test_disgust_detection(self):
        """Test dominant emotion 'disgust'"""
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

    def test_sadness_detection(self):
        """Test dominant emotion 'sadness'"""
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

    def test_efear_detection(self):
        """Test dominant emotion 'fear'"""
        result_5 = emotion_detector("I am really afraid that will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')


unittest.main()