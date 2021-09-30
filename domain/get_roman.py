from app.models import Process, User

def get_roman(n, user_id):
    output = ""

    M = n // 1000
    C = n // 100 % 10
    D = n // 10 % 10
    U = n % 10

    output += M * "M"

    if C == 9:
        output += "CM"
    elif C >= 5:
        output += "D" + ((C - 5) * "C")
    elif C == 4:
        output += "CD"
    else:
        output += C * "C"

    if D == 9:
        output += "XC"
    elif D >= 5:
        output += "L" + ((D - 5) * "X")
    elif D == 4:
        output += "XL"
    else:
        output += D * "X"

    if U == 9:
        output += "IX"
    elif U >= 5:
        output += "V" + ((U - 5) * "I")
    elif U == 4:
        output += "IV"
    else:
        output += U * "I"

    user = User.objects.get(id=user_id)
    process = Process(decimal=n, result=output, user_id=user)
    process.save()

    return output