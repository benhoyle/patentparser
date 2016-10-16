# -*- coding: utf-8 -*-
import json
import os
import sys
import time
from flask import Flask, Response, request

from patentparser.core import Claim

#[=========================== Server Setup ================================]
# Set current module location (for opening test json file)
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
# Add custom path for epo-ops module (set as environment variable)
# see http://conda.pydata.org/docs/using/envs.html#saved-environment-variables
custom_path = os.environ.get("CUSTOM_PATH")
sys.path.append(custom_path)
import epo_ops

# Get client key and secret for OPS login from environment variables
consumer_key = os.environ.get('C_KEY')
consumer_secret = os.environ.get('C_SECRET')

#[=========================== Server Setup END =============================]

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/numbersearch/<number>', methods=['GET'])
def number_search(number):
    """ Perform a search on EPO OPS and return claim 1. """
    # Setup a new registered EPO OPS client that returns JSON
    registered_client = epo_ops.RegisteredClient(
        key=consumer_key, 
        secret=consumer_secret, 
        accept_type='json')
    claims = registered_client.published_claims(number)
    return json.dumps(claims)


# Need to change and configure this
@app.route('/api/claimdata/<number>', methods=['GET', 'POST'])
def claim_handler(number):
    """ Perform a search on EPO OPS and return claim 1. """
    # Setup a new registered EPO OPS client that returns JSON
    registered_client = epo_ops.RegisteredClient(
        key=consumer_key, 
        secret=consumer_secret, 
        accept_type='json')
    claims = registered_client.published_claims(number)
    #Add data cleansing here
    claim = Claim(claims[0])
    #print(number)
    #claim = ""

    if request.method == 'POST':
        pass
        #new_claimdata = request.form.to_dict()
        #new_claimdata['id'] = int(time.time() * 1000)
        #claimdata.append(new_claimdata)

        #with open('claimdata.json', 'w') as f:
            #f.write(json.dumps(claimdata, indent=4, separators=(',', ': ')))

    return Response(
        json.dumps(claim.json()),
        #json.dumps("test"),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )

def main():
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)

if __name__ == '__main__':
    main()