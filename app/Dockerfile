# Utilizamos uma imagem Python, versão 3.6 como imagem
FROM python:3.6

# O EXPOSE indica a porta utilizada em nosso container, utilizaremos a porta 5000, a dafault do Flask
EXPOSE 5000

#Copiando todos os arquivos do diretório local - ignorando o Dockerfile - para o /app
WORKDIR /app
COPY . .

# Instalação de todas as dependências necessárias e início do programa
RUN pip install -r requirements.txt
CMD python app.py
