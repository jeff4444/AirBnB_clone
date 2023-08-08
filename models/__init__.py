#!/usr/bin/python3
"""Init module for Filestorage package"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
