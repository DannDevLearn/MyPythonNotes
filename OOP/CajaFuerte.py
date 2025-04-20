class CajaFuerte:
    def __init__(self, clave: str, cantidad: int):
        self.__clave = clave
        self.__cantidad = cantidad

    def get_clave(self) -> str:
        return self.__clave

    def get_cantidad(self) -> int:
        return self.__cantidad
    # Los set se hacen muy similar usando self

caja = CajaFuerte("123", 5000)

print(caja.get_clave())
print(caja.get_cantidad())