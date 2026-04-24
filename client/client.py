import xmlrpc.client
import json
from utils.serializer import (
    serialize_request,
    deserialize_block
)

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# 👇 Pergunta ao utilizador
block_id = int(input("Que bloco queres pedir? (Ex: 1, 2, 3): "))

print(f"A pedir bloco {block_id} ao servidor...")

# Serializar pedido
request = serialize_request(block_id)

# Enviar pedido
response = proxy.get_block(request)

# Verificar erro
if "ERRO" in response:
    print(response)

else:
    # 👇 Guardar ficheiro (IMPORTANTE para o professor)
    filename = f"bloco_{block_id}.json"
    with open(filename, "w") as f:
        f.write(response)

    print(f"\nBloco guardado em {filename}")

    # Desserializar
    block = deserialize_block(response)

    print("\nBloco recebido:")
    print(block)

    # 👇 Evitar erro (caso seja dict)
    if isinstance(block, dict):
        print("Hash:", block.get("hash"))
        print("Previous Hash:", block.get("previous_hash"))
    else:
        print("Hash:", block.hash)
        print("Previous Hash:", block.previous_hash)