from flask import Flask, request, jsonify

app = Flask(__name__)

# return student number
@app.route("/", methods=["GET"])
def home():
    return jsonify({"student_number": "200590360"}) 


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)

    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    #  Response
    if intent_name == "Stretching Exercises":
        response_text = (
            "💪 **Here are some great stretching exercises!**\n\n"
            "**🟢 Pre-workout Stretches:**\n"
            "• Arm Circles - Loosens shoulders\n"
            "• Leg Swings - Improves hip mobility\n"
            "• High Knees - Warms up legs\n\n"
            "**🔵 Post-workout Stretches:**\n"
            "• Hamstring Stretch - Relaxes leg muscles\n"
            "• Shoulder Stretch - Relieves tension\n"
            "• Child’s Pose - Stretches lower back\n\n"
            "**🟠 Desk Stretches (For Office Workers):**\n"
            "• Neck Rolls - Reduces stiffness\n"
            "• Seated Spinal Twist - Relaxes back muscles\n"
            "• Wrist Stretches - Helps with typing strain\n\n"
            "👉 Want a video guide? Check this out: [Stretching Video](https://www.youtube.com/watch?v=4BOTvaRaDjI) 🎥"
        )
    else:
        response_text = "Sorry, I don't have information on that."

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
