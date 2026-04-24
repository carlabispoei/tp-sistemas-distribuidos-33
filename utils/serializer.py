import json
from models.block import Block

# -------- BLOCO --------
def serialize_block(block):
    return json.dumps(block.to_dict())

def deserialize_block(block_json):
    data = json.loads(block_json)
    return Block.from_dict(data)

# -------- PEDIDO --------
def serialize_request(block_id):
    return json.dumps({"block_id": block_id})

def deserialize_request(request_json):
    return json.loads(request_json)["block_id"]