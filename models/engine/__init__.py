#!/usr/bin/python3



from os import getenv
from module.engine.file_storage import FileStorage


if not getnev('hbnb_dev_db') == 'db':
    from models.engine.file_storage import FileStorage
    pack = FileStorage()
else :
    from models.engine.db_storage import DBStorage
    pack = DBStorage()


pack.reaload()
