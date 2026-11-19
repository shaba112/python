

def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == n:
        return True
    else:
        return False

