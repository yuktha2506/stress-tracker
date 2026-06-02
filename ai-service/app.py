import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from textblob import TextBlob
import numpy as np

load_dotenv()

app = Flask(__name__)
CORS(app)

MOOD_MAP = {
    "great": 1,
    "happy": 2,
    "calm": 3,
    "neutral": 5,
    "tired": 6,
    "anxious": 8,
    "sad": 8,
    "overwhelmed": 9,
    "burned out": 10,
}


def build_demo_model():
    # Synthetic seed data keeps the service runnable before real company data exists.
    x = np.array([
        [2, 8, 6, 2, 2],
        [4, 7, 8, 4, 4],
        [5, 6, 9, 5, 6],
        [7, 5, 10, 8, 8],
        [9, 4, 12, 9, 9],
        [3, 8, 7, 3, 3],
        [8, 5, 11, 8, 10],
        [6, 6, 9, 6, 7],
    ])
    y = np.array(["LOW", "LOW", "MEDIUM", "HIGH", "HIGH", "LOW", "HIGH", "MEDIUM"])
    return Pipeline([
        ("scale", StandardScaler()),
        ("model", RandomForestClassifier(n_estimators=80, random_state=42)),
    ]).fit(x, y)


MODEL = build_demo_model()


def mood_to_score(mood):
    if isinstance(mood, (int, float)):
        return float(mood)
    return MOOD_MAP.get(str(mood).lower().strip(), 5)


def recommendation(risk_level, payload, sentiment_score=0):
    stress = float(payload.get("stress_level", 5))
    sleep = float(payload.get("sleep_hours", 7))
    work = float(payload.get("work_hours", 8))
    if risk_level == "HIGH":
        return "High burnout risk detected. Recommend a manager check-in, workload reprioritization, no-meeting recovery block, and sleep recovery plan."
    if work > 9 or stress > 6:
        return "Moderate risk detected. Move one low-priority task, take a focused break, and cap work hours today."
    if sleep < 6 or sentiment_score < -0.2:
        return "Recovery signal is soft. Prioritize rest, hydration, and a lighter task queue."
    return "Low risk. Maintain steady routines, short breaks, and healthy boundaries."


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "stress-tracker-ai"})


@app.post("/predict")
def predict():
    payload = request.get_json(force=True)
    features = np.array([[
        float(payload.get("stress_level", 5)),
        float(payload.get("sleep_hours", 7)),
        float(payload.get("work_hours", 8)),
        mood_to_score(payload.get("mood", "neutral")),
        float(payload.get("deadline_pressure", 5)),
    ]])

    risk_level = MODEL.predict(features)[0]
    probabilities = dict(zip(MODEL.classes_, MODEL.predict_proba(features)[0]))
    burnout_score = round(
        min(100, max(0, features[0][0] * 8 + features[0][2] * 3 + features[0][4] * 5 - features[0][1] * 4)),
        1,
    )
    notes = payload.get("notes", "")
    sentiment_score = TextBlob(notes).sentiment.polarity if notes else 0

    return jsonify({
        "risk_level": risk_level,
        "burnout_score": burnout_score,
        "confidence": round(float(probabilities.get(risk_level, 0)), 2),
        "sentiment": {
            "score": round(sentiment_score, 3),
            "label": "POSITIVE" if sentiment_score > 0.1 else "NEGATIVE" if sentiment_score < -0.1 else "NEUTRAL",
        },
        "recommendation": recommendation(risk_level, payload, sentiment_score),
    })


@app.post("/sentiment")
def sentiment():
    text = request.get_json(force=True).get("text", "")
    score = TextBlob(text).sentiment.polarity
    return jsonify({
        "score": round(score, 3),
        "label": "POSITIVE" if score > 0.1 else "NEGATIVE" if score < -0.1 else "NEUTRAL",
    })


@app.post("/recommendations")
def recommendations():
    payload = request.get_json(force=True)
    risk = payload.get("risk_level", "MEDIUM")
    return jsonify({
        "items": [
            recommendation(risk, payload),
            "Use a 25-minute focus sprint followed by a 5-minute recovery break.",
            "Share deadline pressure early so HR or managers can rebalance work."
        ]
    })


@app.post("/weekly-report")
def weekly_report():
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "title": "AI-generated weekly wellness report",
        "summary": "Stress was highest mid-week, driven by deadline pressure and extended work hours. Recovery improved where employees had fewer meetings and better sleep.",
        "actions": [
            "Reduce meeting density for high-pressure teams.",
            "Identify employees with repeated high stress and low sleep.",
            "Send break and recovery reminders during peak workload windows."
        ],
        "input_size": len(payload.get("logs", []))
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 7000)), debug=os.getenv("FLASK_ENV") == "development")
