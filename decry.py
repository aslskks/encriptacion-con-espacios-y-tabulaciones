def decode(file):
    with open(file, "r") as f:
        data = f.read()
        for index in range(0, len(data), 8):
            letra = ""
            for char in data[index:index+8]:
                if char == " ":
                    letra += '0'
                else:
                    letra += '1'
            letra = chr(int(letra, 2))
            print(letra, end= '')

elecion = int(input("1: cambiar nombre\n2: usar file.txt como nombre\n: "))

file = ""

if elecion == 1:
    file = input("cual es el nombre: ")
else:
    file ="file.txt"

decode(file)