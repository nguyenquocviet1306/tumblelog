from mongoengine import connect

db_name = "tumblelog"
host = "ds031157.mlab.com"
port = 31157
username = "admin"
password = "admin"

db_instance = None

def mlab_connect():
    global db_instance
    db_instance = connect(db=db_name, host=host, port=port, username=username, password=password)

def mlab_disconnect():
    db_instance.close()