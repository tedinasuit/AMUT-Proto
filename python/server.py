from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess  # Add this line to import subprocess

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5500")

prompt_list = []

@app.route('/add_prompt', methods=['POST'])
def add_prompt():
    data = request.get_json()
    prompt = data.get('prompt')
    prompt_list.append(prompt)
    return jsonify(success=True)

@app.route('/run_script', methods=['GET'])
def run_script():
    # Replace this command with the actual command to run your Python script
    subprocess.run(['python', 'AMUT_workflow_SDXLTurbo.py'])
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
