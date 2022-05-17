IAMBOT = "Soy un bot"
DESC = "puedo gestionar tus turnos"
QUES1 = "que necesitas?"
SKILL_DESC = "te ayudo a : \n1. consultar\n 2. actualizar\n 3. agendar \n 4. declinar tus turnos asignados.\n"

def get_current_time_object():
    """
    Return current time object with info about hour, minute, seconds, and date
    """
    from datetime import datetime
    now = datetime.now()
    return now