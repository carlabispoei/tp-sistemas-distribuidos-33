import hashlib

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.data}{self.previous_hash}"
        return hashlib.sha256(value.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    @staticmethod
    def from_dict(data):
        block = Block(
            data["index"],
            data["data"],
            data["previous_hash"]
        )
        block.hash = data["hash"]
        return block

    def __str__(self):
        return (f"Block(index={self.index}, data={self.data}, "
                f"prev_hash={self.previous_hash}, hash={self.hash[:10]}...)")