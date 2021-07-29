from pydantic import BaseModel, Field
from typing import List, Optional


class Flex(BaseModel):
    userId: str = Field(..., example='UserId LINE TOKEN')
    channel_access_token: str = Field(..., example='Token LINE OA')
    docno: Optional[str] = None
    docdate: Optional[str] = None
    duedate: Optional[str] = None
    remark: Optional[str] = None
    endpoint: Optional[str] = None


class Text(BaseModel):
    userId: str = Field(..., example='UserId LINE TOKEN')
    channel_access_token: str = Field(..., example='Token LINE OA')
    text: str = Field(..., example='message send to user')
    docno: Optional[str] = None
    docdate: Optional[str] = None
    duedate: Optional[str] = None
    remark: Optional[str] = None
    endpoint: Optional[str] = None


class ReceiveCard(BaseModel):
    line: List[Flex]


class ReceiveText(BaseModel):
    line: List[Text]
