from flask import Flask, render_template, request, jsonify
import requests, base64, json, os

app = Flask(__name__)

# --- Config ---
API_KEY = os.getenv("API_KEY")  # set this in Render → Environment tab
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# --- Gemini API ---
def generate_response(prompt_text, image_b64):
    if not prompt_text.strip():
        prompt_text = "Describe this image clearly in one short sentence."

    body = {
        "contents": [
            {
                "parts": [
                    {"text": (
                        "You are an AI describing images for visually impaired users.\n"
                        "Describe the image in 1 short, clear sentence.\n"
                        "Avoid markdown, symbols, or commentary.\n"
                        f"User prompt: {prompt_text}"
                    )},
                    {"inline_data": {"mime_type": "image/jpeg", "data": image_b64}}
                ]
            }
        ]
    }

    response = requests.post(
        ENDPOINT, headers={"Content-Type": "application/json"}, data=json.dumps(body)
    )

    if response.status_code == 200:
        data = response.json()
        text = (
            data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
        )
        return text or "No description found."
    else:
        return f"Error: {response.status_code} - {response.text}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    prompt = request.form.get('prompt', '')
    image_data = request.form.get('image', '')

    # Extract base64 part (remove data:image/jpeg;base64, prefix)
    if "," in image_data:
        image_data = image_data.split(",")[1]

    result = generate_response(prompt, image_data)
    return jsonify({'response': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
