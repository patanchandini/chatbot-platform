import unittest
from modules.sentiment_escalation.analyzer import analyze_sentiment, check_escalation

class TestSentimentEscalation(unittest.TestCase):
    
    def test_sarcasm_detection(self):
        # Hidden Evaluation: Sarcasm
        message = "Oh great, my account got locked again. Fantastic service."
        result = analyze_sentiment(message, history=[])
        self.assertEqual(result["sentiment"], "sarcastic")
        
    def test_after_hours_high_risk(self):
        # Hidden Evaluation: After-hours requests & calm high-risk
        is_after_hours = True
        sentiment = {"sentiment": "calm"} 
        # Even if calm, account compromise should escalate
        escalation = check_escalation(sentiment, history=[{"issue": "account compromise"}], is_after_hours=is_after_hours)
        self.assertTrue(escalation["escalate"])
        self.assertEqual(escalation["queue"], "on-call")
