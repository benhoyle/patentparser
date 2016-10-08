import json
import os
import time
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

# Need to change and configure this
@app.route('/api/claimdata', methods=['GET', 'POST'])
def claim_handler():
    with open('claimdata.json', 'r') as f:
        claimdata = json.loads(f.read())

    if request.method == 'POST':
        new_claimdata = request.form.to_dict()
        new_claimdata['id'] = int(time.time() * 1000)
        claimdata.append(new_claimdata)

        with open('claimdata.json', 'w') as f:
            f.write(json.dumps(claimdata, indent=4, separators=(',', ': ')))

    return Response(
        json.dumps(claimdata),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)