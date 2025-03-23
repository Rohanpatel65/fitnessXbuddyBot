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

    message = (
        "💪 Let's get you moving! Stretching is key for flexibility, reducing stiffness, and improving circulation. "
        "Try these **essential stretches** for a full-body refresh:\n\n"
        "✅ **Neck Rolls** – Gently roll your neck in circles to relieve tension.\n"
        "✅ **Shoulder Rolls** – Loosen tight shoulders and improve posture.\n"
        "✅ **Arm Circles** – Increase shoulder mobility and warm up your upper body.\n"
        "✅ **Side Stretch** – Stretch your obliques and improve flexibility.\n"
        "✅ **Cat-Cow Stretch** – A great way to warm up and mobilize your spine.\n"
        "✅ **Seated Forward Bend** – Stretch your lower back and hamstrings.\n"
        "✅ **Quad Stretch** – Improve flexibility in your thighs and hips.\n"
        "✅ **Butterfly Stretch** – Open up your hips and stretch your inner thighs.\n"
        "✅ **Leg Swings** – Boost hip mobility and warm up your legs.\n"
        "✅ **Child’s Pose** – Relax and stretch your lower back and shoulders.\n\n"
        "Take deep breaths while stretching, hold each pose for 15-30 seconds, and enjoy the benefits! 🚀"
    )
    
    return jsonify({"fulfillmentText": message})

# ✅ Run Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
