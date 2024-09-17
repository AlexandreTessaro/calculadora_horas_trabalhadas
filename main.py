from src.calculadora import calcular_horas_trabalhadas, calcular_horas_com_intervalo, calcular_horas_invertido
from src.formatacao import formatar_horario_sem_pontos

def main():
    print("Bem-vindo à Calculadora de Horas Trabalhadas!")
    
    inicio = input("Insira o horário de início (HH:mm ou Hmmm): ")
    fim = input("Insira o horário de término (HH:mm ou Hmmm): ")

    if ":" not in inicio:
        inicio = formatar_horario_sem_pontos(inicio)
    if ":" not in fim:
        fim = formatar_horario_sem_pontos(fim)

    intervalo = input("Insira o intervalo de almoço (HH:mm ou Hmmm, ou deixe em branco para nenhum): ")
    if intervalo:
        if ":" not in intervalo:
            intervalo = formatar_horario_sem_pontos(intervalo)
        
        horas_trabalhadas = calcular_horas_com_intervalo(inicio, fim, intervalo)
    else:
        horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
    
    if horas_trabalhadas is None:
        print("Erro ao calcular as horas trabalhadas. Verifique os horários inseridos.")
    else:
        print(f"Você trabalhou {horas_trabalhadas:.2f} horas.")

if __name__ == "__main__":
    main()
