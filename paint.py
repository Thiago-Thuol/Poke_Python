def verde(input_text):
    return (f"{"\033[32m"}{input_text}{"\033[0m"}")
def amarelo(input_text):
    return (f"{"\033[33m"}{input_text}{"\033[0m"}")
def vermelho(input_text):
    return (f"{"\033[31m"}{input_text}{"\033[0m"}")
def branco(input_text):
    return (f"{"\033[37m"}{input_text}{"\033[0m"}")

print (branco("oi"))
