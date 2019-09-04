from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.session_name = self.scope['url_route']['kwargs']['jam_session_name']
        self.session_group_name = 'jam-session_%s' % self.session_name

        # join session group
        async_to_sync(self.channel_layer.group_add)(
            self.session_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # leave session group
        async_to_sync(self.channel_layer.group_discard)(
            self.session_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.session_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        # send message to websocket
        self.send(text_data=json.dumps({
            'message': message
        }))
