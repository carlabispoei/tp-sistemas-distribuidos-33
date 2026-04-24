1.	Descrição do Trabalho

O presente trabalho consiste no desenvolvimento de um sistema distribuído baseado no paradigma cliente-servidor, utilizando Remote Procedure Call (RPC). O objetivo é permitir a comunicação entre um cliente e um servidor para a obtenção de blocos de uma blockchain Ethereum simulada.
O cliente envia um pedido ao servidor contendo o identificador de um bloco. O servidor processa esse pedido, obtém o bloco correspondente de uma estrutura simulada, procede à sua serialização em formato JSON e envia-o de volta ao cliente. O cliente, por sua vez, guarda o bloco recebido num ficheiro e pode reenviá-lo ao servidor para desserialização.
Este sistema permite demonstrar conceitos fundamentais de sistemas distribuídos, como comunicação remota, serialização e desserialização de dados.

 
Figura 1 – Arquitetura do sistema cliente-servidor
2.	Implementação do Trabalho	

A implementação foi realizada em Python, utilizando a biblioteca xmlrpc para comunicação entre cliente e servidor.
O servidor mantém uma estrutura de blockchain simulada composta por blocos encadeados através de hashes. Cada bloco contém um índice, dados e a referência ao bloco anterior.
Quando o cliente solicita um bloco, o servidor:
1.	Recebe o pedido serializado 
2.	Desserializa o identificador do bloco 
3.	Procura o bloco na blockchain 
4.	Serializa o bloco em formato JSON 
5.	Envia o resultado ao cliente 
O cliente:
1.	Serializa o pedido 
2.	Envia ao servidor via RPC 
3.	Recebe o bloco serializado 
4.	Guarda o bloco num ficheiro JSON 
5.	Desserializa o conteúdo para visualização 
A serialização foi implementada com JSON, permitindo uma representação simples e legível dos dados.
A arquitetura segue um modelo modular, permitindo a separação clara entre cliente, servidor e componentes de serialização.

3.	Funcionamento do trabalho	


O funcionamento do sistema inicia-se com a execução do servidor RPC, que fica à escuta de pedidos na porta definida. De seguida, é executado o cliente, que estabelece ligação com o servidor.

Ao iniciar o cliente, é apresentado ao utilizador um pedido de introdução do número do bloco pretendido, como ilustrado na Figura 2.

 
                                                                                                   Figura 2

O cliente recebe o valor introduzido pelo utilizador e procede à sua serialização, enviando o pedido ao servidor através do protocolo RPC.
O servidor recebe o pedido, desserializa o identificador do bloco e procura o bloco correspondente na blockchain simulada. Caso o bloco exista, o servidor procede à sua serialização em formato JSON e envia-o de volta ao cliente. (Fig. 3)


 
                                                                                                   Figura 3

O cliente recebe o bloco serializado, guarda-o automaticamente num ficheiro JSON (Fig. 4) com o nome correspondente ao identificador do bloco e realiza a desserialização dos dados para apresentação ao utilizador. 
 
Figura 4
Se o bloco solicitado não existir, o servidor devolve uma mensagem de erro, que é apresentada ao utilizador no cliente. (Fig. 5)
Este processo demonstra o fluxo completo de comunicação entre cliente e servidor, incluindo envio de pedidos, processamento remoto, serialização e desserialização de dados.

 
Fig. 5


4.	Conclusão


Neste trabalho foi desenvolvido um sistema distribuído simples baseado em RPC, que permite a comunicação entre cliente e servidor para a troca de dados estruturados.
Foram implementados os conceitos de serialização e desserialização, bem como a simulação de uma blockchain com blocos encadeados.
O sistema demonstrou funcionar corretamente, cumprindo todos os requisitos definidos no enunciado.
Como trabalho futuro, poderia ser implementada a ligação a uma blockchain real ou a utilização de uma base de dados para armazenamento persistente.




