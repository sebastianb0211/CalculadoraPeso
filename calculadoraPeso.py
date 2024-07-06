usuarios = []

def registrar_usuario():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso (kg): "))
    estatura = float(input("Ingrese la estatura (m): "))
    genero = input("Ingrese el género (M/F): ")
    
    usuario = {
        'nombre': nombre,
        'edad': edad,
        'peso': peso,
        'estatura': estatura,
        'genero': genero
    }
    
    usuarios.append(usuario)
    print("Usuario registrado exitosamente.\n")

def calcular_peso_ideal():
    for usuario in usuarios:
        estatura_cm = usuario['estatura'] * 100
        if usuario['genero'].lower() == 'm':
            peso_ideal = 50 + 0.91 * (estatura_cm - 152.4)
        else:
            peso_ideal = 45.5 + 0.91 * (estatura_cm - 152.4)
        
        imc = usuario['peso'] / (usuario['estatura'] ** 2)
        
        print(f"{usuario['nombre']}, su peso ideal es {peso_ideal} kg.")
        print(f"Su IMC actual es {imc}.")

        if imc < 18.5:
            print("Está por debajo de su peso ideal.")
        elif 18.5 <= imc < 24.9:
            print("Está dentro de su peso ideal.")
        elif 25 <= imc < 29.9:
            print("Está por encima de su peso ideal (sobrepeso).")
        else:
            print("Está por encima de su peso ideal (obesidad).")
        print("\n")

def visualizar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.\n")
        return
    
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print(f"Peso: {usuario['peso']} kg")
        print(f"Estatura: {usuario['estatura']} m")
        print(f"Género: {usuario['genero']}")
        print("\n")

def main():
    while True:
        print("Menú:")
        print("1. Registrar usuario")
        print("2. Calcular peso ideal")
        print("3. Visualizar usuarios")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            calcular_peso_ideal()
        elif opcion == '3':
            visualizar_usuarios()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.\n")

# Ejecutar la función main de una forma natural
main()
