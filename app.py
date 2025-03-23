from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def base_route():
    student_id = "200590360"  
    return jsonify({"student_number": student_id})

# ✅ Webhook for Dialogflow Fulfillment
@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    
    # Extract parameters (if any)
    params = req.get("queryResult", {}).get("parameters", {})
    
    # Get intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "stretching exercises":
        message = "💪 Try these stretches: Arm Circles, Leg Swings, and Child’s Pose."
    else:
        message = "Sorry, I don't have information on that."

    return jsonify({"fulfillmentText": message})

# ✅ Run Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
