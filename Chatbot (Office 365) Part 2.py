from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods = ['POST'])
def webhook():
    data = request.get_json()
    intent = data['nlp']['intents'][0]['slug'] # Extract the intent
    response = generate_response(intent) 
    return jsonify({'response' : response})

def generate_response(intent):
    if intent == 'access document':
        return 'You need to access Office 365 documents within the MCC sharepoint and navigate to the documents within files.'
    else:
        return 'I am sorry I am unable to help with that'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

    