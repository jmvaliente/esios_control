# esios_control
Control esios para el precio de la electricidad en Python

Con esta aplicación podemos conocer el precio por hora de una tarifa general y hacer actuaciones como conectar o desconectar elementos de la red eléctrica para poder optimizar el consumo eléctrico. Esto se puede realizar con relés o con interruptores inalámbricos controlados por ESP8266. Se puede usar con una Raspberry Pi.

Un ejemplo es la modificación de un interruptor Sonoff basado en ESP8266. Es un interruptor inalámbrico muy económico que permite una reprogramación usando un convertidor a serial FTDI.

Con esto podemos configurar abrir o cerrar nuestro interruptor cuando el precio de la electricidad este caro o barato.

Es necesario un token para la descarga de información. Este se puede pedir en la pagina https://api.esios.ree.es/
