import json

from channels.generic.websocket import AsyncWebsocketConsumer


class PostNotifyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        # self.user = self.scope["user"]
        # self.room_group_name = f'post_notification_{self.scope["user"].id}'
        #
        # await self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )

        await self.accept()

    async def disconnect(self, close_code):
        print('disconected')
        # Leave room group
        # await self.channel_layer.group_discard(
        #     self.room_group_name,
        #     self.channel_name
        # )

    # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     count = text_data_json['count']
    #
    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message,
    #             'count':count
    #         }
    #     )
    #
    #
    # async def send_notification(self, event):
    #     message = event['message']
    #     count = event['count']
    #
    #     await self.send(text_data=json.dumps({
    #         'message': message,
    #         'count': count,
    #     }))

