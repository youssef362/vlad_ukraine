from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)
HEADERS={'Content-Type': 'application/json'}
BOT_WEBHOOK='https://admin.chatme.ai/connector/webim/webim_message/5e764f5d23e421f465c334899ed1229e/bot_api_webhook'
WEBHOOK_SITE='https://webhook.site/b03c80bf-6ae0-4222-bd81-4725376b81a8'

@app.route('/conversation/<user_id>/message', methods=['post'])
def get_bot_answer(user_id):
    incomingdata=request.json
    print('indata=', incomingdata)
    print('indatazero=', incomingdata[0]['payload']['message'])   
    bot_response = requests.request("POST", BOT_WEBHOOK, headers=HEADERS, json={'event': 'new_message', 'chat': {'id': user_id},'text': incomingdata[0]['payload']['message']})
    whs = requests.request("POST", WEBHOOK_SITE, headers=HEADERS, json={'event': 'new_message', 'chat': {'id': user_id},'text': incomingdata[0]['payload']['message']})
    
    print('bot_response= ', bot_response.content)
    json_bot_response = json.loads(bot_response.content.decode('utf-8'))
    print('json_bot_response_type = ', type(json_bot_response))
    print('json_bot_response= ', json_bot_response)
    print('json_bot_response_messages= ', json_bot_response['messages'])
    print('json_bot_response_messages_text= ', json_bot_response['messages'][0]['text'])
    ###payload = {'type': 'text', 'message': json_bot_response['messages'][0]['text']}
   ### resp = {[{'type': 'text', 'payload': payload}]} 
    resp = ([{'type': 'text', 'payload': {'type': 'text', 'message': json_bot_response['messages'][0]['text']}}])
    return resp 

if __name__ == '__main__':
    app.run()
