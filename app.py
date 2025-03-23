from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"student_number": "200590360"})  

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True, silent=True)
    print("Received request:", req)  # Debugging log

    # Get intent name from Dialogflow request
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "Stretching Exercises":
        response_text = "💪 Try these stretches: Arm Circles, Leg Swings, and Child’s Pose."
    else:
        response_text = "Sorry, I don't have information on that."

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
