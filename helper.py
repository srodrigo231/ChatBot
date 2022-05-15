

IAMBOT = "Soy un bot"
DESC = "y gestiono tus turnos"
QUES1 = "que necesitas?"
SKILL_DESC = "puedo ayudarte a consultar, actualizar, agendar y declinar tus turnos asignados."

def get_current_time_object():
    """
    Return current time object with info about hour, minute, seconds, and date
    """
    from datetime import datetime
    now = datetime.now()
    return now

