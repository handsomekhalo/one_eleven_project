from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_characters():
    data = request.get_json()

    if not data or "data" not in data:
        return jsonify({"error": "Missing data field"}), 400

    input_string = data["data"]

    sorted_chars = sorted(list(input_string))

    return jsonify({
        "word": sorted_chars
    })

if __name__ == '__main__':
    app.run(debug=True)