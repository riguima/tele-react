# tele-react

Um robô de Telegram que faz reações automaticas em grupos e canais

## Instalação

Instale os requerimentos com `pip install -r requirements.txt`

## Configuração

Crie um arquivo chamado `.env` no diretório raiz e defina as seguintes variáveis:

- SQLALCHEMY_DATABASE_URI = A url do banco de dados, por exemplo "postgresql://username:password@localhost:5432/my_database"
- USERNAME = Nome do seu usuário, a aplicação vai usar sua conta para fazer as reações, porque bots do Telegram não podem fazer reações
- BOT\_NAME = Nome do bot que será usado para se comunicar com o usuário definido em USERNAME
- API\_ID
- API\_HASH
- BOT\_TOKEN

## Uso

Rode o bot com `python tele_react/main.py`
