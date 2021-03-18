
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os

SECURE_CONNECT_BUNDLE = './secure-connect-mlb-data.zip'
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')


class Connection:
    def __init__(self):
        self.secure_connect_bundle = SECURE_CONNECT_BUNDLE
        self.cloud_config = {
            'secure_connect_bundle': self.secure_connect_bundle
        }
        self.auth_provider = PlainTextAuthProvider(client_id, client_secret)
        self.cluster = Cluster(cloud=self.cloud_config,
                               auth_provider=self.auth_provider)
        self.session = self.cluster.connect()

    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()
