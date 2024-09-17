from datetime import datetime
from src.formatacao import validar_horario

def calcular_horas_trabalhadas(inicio, fim):
    hora_inicio = validar_horario(inicio)
    hora_fim = validar_horario(fim)
    
    if hora_inicio and hora_fim:
        horas_trabalhadas = (hora_fim - hora_inicio).seconds / 3600
        if horas_trabalhadas < 0:
            horas_trabalhadas += 24  # Para casos onde fim é no dia seguinte
        return horas_trabalhadas
    return None

def calcular_horas_com_intervalo(inicio, fim, intervalo):
    horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
    intervalo_duracao = validar_horario(intervalo)
    
    if horas_trabalhadas and intervalo_duracao:
        intervalo_horas = intervalo_duracao.hour + intervalo_duracao.minute / 60
        return horas_trabalhadas - intervalo_horas
    return None

def calcular_horas_invertido(inicio, fim):
    horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
    if horas_trabalhadas is None:
        return None
    
    if horas_trabalhadas < 0:
        horas_trabalhadas += 24  # Ajuste para horários invertidos
    return horas_trabalhadas
