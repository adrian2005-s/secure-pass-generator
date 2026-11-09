import argparse
import random
import string


def generar_password(
    longitud=12,
    incluir_mayus=True,
    incluir_nums=True,
    incluir_simbolos=True,
):
  caracteres = string.ascii_lowercase
  if incluir_mayus:
    caracteres += string.ascii_uppercase
  if incluir_nums:
    caracteres += string.digits
  if incluir_simbolos:
    caracteres += string.punctuation

  if not caracteres:
    return "Error: Debes seleccionar al menos un tipo de caracter."

  return "".join(random.choice(caracteres) for _ in range(longitud))


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description="Generador seguro de contraseñas por CLI."
  )
  parser.add_argument(
      "-l",
      "--length",
      type=int,
      default=12,
      help="Longitud de la contraseña",
  )
  args = parser.parse_args()

  pwd = generar_password(longitud=args.length)
  print(f"Contraseña generada: {pwd}")