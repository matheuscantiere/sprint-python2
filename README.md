# Projeto Chatbot do Turbo Racing

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
    
## ecnologias Utilizadas
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
    git clone https://github.com/matheuscantiere/sprint-python2.git

    cd seu-repositorio

### 2. Instalar as Dependências
    pip install twilio
    pip install Flask


### 3. Configuração do Twilio
#### 3.1 Criar Conta no Twilio
    Não precisa colocar a autentificação de 2 fatores.
![Criar Conta](/img/CriarCOnta.png)
    

#### 3.2 Adicionar Numero de Telefone
![Numero Telefone](/img/NumeroTelefone.png)

#### 3.3 Código de segurança
    Coloque o código que chegara através do seu número de celular.
![Código de Segurança](/img/ColocarCodigo.png)

#### 3.4 Salvar Código de Recuperação
    salve este código para conseguir recuperar sua conta caso algo aconteça com ela.
![Código de recuperação](/img/SalvarCodigo.png)

#### 3.5 Colocar Informações
    Coloque as informações necessárias para poder seguir com o cadastro.
![Informações](/img/Informacoes.png)

#### 3.6 Clique em Account Dashboard
    Clique em Account Dashboard para pegar alguns dados necessarios
![Account Dashboard](/img/DashBoard.png)

#### 3.7 Pegar o SID e o AUTH TOKEN
    Pegue o SID e o AUTH TOKEN para poder substituir no código
![SidToken](/img/SidToken.png)

#### 3.8 Conectar com WhatsApp
    Clique em send a WhatsApp message para poder conectar com seu WhatsApp e conseguir mandar mensagens.
![WhatsApp](/img/Menssagem.png)

#### 3.9 QR code
    Escaneie o QR code para poder abrir seu WhatsApp
![QR code](/img/QrCode.png)

#### 3.10 Enviar mensagem pré selecionada
    Envie a mensagem que o twilio colocou para você.
![Mensagem](/img/MenssagemTwilio.png)



### 4. Configuração do ngrok
#### 4.1 Crie uma conta na ngrok
![Conta](/img/ContaNgrok.png)

#### 4.2 Adicionando Informações no Ngrok
    Colocando informações no ngrok para prosseguir no login
![Informações](/img/InformacoesNgrok.png)

#### 4.3 Instalação Ngrok
    Instale o Ngrok de acordo com seu sistema operacional
![instalação](/img/InstalacaoNgrok.png)

#### 4.4 Executando Ngrok
    Após baixar e extrair o ngrok execute o arquivo para poder terminar de configurar.
![Executar](/img/Executar.png)

#### 4.5 Clique em YOURAUTHOKEN
    Clique em yourauthoken para consegui pegar seu token
![Informações](/img/AutenticacaoToken.png)

#### 4.6 Copie seu Token para poder autenticar
    Copie seu token para poder autenticar no cmd do ngrok
![Informações](/img/CopiarToken.png)

#### 4.7 Autenticando seu token no cmd do ngrok
    Após executar o Ngrok execute o comando "ngrok config add-authtoken SEU TOKEN"
![Informacoes](/img/CmdToken.png)

#### 4.8 Iniciando o ngrok 
    Após autenticar seu token, digite o comando "ngrok http 5000" para poder iniciar o ngrok
![Informações](/img/Http5000.png)

#### 4.9 Copiando URL e colocando no twilio para poder rodar
    Copie a URL que o ngrok ira disponibilizar e coloque no twilio para ligar com seu whatsapp
![Informações](/img/CopiarUrl.png)

#### 4.10 Colocando a url no twilio
    Coloque a URL que o ngrok gerou no twilio no final coloque   https://seu-ngrok-url.ngrok.io/whatsapp para conseguir se conectar.
![Informações](/img/ColocandoUrlTwilio.png)


### 5 Configurando Código Python
### 5.1 Colocando suas informações no código Python
    Coloque suas informações do sid e o auth token no código Python para conseguir conectar, também coloque seu numero de celular com o DDD para a mensagem chegar para você.
![Informações](/img/SubstituirInformacoesCodigo.png)

### 5.2 Executando Projeto
    Execute o projeto Python em sua máquina, após executar o twilio enviará uma mensagem personalizada de boas-vindas, após isso você já pode colocar alguns tópicos que temos para ver algumas informações sobre a formula E
    Também pode executar com o comando  python app.py no terminal do VsCode
![Informações](/img/ExecutarProjeto.png)

### 5.3 Confirmações no cmd do ngrok
    Caso de tudo certo quando você enviar a mensagem no WhatsApp receberá uma confirmação no cmd do ngrok
![Informacoes](/img/ConfirmacaoCMD.png)


### 6. Testar o Chatbot

    Envie mensagens no WhatsApp para o número verificado com os seguintes comandos:

    "pilotos": Exibe a classificação dos pilotos.
    "equipes": Mostra as equipes e carros da Fórmula E.
    "termos": Explica termos técnicos importantes da competição.
    "regulamento": Exibe as principais regras e mudanças da temporada.
    "curiosidades": Fatos interessantes sobre a Fórmula E.
    "detalhes": Informações detalhadas dos principais pilotos.


## Diagrama de Blocos
![Diagrama](DiagramaBlocos.png)

## Autores

- Enzo Valieres (RM555119)
- Gilherme Barbiero(RM 555185)
- Matheus Cantiere (RM558479)
- Pedro de Lorenzo (RM554720)
- Vinicius Castro (RM556137)
