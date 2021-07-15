
import Loggan_Language

while True:
    text = input('loggan > ')
    result, error = Loggan_Language.run(text)

    if error: print(error.as_string())
    else: print(result)
    