# match_database.py
from database import Database

class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def create_jogador(self, name):
        query = "CREATE (:Jogador {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_jogadores(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [record["name"] for record in results]

    def update_jogador(self, old_name, new_name):
        query = "MATCH (j:Jogador {name: $old_name}) SET j.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_jogador(self, name):
        query = "MATCH (j:Jogador {name: $name}) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_partida(self, name):
        query = "CREATE (:Partida {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def adicionar_jogador_a_partida(self, jogador_name, partida_name):
        query = """
        MATCH (j:Jogador {name: $jogador_name})
        MATCH (p:Partida {name: $partida_name})
        CREATE (j)-[:PARTICIPOU_DE]->(p)
        """
        parameters = {"jogador_name": jogador_name, "partida_name": partida_name}
        self.db.execute_query(query, parameters)

    def get_partidas(self):
        query = "MATCH (p:Partida) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [record["name"] for record in results]

    def delete_partida(self, name):
        query = "MATCH (p:Partida {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def registrar_resultado(self, partida_name, jogador_name, resultado):
        """
        Registra o resultado de um jogador em uma partida específica.
        """
        query = f"""
        MATCH (j:Jogador {{name: $jogador_name}})-[:PARTICIPOU_DE]->(p:Partida {{name: $partida_name}})
        SET j['resultado_na_partida_{partida_name}'] = $resultado
        """
        parameters = {"partida_name": partida_name, "jogador_name": jogador_name, "resultado": resultado}
        self.db.execute_query(query, parameters)

    def get_resultado_partida(self, partida_name, jogador_name):
        """
        Obtém o resultado de um jogador específico em uma partida.
        """
        query = f"""
        MATCH (j:Jogador {{name: $jogador_name}})-[:PARTICIPOU_DE]->(p:Partida {{name: $partida_name}})
        RETURN j['resultado_na_partida_{partida_name}'] AS resultado
        """
        parameters = {"partida_name": partida_name, "jogador_name": jogador_name}
        results = self.db.execute_query(query, parameters=parameters)
        return results[0]["resultado"] if results and results[0].get("resultado") is not None else None

    def listar_resultados_partida(self, partida_name):
        """
        Lista os resultados de todos os jogadores em uma partida específica.
        """
        query = f"""
        MATCH (j:Jogador)-[:PARTICIPOU_DE]->(p:Partida {{name: $partida_name}})
        RETURN j.name AS jogador, j['resultado_na_partida_{partida_name}'] AS resultado
        """
        parameters = {"partida_name": partida_name}
        results = self.db.execute_query(query, parameters=parameters)
        return {record["jogador"]: record["resultado"] for record in results if record.get("resultado") is not None}