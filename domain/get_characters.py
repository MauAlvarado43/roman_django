from app.models import Process

def get_characters(pk):
    
    number = Process.objects.get(id= pk)
    output = list(set(number.result))

    return {"characters": output}