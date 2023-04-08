numero = 42;
divisor = 1;

while (divisor <= numero) {
    resto = numero % divisor;
    if (resto == 0) {
        printf("Divisor encontrado: %d \n", divisor);
    }
    divisor = divisor + 1;
}
