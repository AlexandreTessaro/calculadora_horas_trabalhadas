from datetime import datetime

def validar_horario(horario):
    try:
        return datetime.strptime(horario, "%H:%M")
    except ValueError:
        print("Erro: Formato de horário inválido. Use HH:mm.")
        return None

def formatar_horario_sem_pontos(horario):
    if len(horario) == 4:  # Exemplo: "0800" -> "08:00"
        return f"{horario[:2]}:{horario[2:]}"
    elif len(horario) == 3:  # Exemplo: "800" -> "08:00"
        return f"0{horario[:1]}:{horario[1:]}"
    else:
        print("Erro: Formato de horário inválido.")
        return None
