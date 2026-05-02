from flask import Flask, request, jsonify, render_template, send_file
from model import predict_intent, get_response

app = Flask(__name__)

# 🏠 Home route (loads UI)
@app.route("/")
def home():
    return render_template("index.html")


# 📄 PDF download route (for fees)
@app.route("/get-fee-pdf")
def get_fee_pdf():
    return send_file("document_loaders/BTech_2025_2026.pdf", as_attachment=True)


# 💬 Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    tag, confidence = predict_intent(user_input)

    # 🔍 Debug (optional, remove later)
    print("User:", user_input)
    print("Tag:", tag)
    print("Confidence:", confidence)

    # 🔥 VERY LOW CONFIDENCE → fallback
    if confidence < 0.3:
        response = "Sorry, I didn't understand. Try asking about admission, fees, courses, routine, notices, login, etc."

    # 🔥 Fees → send PDF link
    elif tag == "fees":
        response = "You can download the fee structure here: http://127.0.0.1:5000/get-fee-pdf"

    # 🔥 Normal intent-based response
    else:
        response = get_response(tag)

    return jsonify({"response": response})


# ▶ Run app
if __name__ == "__main__":
    app.run(debug=True)