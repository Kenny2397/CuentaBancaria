from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(8,1000)
cuenta2 = CuentaBancaria(5,1000)

cuenta1.deposito(100).deposito(100).deposito(100).retiro(100).generar_interes().mostrar_info_cuenta()

cuenta2.deposito(100).deposito(100).retiro(100).retiro(100).retiro(100).retiro(100).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()
