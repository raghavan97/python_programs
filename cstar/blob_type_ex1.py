import json
import datetime
import pytz
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster

# Running instructions
# docker run -p9042:9042 cassandra
# inside the container
# cqlsh
# CREATE KEYSPACE my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1} ;
# in the virtual env
# pip install cassandra-driver
# python <this program>

class MyConstants():
    my_keyspace = "my_keyspace"
    my_connection = "my_connection"

# This defines the table
class FileModel(Model):
    __keyspace__ = MyConstants.my_keyspace

    # We can specify the connection name associated with this Model
    # __connection__ = MyConstants.my_connection 
    machine = columns.Text(primary_key=True)
    path = columns.Text(primary_key=True)
    meta = columns.Text()
    updated_on = columns.DateTime()
    content = columns.Blob()

    def to_dict(self):
        return dict(
            path=self.path,
            meta=json.loads(self.meta)
        )

# This is one level above the FileModel and manages FileModel objects
class FileServer(object):

    def __init__(self, cass_servers_list):
        cluster = Cluster(cass_servers_list)
        session = cluster.connect(keyspace=MyConstants.my_keyspace)

        # The name of the connection
        connection.register_connection(MyConstants.my_connection, session=session)
        connection.set_default_connection(MyConstants.my_connection)

        # connection.setup(cass_servers_list, "cqlengine", protocol_version=3)
        sync_table(FileModel)

    @classmethod
    def get_model_values(cls, config):
        conf = dict()
        for col in ('path', 'machine', 'meta', 'content'):
            if col in config:
                conf[col] = config[col]
        
        return conf

    @classmethod
    def insert(cls, **config):
        conf = cls.get_model_values(config)
        conf['updated_on'] = datetime.datetime.now(tz=pytz.UTC)
        FileModel.create(**conf)

    @classmethod
    def get(cls, **config):

        # using filter , it returns None, if it does not exist
        # using get , gives an exception DoesNotExist for the same
        conf = cls.get_model_values(config)
        q = FileModel.objects.filter(**conf)
        if q:
            return q[0]
        return None

    @classmethod
    def list(cls, **config):
        conf = cls.get_model_values(config)
        q = FileModel.objects.filter(**conf)
        return q


    @classmethod
    def delete(cls, **config):
        conf = cls.get_model_values(config)
        entry = cls.get(**conf)
        if entry:
            entry.delete()

if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    fs = FileServer(['172.17.0.1'])
    meta = {
        'chumma': 40
    }
    with open("/bin/sleep", "rb") as fp:
        content = fp.read()
    
    entry={
        'machine': 'R2D2',
        'path': '/var/abcd',
        'content': content,
        'meta': json.dumps(meta),
    }
    fs.insert(**entry)
    entry['path']='/var/abcdef'
    fs.insert(**entry)

    config = {
        'machine': 'R2D2',
        'path': '/var/abcd'
    }
    entry = fs.get(**config)
    print(entry.meta,entry.machine)

    config = {
        'machine': 'R2D2'
    }
    entries = fs.list(**config)
    for e in entries:
        print(e.meta, e.machine, e.path)


    fs.delete(path='/var/dumma', machine='chumma')
    fs.delete(path='/var/abcd', machine='R2D2')
