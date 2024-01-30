import json
from datetime import datetime

import pika
from PySide6.QtCore import QObject, Signal
from pika.exceptions import AMQPError

from utils import UserConnection


class NotificationReceiver(QObject):
    got_message = Signal()

    def __init__(self, parent=None, mq_connection_object: pika.BlockingConnection = None,
                 session_object: UserConnection = None):
        super().__init__(parent)
        self.channel_broker = mq_connection_object.channel()
        self.session_object = session_object
        self.channel_broker.basic_consume(queue=f"{self.session_object.email}_msgchannel",
                                          auto_ack=True,
                                          on_message_callback=self.callback)
        self.message = None

    def callback(self, ch, method, properties, body):
        raw_message = str(body.decode("utf-8"))
        json_acceptable_string = raw_message
        message_dict = json.loads(json_acceptable_string)
        ids_list = [notification['ntfcn_id'] for notification in self.session_object.notifications]
        if message_dict['ntfcn_id'] not in ids_list:
            self.session_object.notifications.append(message_dict)
            self.session_object.api.set_message_received(message_dict['ntfcn_id'])
            self.message = message_dict
            self.got_message.emit()

    def start_broker_loop(self):
        try:
            self.channel_broker.start_consuming()
        except AMQPError:
            pass

    def stop_broker_loop(self):
        try:
            self.channel_broker.stop_consuming()
        except AssertionError:
            pass


class NotificationTypes:
    DOC_FOLDER_CHANGE = 'DOC_FOLDER_CHANGE'
    NEW_PROJECT_INVITATION = 'NEW_PROJECT_INVITATION'
    FOLDER_ADDED = 'FOLDER_ADDED'
    FOLDER_REMOVED = 'FOLDER_REMOVED'
    FOLDER_RENAMED = 'FOLDER_RENAMED'
    DOC_ADDED = 'DOC_ADDED'
    DOC_REMOVED = 'DOC_REMOVED'


class Notification:
    Types = NotificationTypes

    def __init__(self, ntfcn_type: NotificationTypes = None, project_id=None,
                 doc_id=None, sender_id=None, receiver_id=None, comments=None, time_limit=None, text=None,
                 window_object=None, doc_type=None, place_id_list=None, receiver_channel=None):
        self.ntfcn_type = ntfcn_type
        self.project_id = project_id
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.time_send = datetime.now().strftime("%m-%d-%Y %H:%M")
        self.comments = comments
        self.text = text
        self.place_id_list = place_id_list
        self.time_limit = time_limit
        self.receiver_channel = receiver_channel

        if self.ntfcn_type == Notification.Types.DOC_FOLDER_CHANGE:
            self.time_limit = None
            self.comments = None

        self.window_object = window_object

    def send(self):
        data = {"receiver_id": self.receiver_id,
                "project_id": self.project_id,
                "doc_id": self.doc_id,
                "sender_id": self.sender_id,
                "ntfcn_type": self.ntfcn_type,
                "comments": self.comments,
                "time_send": self.time_send,
                "time_limit": self.time_limit,
                "msg_text": self.text,
                "doc_type": self.doc_type,
                "place_id": self.place_id_list,
                "receiver_channel": self.receiver_channel}
        self.window_object.session.api.send_message(data)
