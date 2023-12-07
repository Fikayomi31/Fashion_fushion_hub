#!/usr/bin/python3
""" create a unique file storage for the application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
