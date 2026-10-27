import unittest
from modules.sentiment_escalation.analyzer import analyze_sentiment, check_escalation

class TestSentimentEscalation(unittest.TestCase):
    
    def test_sarcasm_detection(self):
        # Simulating a hidden evaluation case
        message = "Oh great, my account got locked again. Fantastic service."
        result = analyze_sentiment(message, history=[])
        self.assertEqual(result["sentiment"], "sarcastic")
        
    def test_after_hours_high_risk(self):
        # Simulating an after-hours account compromise complaint
        is_after_hours = True
        sentiment = {"sentiment": "urgent"}
        escalation = check_escalation(sentiment, history=[], is_after_hours=is_after_hours)
        
        self.assertTrue(escalation["escalate"])
        self.assertEqual(escalation["queue"], "on-call")