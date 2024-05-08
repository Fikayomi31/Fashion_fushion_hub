#!/usr/bin/python3
""" create a unique file storage for the application"""
from os import getenv

storage_type = getenv("FFH_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
