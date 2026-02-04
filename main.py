from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

app = FastAPI()

class DeliveryInfo(BaseModel):
    read: Dict[str, Any] = Field(default_factory=dict)
    delivered: List[datetime] = Field(default_factory=list)

class MessageEvent(BaseModel):
    event_timestamp: datetime
    message_id: str
    org_id: str
    ack: bool
    body: Optional[str] = None
    from_: str = Field(..., alias="from")
    links: List[Any] = Field(default_factory=list)
    location: Optional[Any] = None
    mentioned_ids: List[Any] = Field(default_factory=list)
    message_type: str
    vcards: List[Any] = Field(default_factory=list)
    chat_id: str
    timestamp: datetime
    org_phone: str
    broadcast_id: Optional[str] = None
    is_deleted: bool
    media: Dict[str, Any] = Field(default_factory=dict)
    performed_by: Optional[str] = None
    prev_body: Optional[str] = None
    quoted_message_id: Optional[str] = None
    sender_phone: str
    parent_message_id: Optional[str] = None
    delivery_info: DeliveryInfo
    updated_at: datetime
    message_ticket_id: Optional[str] = None
    unique_id: str
    flag_status: Optional[str] = None
    flag_metadata: Dict[str, Any] = Field(default_factory=dict)

@app.post("/events")
async def receive_event(event: MessageEvent):
    """
    Endpoint to receive message events.
    """
    return {"status": "success", "received_id": event.unique_id}

@app.get("/")
async def root():
    return {"message": "FastAPI Server is running"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
