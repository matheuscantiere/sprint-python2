# Projeto ChatBot do Turbo Racing

Este projeto é um chatbot interativo para o WhatsApp sobre a Fórmula E, desenvolvido utilizando Python, Flask, Twilio e Ngrok. O chatbot fornece informações sobre pilotos, equipes, termos técnicos, regulamento e curiosidades da Fórmula E.




## Funcionalidades 
    Envio de mensagem de boas-vindas via WhatsApp utilizando Twilio.
    Integração com Flask para receber e responder mensagens dos usuários.

    O chatbot responde a comandos específicos enviados pelo usuário, oferecendo informações detalhadas sobre:
    Pilotos: Classificação dos pilotos com nome, equipe e pontos.
    Equipes: Lista de equipes, pilotos e modelos de carros.
    Termos Técnicos: Definições de termos importantes da Fórmula E.
    Regulamento: Regras e mudanças na competição.
    Curiosidades: Fatos interessantes sobre a temporada e a competição.
    Detalhes dos Pilotos: Informações completas sobre os principais pilotos.
    
##  Tecnologias Utilizadas
    Python: Linguagem principal para o desenvolvimento do projeto.
    Twilio: API para envio e recebimento de mensagens via WhatsApp.
    Flask: Framework para criar a aplicação web que recebe e responde mensagens.
    Ngrok: Ferramenta para criar um túnel HTTP público que expõe o servidor local, permitindo a integração com Twilio.

## Requisitos
    Python 3.x
    Conta no Twilio com número de WhatsApp verificado
    Ngrok para expor a aplicação Flask
    Pacotes Python:
     Flask
     twilio


## Instalação e Execução

### 1. Clonar o Repositório
    git clone https://github.com/seu-usuario/seu-repositorio.git

    cd seu-repositorio

### 2. Instalar as Dependências
    pip install -r requirements.txt

### 3. Configurar Twilio
    Substitua as credenciais account_sid e auth_token no código pelo seu SID e token de 
    autenticação disponíveis no painel do Twilio.

### 4. Executar o Servidor Flask
    python app.py

### 5. Expor a Aplicação com Ngrok
    Em um terminal separado, execute:
     ngrok http 5000

    Copie o URL gerado pelo Ngrok e configure como seu Webhook no Twilio.

### 6. Configurar o Webhook no Twilio
    1 Acesse sua conta Twilio.
    2 Vá para a seção de números e selecione o número de WhatsApp configurado.
    3 No campo "Webhook", insira a URL do Ngrok seguida de /whatsapp, por exemplo:
     https://seu-ngrok-url.ngrok.io/whatsapp

### 7. Testar o Chatbot

    Envie mensagens no WhatsApp para o número verificado com os seguintes comandos:

    "pilotos": Exibe a classificação dos pilotos.
    "equipes": Mostra as equipes e carros da Fórmula E.
    "termos": Explica termos técnicos importantes da competição.
    "regulamento": Exibe as principais regras e mudanças da temporada.
    "curiosidades": Fatos interessantes sobre a Fórmula E.
    "detalhes": Informações detalhadas dos principais pilotos.


## Diagrama de Blocos


## Autores

- Enzo Valieres (RM555119)
- Gilherme Barbiero(RM 555185)
- Matheus Cantiere (RM558479)
- Pedro de Lorenzo (RM554720)
- Vinicius Castro (RM556137)
