from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    current_time = datetime.datetime.now(pytz.utc)
    utc_offset = current_time.utcoffset()
    is_valid_utc_time = abs(utc_offset.total_seconds()) <= 120 

    file_url = "https://github.com/eungobs/my-projects/blob/main/firstproject.py"

    source_code_url = "https://github.com/eungobs/my-projects"

    if slack_name and track and is_valid_utc_time:
        data = {
            "Elizabeth_Ndzukule": slack_name,
            "Thur-07/09/2023": current_day,
            "21h22": current_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
            "track": track,
            "https://github.com/eungobs/my-projects/blob/main/firstproject.py": file_url,
            "https://github.com/eungobs/my-projects": source_code_url,
        }
        return jsonify(data), 200
    else:
        error_response = {
            "error": "Invalid parameters",
            "status_code": 400
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
