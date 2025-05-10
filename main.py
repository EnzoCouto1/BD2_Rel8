# main.py
from database import Database
from match_database import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.207.162.83:7687", "neo4j", "feedback-tones-incomes")
db.drop_all()

# Criando uma instância da classe MatchDatabase para interagir com o banco de dados
match_db = MatchDatabase(db)

# Criando alguns jogadores
match_db.create_jogador("João")
match_db.create_jogador("Maria")
match_db.create_jogador("José")
match_db.create_jogador("Ana")
match_db.create_jogador("Carlos")
match_db.create_jogador("Beatriz")

# Criando algumas partidas
match_db.create_partida("Truco da Galera")
match_db.create_partida("Xadrez Rápido")
match_db.create_partida("Truco dos Amigos")

# Adicionando jogadores às partidas de Truco
match_db.adicionar_jogador_a_partida("João", "Truco da Galera")
match_db.adicionar_jogador_a_partida("Maria", "Truco da Galera")
match_db.adicionar_jogador_a_partida("José", "Truco dos Amigos")
match_db.adicionar_jogador_a_partida("Ana", "Truco dos Amigos")

# Adicionando jogadores à partida de Xadrez
match_db.adicionar_jogador_a_partida("Carlos", "Xadrez Rápido")
match_db.adicionar_jogador_a_partida("Beatriz", "Xadrez Rápido")

# Atualizando o nome de um jogador
match_db.update_jogador("João", "Pedro")

# Registrando resultados das partidas de Truco (pontuação)
match_db.registrar_resultado("Truco da Galera", "Pedro", 12)
match_db.registrar_resultado("Truco da Galera", "Maria", 10)
match_db.registrar_resultado("Truco dos Amigos", "José", 15)
match_db.registrar_resultado("Truco dos Amigos", "Ana", 13)

# Registrando resultados da partida de Xadrez (vitória = 1, derrota = 0)
match_db.registrar_resultado("Xadrez Rápido", "Carlos", 1)
match_db.registrar_resultado("Xadrez Rápido", "Beatriz", 0)

# Deletando um jogador e uma partida
match_db.delete_jogador("Beatriz")
match_db.delete_partida("Xadrez Rápido")

# Imprimindo todas as informações do banco de dados
print("\nJogadores:")
print(match_db.get_jogadores())
print("\nPartidas:")
print(match_db.get_partidas())
print("\nResultado da partida 'Truco da Galera':")
print(match_db.listar_resultados_partida("Truco da Galera"))
print("\nResultado de Pedro na partida 'Truco da Galera':", match_db.get_resultado_partida("Truco da Galera", "Pedro"))
print("\nResultado da partida 'Truco dos Amigos':")
print(match_db.listar_resultados_partida("Truco dos Amigos"))
print("\nResultado da partida 'Xadrez Rápido':") # Esta partida foi deletada
print(match_db.listar_resultados_partida("Xadrez Rápido"))

# Fechando a conexão com o banco de dados
db.close()