import json
import os
import time
from flask import Flask, Response, request

# Set current module location (for opening test json file)
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/numbersearch/<number>', methods=['GET'])
def number_search(number):
    """ Perform a search on EPO OPS and return claim 1. """
    pass


# Need to change and configure this
@app.route('/api/claimdata', methods=['GET', 'POST'])
def claim_handler():
    with open(os.path.join(__location__,'claimdata.json'), 'r') as f:
        claimdata = json.loads(f.read())
        # Add consecutive numbered keys for React
        words = [{'id':i, 'word':item['word'], 'pos':item['pos']} for i, item in list(enumerate(claimdata['words']))]

    if request.method == 'POST':
        pass
        #new_claimdata = request.form.to_dict()
        #new_claimdata['id'] = int(time.time() * 1000)
        #claimdata.append(new_claimdata)

        #with open('claimdata.json', 'w') as f:
            #f.write(json.dumps(claimdata, indent=4, separators=(',', ': ')))

    return Response(
        json.dumps({"words":words}),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)