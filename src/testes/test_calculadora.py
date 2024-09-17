import unittest
from src.calculadora import calcular_horas_trabalhadas, calcular_horas_com_intervalo, calcular_horas_invertido
from src.formatacao import formatar_horario_sem_pontos

class TestCalculadoraHoras(unittest.TestCase):

    def test_validar_horario(self):
        from src.formatacao import validar_horario
        self.assertIsNotNone(validar_horario("08:00"))
        self.assertIsNone(validar_horario("25:00"))  # Horário inválido

    def test_calcular_horas_trabalhadas(self):
        self.assertEqual(calcular_horas_trabalhadas("08:00", "17:00"), 9)
        self.assertEqual(calcular_horas_invertido("17:00", "08:00"), 15)  # Horário invertido

    def test_calcular_horas_com_intervalo(self):
        self.assertEqual(calcular_horas_com_intervalo("08:00", "17:00", "01:00"), 8)

    def test_formatar_horario_sem_pontos(self):
        self.assertEqual(formatar_horario_sem_pontos("800"), "08:00")
        self.assertEqual(formatar_horario_sem_pontos("1700"), "17:00")

if __name__ == "__main__":
    unittest.main()
