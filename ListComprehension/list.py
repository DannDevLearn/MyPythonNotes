'''
En python existe algo muy poderoso que se llama ListComprehension, asi que tomaremos como base
el video de YouTube

    https://www.youtube.com/watch?v=SNq4C988FjU

'''

# Tenemos un arreglo y para iterarlo tenemos la manera clasica y usando list comprehension

fruits = ["apple", "lemon", "watermelo", "strawberries"]

# froma clasica\
for fruit in fruits:
    print(f"Clasic iteration: {fruit}")

# fList Comprehension
[print(f) for f in fruits]

# Ahora si queremos pasar a mayusculas debemos crear un nuevo arreglo
# pero con list comprehension no es necesario solo se reasigna

fruits = [f.upper() for f in fruits]
print(fruits)

# Ahora cabe mencionar que tmabien podemos usarlo para stirng manipulation

my_string = "HelloMyNameIsDann"

arr_string = [i for i in my_string] # esto creara un arreglo de caracteres

print(arr_string)

# Ahora podemos hacer mas con esto

result = "".join(
    [letter if letter.islower() else ' ' + letter for letter in arr_string ]
)[1:]

print(result) # Agregarmos espacios a cada palabra cuandi inicia con mayusculas