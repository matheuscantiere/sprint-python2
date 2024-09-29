from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Substitua essas credenciais pelas suas, que estão no painel do Twilio
account_sid = 'seu SID'
auth_token = 'Seu Auth Token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="🌟 *Bem-vindo ao Chat Turbo!* ⚡\n\n O *Chat Turbo* traz tudo sobre *Fórmula E*! 🏎️💨 Aqui você encontra informações sobre *pilotos* 🏁, *ranking* da temporada 🏆, *equipes* 🔧, além de detalhes sobre *regulamento* 📜 e *termos técnicos* ⚙️. Explore o futuro do automobilismo elétrico! 🔋\n\n Pronto para acelerar?🏎️⚡\n Digite: _*opções*_ \n\n #ChatTurbo #FormulaE #Futuro",
    from_='whatsapp:+14155238886',
    to='whatsapp:+55 Seu numero de telefone com DDD'
)

print(f"Mensagem enviada: {message.sid}")

# Criar servidor Flask para receber mensagens
app = Flask(__name__)

detalhes = [
    {
      "name": "Jake Dennis", 
      "country": "🇬🇧",
      "team": "Andretti",
      "position": 1,
      "points": 229,
      "races_won": 4,
      "best_lap_time": "1:28.456",
      "best_track": "Londres 🇬🇧"
    },
    {
      "name": "Nick Cassidy", 
      "country": "🇳🇿",
      "team": "Envision Racing",
      "position": 2,
      "points": 220,
      "races_won": 3,
      "best_lap_time": "1:28.789",
      "best_track": "Mônaco 🇲🇨"
    },
    {
      "name": "Mitch Evans", 
      "country": "🇳🇿",
      "team": "Jaguar TCS Racing",
      "position": 3,
      "points": 197,
      "races_won": 2,
      "best_lap_time": "1:29.012",
      "best_track": "Roma 🇮🇹"
    },
    {
      "name": "Pascal Wehrlein", 
      "country": "🇩🇪",
      "team": "TAG Heuer Porsche",
      "position": 4,
      "points": 170,
      "races_won": 2,
      "best_lap_time": "1:28.890",
      "best_track": "Cidade do Cabo 🇿🇦"
    },
    {
      "name": "Sébastien Buemi", 
      "country": "🇨🇭",
      "team": "Envision Racing",
      "position": 5,
      "points": 146,
      "races_won": 1,
      "best_lap_time": "1:29.100",
      "best_track": "Diriyah 🇸🇦"
    },
    {
      "name": "Antonio Felix da Costa", 
      "country": "🇵🇹",
      "team": "TAG Heuer Porsche",
      "position": 6,
      "points": 138,
      "races_won": 1,
      "best_lap_time": "1:29.234",
      "best_track": "Cidade do Cabo 🇿🇦"
    },
    {
      "name": "Jean-Éric Vergne", 
      "country": "🇫🇷",
      "team": "DS Penske",
      "position": 7,
      "points": 125,
      "races_won": 1,
      "best_lap_time": "1:29.456",
      "best_track": "Hyderabad 🇮🇳"
    },
    {
      "name": "Stoffel Vandoorne", 
      "country": "🇧🇪",
      "team": "DS Penske",
      "position": 8,
      "points": 112,
      "races_won": 0,
      "best_lap_time": "1:29.670",
      "best_track": "Berlim 🇩🇪"
    },
    {
      "name": "Sam Bird", 
      "country": "🇬🇧",
      "team": "NEOM McLaren",
      "position": 9,
      "points": 105,
      "races_won": 1,
      "best_lap_time": "1:29.890",
      "best_track": "Cidade do México 🇲🇽"
    },
    {
      "name": "Maximilian Günther", 
      "country": "🇩🇪",
      "team": "Maserati MSG Racing",
      "position": 10,
      "points": 96,
      "races_won": 0,
      "best_lap_time": "1:30.100",
      "best_track": "Mônaco 🇲🇨"
    },
    {
      "name": "Robin Frijns", 
      "country": "🇳🇱",
      "team": "ABT CUPRA",
      "position": 11,
      "points": 85,
      "races_won": 0,
      "best_lap_time": "1:30.200",
      "best_track": "Valência 🇪🇸"
    },
    {
      "name": "Oliver Rowland", 
      "country": "🇬🇧",
      "team": "Nissan Formula E",
      "position": 12,
      "points": 78,
      "races_won": 0,
      "best_lap_time": "1:30.450",
      "best_track": "Diriyah 🇸🇦"
    },
    {
      "name": "Edoardo Mortara", 
      "country": "🇨🇭",
      "team": "Mahindra Racing",
      "position": 13,
      "points": 70,
      "races_won": 0,
      "best_lap_time": "1:30.670",
      "best_track": "Seul 🇰🇷"
    },
    {
      "name": "Lucas di Grassi", 
      "country": "🇧🇷",
      "team": "ABT CUPRA",
      "position": 14,
      "points": 62,
      "races_won": 1,
      "best_lap_time": "1:30.890",
      "best_track": "Cidade do México 🇲🇽"
    },
    {
      "name": "Nyck de Vries", 
      "country": "🇳🇱",
      "team": "Mahindra Racing",
      "position": 15,
      "points": 55,
      "races_won": 0,
      "best_lap_time": "1:31.200",
      "best_track": "Mônaco 🇲🇨"
    },
    {
      "name": "Sérgio Sette Câmara", 
      "country": "🇧🇷",
      "team": "NIO 333 Racing",
      "position": 16,
      "points": 50,
      "races_won": 0,
      "best_lap_time": "1:31.450",
      "best_track": "São Paulo 🇧🇷"
    },
    {
      "name": "Nico Müller", 
      "country": "🇨🇭",
      "team": "ABT CUPRA",
      "position": 17,
      "points": 48,
      "races_won": 0,
      "best_lap_time": "1:31.670",
      "best_track": "Berlim 🇩🇪"
    },
    {
      "name": "Jake Hughes", 
      "country": "🇬🇧",
      "team": "NEOM McLaren",
      "position": 18,
      "points": 45,
      "races_won": 0,
      "best_lap_time": "1:31.890",
      "best_track": "Diriyah 🇸🇦"
    },
    {
      "name": "Sam Bird", 
      "country": "🇬🇧",
      "team": "NEOM McLaren",
      "position": 19,
      "points": 42,
      "races_won": 1,
      "best_lap_time": "1:32.010",
      "best_track": "Cidade do México 🇲🇽"
    },
    {
      "name": "Edoardo Mortara", 
      "country": "🇨🇭",
      "team": "Mahindra Racing",
      "position": 20,
      "points": 38,
      "races_won": 0,
      "best_lap_time": "1:32.230",
      "best_track": "Mônaco 🇲🇨"
    },
    {
      "name": "Robin Frijns", 
      "country": "🇳🇱",
      "team": "Envision Racing",
      "position": 21,
      "points": 36,
      "races_won": 0,
      "best_lap_time": "1:32.456",
      "best_track": "Londres 🇬🇧"
    },
    {
      "name": "Norman Nato", 
      "country": "🇫🇷",
      "team": "Andretti",
      "position": 22,
      "points": 30,
      "races_won": 0,
      "best_lap_time": "1:32.678",
      "best_track": "Roma 🇮🇹"
    },
    {
      "name": "Sacha Fenestraz", 
      "country": "🇫🇷",
      "team": "Nissan Formula E",
      "position": 23,
      "points": 28,
      "races_won": 0,
      "best_lap_time": "1:32.890",
      "best_track": "Cidade do Cabo 🇿🇦"
    },
    {
      "name": "Maximilian Günther", 
      "country": "🇩🇪",
      "team": "Maserati MSG Racing",
      "position": 24,
      "points": 25,
      "races_won": 0,
      "best_lap_time": "1:33.012",
      "best_track": "Mônaco 🇲🇨"
    },
    {
      "name": "Oliver Rowland", 
      "country": "🇬🇧",
      "team": "Nissan Formula E",
      "position": 25,
      "points": 20,
      "races_won": 0,
      "best_lap_time": "1:33.234",
      "best_track": "Diriyah 🇸🇦"
    },
    {
      "name": "Tom Blomqvist", 
      "country": "🇬🇧",
      "team": "Jaguar TCS Racing",
      "position": 26,
      "points": 18,
      "races_won": 0,
      "best_lap_time": "1:33.456",
      "best_track": "Seul 🇰🇷"
    },
    {
      "name": "Dan Ticktum", 
      "country": "🇬🇧",
      "team": "NIO 333 Racing",
      "position": 27,
      "points": 15,
      "races_won": 0,
      "best_lap_time": "1:33.670",
      "best_track": "Cidade do Cabo 🇿🇦"
    },
    {
      "name": "Norman Nato", 
      "country": "🇫🇷",
      "team": "Andretti Formula E",
      "position": 28,
      "points": 12,
      "races_won": 0,
      "best_lap_time": "1:33.890",
      "best_track": "São Paulo 🇧🇷"
    }
]


equipes = {
    "Avalanche Andretti": {"Pilotos": ["Jake Dennis", "Andre Lotterer"], "Carro": "Gen3"},
    "Envision Racing": {"Pilotos": ["Nick Cassidy", "Sebastian Buemi"], "Carro": "Gen3"},
    "Jaguar TCS Racing": {"Pilotos": ["Mitch Evans", "Sam Bird"], "Carro": "Jaguar I-Type 6"},
    "TAG Heuer Porsche": {"Pilotos": ["Pascal Wehrlein", "Antonio Felix da Costa"], "Carro": "Porsche 99X Electric"},
    "DS Penske": {"Pilotos": ["Jean-Eric Vergne", "Stoffel Vandoorne"], "Carro": "DS E-Tense FE23"},
    "Nissan Formula E Team": {"Pilotos": ["Sacha Fenestraz", "Norman Nato"], "Carro": "Nissan Gen3"},
    "Mahindra Racing": {"Pilotos": ["Lucas di Grassi", "Roberto Merhi"], "Carro": "Mahindra M9Electro"}
}

termos = {
    "*Attack Mode*": "Modo que concede potência extra temporária, ativado ao passar por uma zona específica da pista.",
    "*Fanboost*": "Aumento de potência temporário concedido por votação dos fãs online.",
    "*Regen*": "Recuperação de energia por frenagem regenerativa, fundamental para estratégias de corrida.",
    "*Gen3 Evo*": "Nova geração de carros com mais eficiência e potência."
}

regulamento = {
    "Gen3 Evo": "Maior potência, com melhorias no chassi e aerodinâmica para a temporada.",
    "Corridas duplas": "Três cidades terão corridas duplas: Diriyah, Mônaco e Xangai.",
    "Limite de regeneração": "Limite de energia recuperada nas corridas ajustado para manter as estratégias mais equilibradas."
}

curiosidades = {
    "Calendário Recorde": "2024/25 será a maior temporada da história da Fórmula E, com 17 corridas.",
    "Monaco Dobrando": "Mônaco terá uma rodada dupla pela primeira vez.",
    "Carro Gen3": "O carro Gen3 estabeleceu novos recordes de velocidade e eficiência energética."
}

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'opcoes' in incoming_msg or 'opções' in incoming_msg:
        msg.body('Escolha uma das opções abaixo:\n\n 1. Pilotos\n 2. Equipes\n 3. Termos\n 4. Regulamentos\n 5. Curiosidades\n 6. Detalhes\n 7. Ranking')

    elif '1' in incoming_msg or 'pilotos' in incoming_msg:
        response_text = "*🚦 Pilotos:*\n\n"
        for piloto in detalhes:
            response_text += f"_Nome:_ {piloto['name']} {piloto['country']}\nEquipe: {piloto['team']}\n\n"
        msg.body(response_text)

    elif '2' in incoming_msg or 'equipes' in incoming_msg:
        response_text = "👥 Equipes e Carros: 🏎\n\n"
        for i, y in equipes.items():
            response_text += f"Equipe: {i}\n, Pilotos: {', '.join(y['Pilotos'])}, Carro: {y['Carro']}\n\n"
        msg.body(response_text)

    elif '3' in incoming_msg or 'termos' in incoming_msg:
        response_text = "📋 Termos Técnicos: 📈\n\n"
        for i, y in termos.items():
            response_text += f"{i}: {y}\n"
        msg.body(response_text)

    elif '4' in incoming_msg or 'regulamento' in incoming_msg:
        response_text = "📖 _Regulamento:_ 📝\n\n"
        for i, y in regulamento.items():
            response_text += f"*{i}*: {y}\n\n"
        msg.body(response_text)

    elif '5' in incoming_msg or 'curiosidades'  in incoming_msg:
        response_text = "*🧠 Curiosidades: 👀*\n\n"
        for i, y in curiosidades.items():
            response_text += f"_{i}_:   {y}\n\n"
        msg.body(response_text)

    elif '6' in incoming_msg or 'detalhes' in incoming_msg:
        # Capturar o nome do piloto digitado pelo usuário (removendo a palavra 'detalhes')
        piloto_nome = incoming_msg.replace('detalhes', '').strip()

        # Procurar por esse nome nos detalhes dos pilotos
        piloto_encontrado = None
        for pilot in detalhes:
            if pilot['name'].lower() == piloto_nome:
                piloto_encontrado = pilot
                break

        # Se o piloto foi encontrado, exibir os detalhes
        if piloto_encontrado:
            response_text = (f"👤*Nome: {piloto_encontrado['name']} {piloto_encontrado['country']}*\n" 
                             f"Equipe: {piloto_encontrado['team']},\n\n"
                             f"Posição: {piloto_encontrado['position']}, Pontos: {piloto_encontrado['points']},\n"
                             f"Corridas ganhas: {piloto_encontrado['races_won']}, \n"
                             f"Melhor volta: {piloto_encontrado['best_lap_time']}, \n"
                             f"Melhor pista: {piloto_encontrado['best_track']}.")
        else:
            response_text = "Piloto não encontrado. Por favor digite: detalhes {nome do piloto}."

        msg.body(response_text)

    elif '7' in incoming_msg or 'ranking' in incoming_msg:
        response_text = "Ranking de Pilotos:\n\n"
        for piloto in detalhes:
            response_text += f" _Posição_: _{piloto['position']}_\n Nome: {piloto['name']}{piloto['country']}, Pontos: {piloto['points']}\n"
        msg.body(response_text)
    
    else:
        msg.body('Opção inválida. Por favor, escolha entre: pilotos, equipes, termos, regulamento, curiosidades, detalhes <nome do piloto>.')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)