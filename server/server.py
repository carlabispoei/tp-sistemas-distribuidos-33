from xmlrpc.server import SimpleXMLRPCServer
from models.block import Block
from utils.serializer import (
    serialize_block,
    deserialize_request
)
import json  

# Criar blockchain ligada
blockchain = []

def create_blockchain():
    global blockchain

    genesis = Block(1, "Genesis Block", "0")
    block2 = Block(2, "Segundo bloco", genesis.hash)
    block3 = Block(3, "Terceiro bloco", block2.hash)

    blockchain = [genesis, block2, block3]

create_blockchain()

# enviar bloco ao cliente
def get_block(request_json):
    print("\nPedido recebido!")

    block_id = deserialize_request(request_json)
    print(f"Cliente pediu bloco: {block_id}")

    # procurar bloco correto
    for block in blockchain:
        print("A verificar bloco:", block.index)

        if block.index == block_id:
            print("Bloco encontrado!")
            print("A enviar bloco:", block.to_dict())

            return serialize_block(block)

    print("Bloco não encontrado!")
    return "ERRO: Bloco não encontrado"


# receber bloco do cliente
def send_block(block_json):
    print("\nRecebi bloco do cliente para desserializar!")

    block = json.loads(block_json)

    print("Bloco desserializado:", block)

    return f"Bloco {block['index']} desserializado com sucesso"


# Servidor
server = SimpleXMLRPCServer(("localhost", 8000))

server.register_function(get_block, "get_block")
server.register_function(send_block, "send_block")  # 👈 NOVO

print("Servidor RPC ativo na porta 8000...")
server.serve_forever()