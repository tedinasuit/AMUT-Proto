from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5500")

latest_prompt = ""

@app.route('/add_prompt', methods=['POST'])
def add_prompt():
    global latest_prompt
    data = request.get_json()
    latest_prompt = data.get('prompt')
    return jsonify(success=True)

@app.route('/run_script', methods=['GET'])
def run_script():
    global latest_prompt
    # Replace this command with the actual command to run your Python script
    subprocess.run(['python', 'AMUT_workflow_SDXLTurbo.py', latest_prompt])
    return jsonify(success=True)

@app.route('/delete_files', methods=['POST'])
def delete_files():
    try:
        folder_path = "../ComfyUI_windows_portable/ComfyUI/output/"
        # Iterate over files in the folder and delete them
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

        return jsonify({'success': True, 'message': 'Files deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
