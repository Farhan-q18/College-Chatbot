from flask import Flask, request, jsonify, render_template, send_file
from model import predict_intent, get_response

app = Flask(__name__)

# 🏠 Home route (loads UI)
@app.route("/")
def home():
    return render_template("index.html")


# 📄 PDF route (you can keep it if needed for direct access)
@app.route("/get-fee-pdf")
def get_fee_pdf():
    return send_file("document_loaders/BTech_2025_2026.pdf", as_attachment=True)


# 💬 Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    tag, confidence = predict_intent(user_input)

    # 🔍 Debug (optional)
    print("User:", user_input)
    print("Tag:", tag)
    print("Confidence:", confidence)

    # 🔥 Low confidence fallback
    if confidence < 0.3:
        response = "Sorry, I didn't understand. Try asking about admission, fees, courses, routine, notices, login, etc."

    # 🔥 All responses handled via intents.json
    else:
        response = get_response(tag)

    return jsonify({"response": response})


# ▶ Run app (Render compatible)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)