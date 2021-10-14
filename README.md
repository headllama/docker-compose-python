## Simples código que cria uma aplicação utilizando o Flask e o MySQL

# Utilização:
  Após clonar esse repositório em sua máquina local, basta rodar o comando `docker-compose up`, após isso, acesse a página `localhost:5000` em seu navegador, ao acessar, você conseguirá ler a tabela mysql criada no arquivo `init.sql`. Para sair, somente basta dar um CRTL+C em seu terminal.


# Apresentação da aplicação:
  Como boas práticas, o container somente deverá ser responsável por apenas um processo, para essa aplicação precisaremos de dois containers - um para rodar a aplicação e outro para o database - para isso utilizaremos o [Docker-Compose](https://docs.docker.com/compose/) 

  Esse programa contém dois arquivos principais: app.py - um simples programa flask que se comunica com o database e expõe um endpoit e o init.sql - um script SQL que inicializa o database antes da criação do programa.

  Foi criado um Dockerfile para o app, que por consequência irá criar uma imagem e, por fim, um container - cuja descrição dos passos estão bem documentados no container em si - basicamente utilizaremos a imagem 3.6 do Python e expomos a porta 5000, copiamos os arquivos app.py e requirements.txt para um diretório utilizado em nossa aplicação e por fim a instalação dos pacotes necessários para sua utiização.

  O arquivo principal - `docker-compose.yaml` utiliza dos serviços: A app e o database MySQL. Os pontos chave desse arquivo são:

- image: Representa uma imagem docker oficial existente do MySQL
- environment: É utilizada para adicionar variáveis de ambiente
- ports: Especifica as portas utilizadas - local e no container - escolhi essa porta alta para não ter conflito com alguma porta comum, eventualmente utilizada em sua máquina
- volumes: Como nós queremos que o container seja utilizado com nosso db, nós conectamos o diretório que contém o init.sql nesse container. O volume também é utilizado para persistir os dados, como você pode ver na [Documentação oficial](https://docs.docker.com/storage/volumes/)


Também conseguimos acessar o database diretamente de nosso terminal através do comando `mysql --host=127.0.0.1 --port=32000 -u root -p`
