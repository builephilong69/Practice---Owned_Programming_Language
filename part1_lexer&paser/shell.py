import loggan

while True:
    text = input('loggan > ')
    result,error = loggan.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)