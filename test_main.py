import unittest
from unittest.mock import patch
import io
import sys

from main import (gerar_numero_sorteado, obter_palpite, exibir_mensagem_palpite,
                  exibir_palpites, verificar_palpite, fazer_suposicao_computador,
                  deseja_jogar_novamente, agradecer_jogador)

class TestGuessTheNumber(unittest.TestCase):
    
    def test_gerar_numero_sorteado(self):
        # Verifica se o número gerado está dentro do intervalo esperado (entre 1 a 100)
        numero_sorteado = gerar_numero_sorteado()
        self.assertTrue(1 <= numero_sorteado <= 100)

    @patch('builtins.input', return_value='50')
    def test_obter_palpite(self, mock_input):
        # Verifica se a função retorna o palpite esperado
        self.assertEqual(obter_palpite("Teste"), 50)

    def test_exibir_mensagem_palpite(self):
        # Verifica se a mensagem de palpite exibida é correta para um palpite baixo
        captured_output = io.StringIO()
        sys.stdout = captured_output
        exibir_mensagem_palpite(30, 50)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Muito baixo!")

    def test_exibir_palpites(self):
        # Verifica se a função exibe corretamente os palpites
        captured_output = io.StringIO()
        sys.stdout = captured_output
        exibir_palpites([10, 20, 30])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Palpites: 10, 20, 30")

    def test_verificar_palpite(self):
        # Verifica se a função retorna True quando o palpite é igual ao número sorteado
        palpites = []
        self.assertTrue(verificar_palpite(50, 50, palpites, True))
        
    @patch('random.randint', return_value=52)
    def test_fazer_suposicao_computador(self, mock_randint):
        # Verifica se a suposição do computador não está na lista de palpites anteriores
        palpites = [30, 40, 50]
        self.assertNotIn(fazer_suposicao_computador(palpites, 1, 100), palpites)

    @patch('builtins.input', return_value='s')
    def test_deseja_jogar_novamente(self, mock_input):
        # Verifica se a função retorna True quando o jogador deseja jogar novamente
        self.assertTrue(deseja_jogar_novamente())

    def test_agradecer_jogador(self):
        # Verifica se a função de agradecimento imprime a mensagem correta
        captured_output = io.StringIO()
        sys.stdout = captured_output
        agradecer_jogador("Teste")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Obrigado por jogar, Teste! Até a próxima. 👋")

if __name__ == '__main__':
    unittest.main()
