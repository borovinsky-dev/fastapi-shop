<!--Приватный ключ -->
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:3072
<!-- Публичный -->
openssl pkey -in private.pem -pubout -out public.pem