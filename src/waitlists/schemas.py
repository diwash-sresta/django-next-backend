from ninja import Schema
from datetime import datetime
from pydantic import EmailStr
from typing import List,Any

class WaitlistEntryCreateSchema(Schema):
  #Create -> Data
  #WaitlistEntryIn
  email: EmailStr

class ErrorWaitlistEntryCreateSchema(Schema):
  #Create -> Data
  #WaitlistEntryIn
  email: List[Any]
  # non_field_errors: List[dict] = []

class WaitlistEntryListSchema(Schema):
  #list -> Data
  #WaitlistEntryOut
  id: int
  email: EmailStr

class WaitlistEntryDetailSchema(Schema):
  #Get -> Data
  #WaitlistEntryOut
  id : int
  email: str
  updated : datetime
  timestamp : datetime

