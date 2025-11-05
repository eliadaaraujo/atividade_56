# Receba uma frase e mostre:
# Quantas letras possui (ignorando espaços).
# Quantas vezes a letra “a” aparece (maiúscula ou minúscula).
# Em que posição ocorre a primeira e a última letra “a”.


frase = input("Digite uma frase: ")

letras = len(frase.replace(" ", ""))
quant_a = frase.lower().count("a")
primeiro_a = frase.lower().find("a") + 1
ultimo_a = frase.lower().rfind("a") + 1

print("Quantidade de letras (sem espaços):", letras)
print("Quantidade de letras 'a':", quant_a)
print("Posição do primeiro 'a':", primeiro_a)
print("Posição do último 'a':", ultimo_a)
