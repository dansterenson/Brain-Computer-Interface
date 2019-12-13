from datetime import datetime
import struct


_HEADER_FORMAT = 'QQI'


class Thought:

    def __init__(self, user_id, timestamp, thought):
        self.user_id = user_id
        self.timestamp = timestamp
        self.thought = thought

    def __repr__(self):
        return f'Thought(user_id={self.user_id!r}, timestamp={self.timestamp!r}, thought={self.thought!r})'

    def __str__(self):
        time = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return f'[{time}] user {self.user_id}: {self.thought}'

    def __eq__(self, other):
        if id(self) == id(other):
            return True
        if not isinstance(other, Thought):
            return False
        if self.user_id != other.user_id or self.thought != other.thought or self.timestamp != other.timestamp:
            return False
        return True

    def serialize(self):
        converted = self.thought.encode("utf-8")
        return struct.pack(f'{_HEADER_FORMAT}%ds' % len(self.thought), self.user_id, int(self.timestamp.timestamp()),
               len(self.thought), converted)

    @classmethod
    def deserialize(cls, data):
        user_id, time, size = struct.unpack(_HEADER_FORMAT, data[:20])
        timestamp = datetime.fromtimestamp(time)
        encoded = struct.unpack("<%ds" % size, data[20:])
        thought = encoded[0].decode("utf-8")
        return Thought(user_id, timestamp, thought)
