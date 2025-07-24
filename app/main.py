from flask import Flask, request, jsonify, redirect
from app import models, utils

app = Flask(__name__)

BASE_URL = "http://localhost:5000"


@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })


@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })


@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field in JSON body"}), 400

    original_url = data['url'].strip()

    if not utils.is_valid_url(original_url):
        return jsonify({"error": "Invalid URL format. Must start with http:// or https://"}), 400


    for _ in range(5):
        short_code = utils.generate_shortcode()
        if not models.get_url(short_code):
            break
    else:
        return jsonify({"error": "Failed to generate unique shortcode"}), 500

    models.add_url(short_code, original_url)

    return jsonify({
        "short_code": short_code,
        "short_url": f"{BASE_URL}/{short_code}"
    }), 201


@app.route('/<short_code>')
def redirect_short_url(short_code):
    original_url = models.get_url(short_code)
    if not original_url:
        print("URL resolved:", original_url)
        return jsonify({"error": "Short code not found"}), 404

    models.increment_click(short_code)
    return redirect(original_url, code=302)


@app.route('/api/stats/<short_code>')
def stats(short_code):
    data = models.get_stats(short_code)
    if not data:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
