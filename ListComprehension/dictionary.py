'''
Video de aporendisaje

    https://www.youtube.com/watch?v=khCzymLy_QE

Asi como tenemos lo que es list comprehension igual podemos usar diccioanrios o mapas
'''

names = ["Dann", "Gandalf", "Germinio"]
profs = ["Prgrammer", "Wizard", "Millionary"]

'''
my_dictionary = {
    names[i]:profs[i] for i in range(len(names))
}
'''

my_dictionary = {
    key:value for (key, value) in zip(names, profs)
}
print(my_dictionary)