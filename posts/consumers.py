import json

from channels.generic.websocket import AsyncWebsocketConsumer


class PostNotifyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_group_name = f'post_notifications_{self.scope["user"].id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_post_notification',
                'message': message
            }
        )


    async def send_post_notification(self, event):
        message = event['message']
        print(event)
        print(23232332)

        await self.send(text_data=json.dumps({
            'message': message
        }))

