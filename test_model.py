import json
from datetime import datetime
from main import MessageEvent

# The payload from the user
payload = {
  "event_timestamp": "2026-02-04T05:31:08Z",
  "message_id": "false_91961898",
  "org_id": "4c90d3aa-c33a-0",
  "ack": False,
  "body": "Hi",
  "from": "91901882723@c.us",
  "links": [],
  "location": None,
  "mentioned_ids": [],
  "message_type": "chat",
  "vcards": [],
  "chat_id": "91901882723@c.us",
  "timestamp": "2026-02-04T05:31:08Z",
  "org_phone": "919343063330@c.us",
  "broadcast_id": None,
  "is_deleted": False,
  "media": {},
  "performed_by": None,
  "prev_body": None,
  "quoted_message_id": "91801882723@c.us",
  "sender_phone": "91801882723@c.us",
  "parent_message_id": None,
  "delivery_info": {
    "read": {},
    "delivered": ["2026-02-04T05:33:05Z"]
  },
  "updated_at": "2026-02-04T05:33:05Z",
  "message_ticket_id": None,
  "unique_id": "ACAA9F100C307C2043CD39471",
  "flag_status": None,
  "flag_metadata": {}
}

try:
    event = MessageEvent(**payload)
    print("Validation Successful!")
    print(f"Parsed Unique ID: {event.unique_id}")
    print(f"Delivery Time: {event.delivery_info.delivered[0]}")
except Exception as e:
    print(f"Validation Failed: {e}")
