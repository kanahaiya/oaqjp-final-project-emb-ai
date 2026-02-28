from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1=emotion_detector('I am glad this happened')
        #print(result1)
        self.assertEqual(0.83237535, result1['dominant_emotion'][0]['emotion']['joy'])
        result2=emotion_detector('I am glad this happened')
        self.assertEqual(0.01388365, result1['dominant_emotion'][0]['emotion']['anger'])
        result2=emotion_detector('I am glad this happened')
        self.assertEqual(0.00850114, result1['dominant_emotion'][0]['emotion']['disgust'])
        result2=emotion_detector('I am glad this happened')
        self.assertEqual(0.17257097, result1['dominant_emotion'][0]['emotion']['sadness'])
        result2=emotion_detector('I am glad this happened')
        self.assertEqual(0.018487887, result1['dominant_emotion'][0]['emotion']['fear'])


unittest.main()        