from fastapi import FastAPI
from pydantic import BaseModel
from modules.sentiment_escalation.analyzer import analyze_sentiment, check_escalation
from modules.rag_assistant.retrieval import process_query

app = FastAPI(title="Chatbot Platform API")

# Define the data models for the API requests
class SentimentRequest(BaseModel):
    text: str

class EscalationRequest(BaseModel):
    sentiment: str
    is_after_hours: bool

class QueryRequest(BaseModel):
    query: str

# 1. Endpoint for Sentiment Analysis
@app.post("/analyze-sentiment")
def get_sentiment(request: SentimentRequest):
    return analyze_sentiment(request.text)

# 2. Endpoint for Escalation Routing
@app.post("/check-escalation")
def route_escalation(request: EscalationRequest):
    sentiment_data = {"sentiment": request.sentiment}
    return check_escalation(sentiment_data, is_after_hours=request.is_after_hours)

# 3. Endpoint for RAG/Query
@app.post("/process-query")
def process_user_query(request: QueryRequest):
    return {"response": process_query(request.query)}