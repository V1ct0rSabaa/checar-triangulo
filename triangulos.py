def mostrar_tipo_triangulo(x: float, y: float, z: float) -> str:
    tipo_triangulo: tuple[str] = ("equilátero", "isóceles", "escaleno")
    mensagem: str = ""
    if x > y + z or y > x + z or z > x + y: # condição impossivel para formar um triangulo
        mensagem = f"Um dos valores do triângulo não deve ser maior que os outros 2 valores, X: {x:.2f} Y: {y:.2f} e Z: {z:.2f} não formam um triângulo"
    else: 
        if x == y and x == z:
            mensagem = "X, Y e Z são iguais, logo formam um triângulo " + tipo_triangulo[0]
        elif x == y and x != z or x == z and x != y or y == z and x != y:
            if x == y:
                mensagem = "X e Y são iguais, mas Z é diferente logo formam um triângulo " + tipo_triangulo[1]
            elif x == z:
                mensagem = "X e Z são iguais, mas Y é diferente logo formam um triângulo " + tipo_triangulo[1]
            else:
                mensagem = "Y e Z são iguais, mas X é diferente logo formam um triângulo " + tipo_triangulo[1] 
        elif x != z and x != y:
                mensagem = "X, Y e Z são diferentes, logo formam um triângulo " + tipo_triangulo[2]
    return mensagem


def mostrar_menu() -> None: 
    menu: str = "1- digitar valores e checar se formam um triângulo\n2- sair do programa: "
    print("Bem vindo ao Programa para formar triângulos")
    continuar: bool = True
    while continuar:
        entrada = input(menu)
        try:
            entrada = int(entrada)
            if entrada == 1:
                x = float(input("digite o valor do lado X: "))
                y = float(input("digite o valor do lado Y: "))
                z = float(input("digite o valor do lado Z: "))
                print(mostrar_tipo_triangulo(x, y, z))
            elif entrada == 2:
                continuar = False
            else:
                print("Opção inválida, não digite numeros diferentes de 1 ou 2.")
        except ValueError:
            print("Opção inválida, digite apenas 1 ou 2")
    print("Fim do programa.")


mostrar_menu()