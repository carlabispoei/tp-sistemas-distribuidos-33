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
    # 👇 Guardar ficheiro
    filename = f"bloco_{block_id}.json"
    with open(filename, "w") as f:
        f.write(response)

    print(f"\nBloco guardado em {filename}")

    # Desserializar
    block = deserialize_block(response)

    print("\nBloco recebido:")
    print(block)

    # Mostrar dados
    if isinstance(block, dict):
        print("Hash:", block.get("hash"))
        print("Previous Hash:", block.get("previous_hash"))
    else:
        print("Hash:", block.hash)
        print("Previous Hash:", block.previous_hash)

    # 🔥 PARTE FINAL DO ENUNCIADO
    print("\nA enviar bloco de volta ao servidor para desserialização...")

    response_server = proxy.send_block(response)

    print("\nResposta do servidor:")
    print(response_server)