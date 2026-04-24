from xmlrpc.server import SimpleXMLRPCServer
from models.block import Block
from utils.serializer import (
    serialize_block,
    deserialize_request
)

# 🔗 Criar blockchain ligada
blockchain = []

def create_blockchain():
    global blockchain

    genesis = Block(1, "Genesis Block", "0")
    block2 = Block(2, "Segundo bloco", genesis.hash)
    block3 = Block(3, "Terceiro bloco", block2.hash)

    blockchain = [genesis, block2, block3]

create_blockchain()

def get_block(request_json):
    print("\nPedido recebido!")

    block_id = deserialize_request(request_json)
    print(f"Cliente pediu bloco: {block_id}")

    # 🔍 procurar bloco correto
    for block in blockchain:
        print("A verificar bloco:", block.index)

        if block.index == block_id:
            print("Bloco encontrado!")
            print("A enviar bloco:", block.to_dict())

            return serialize_block(block)  # ✅ CORRETO

    print("Bloco não encontrado!")
    return "ERRO: Bloco não encontrado"


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(get_block, "get_block")

print("Servidor RPC ativo na porta 8000...")
server.serve_forever()