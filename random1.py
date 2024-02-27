
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Fungsi untuk melakukan dekripsi teks menggunakan kunci privat RSA
def decrypt_text(encrypted_text, private_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    encrypted_text = base64.b64decode(encrypted_text.encode())
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    return decrypted_text

# Kunci privat RSA yang digunakan untuk dekripsi
private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEApaXxZyZ1JCOGge7PxoGO2yMCL4O+/e6+JVfx90GStyVzD8lN\nZGmsZXYnWW3z48eSBrxjHuNfzb1NhWOPL/Pv+Ts+GoHAL88xnIgjgRlcrM6oPBok\nF0ZBfcYxurK2OGIto2S+VisMo2kupOO8ZrqoEbK733jGQmup1Ng2eCaqnfkGXKAk\nwgMYFEZjZp2drzY7yaGYMPndnWEFut5jnvUvIpnxroXejlFz1F83MHlcnoafFgqX\naDbBOZdgno2e4wuNGgTD4Cr3WYuG9Eafned4uliQBxStloY5wSRtd5UniXhQlvHz\nOQgnm3z7Ij/NZxEsfXC3XlrN47e1bFe1LoIJQQIDAQABAoIBABJFyso9hWrEAfaT\njsc3m7f75cXyxybpFv/U0pfbO4lZN9b4FmHTH92t4dOVQ9P+u/KjBZ6ex57RCOwD\n0mPgaXqBYN2I7le/x/nb0SnQr8bOwaNmoVBRc1BB5JKzG9N+rgjiCDaGZ22fwNHW\n3t2orblNEXkqcBlb2cdFRgXtQwErrX2hNiN7V+h3aBXRmyuBycoslkmaQanUMb0q\n8/K4K8XiHpmFrSazgH7B/ucp1WmfDvMUqW9REJUU6O0G6DfZvs7MLW52Uh+Tp7fp\nQtIfZ4COAdV9/dUt+R101aqh92Ro5uH433w33FUVKxT/Nw9tqkk394x2gfq+v99t\n9rnKHSkCgYEAvGVU/lFjFgXZjq8v70Hf+J/aRtUnb6dURTsZjLkBlplrKb5QP+W1\nQzfRI7ixRbmOdJiw0EWG2q0Zjn5XnQ5sKw4AIA1fu6JUvQAlQ1Rj/TnaiMiRJ+Po\nD3PeatlhA2u31RT2rV9MqqzTqvI62je9v73DiiNxSa6hKDay7Nu4nAkCgYEA4Rbw\ngYhUNuoEDDYDCW8axSQSqkPH3hwD+fjEJjVjPio0hctT8FRsd2ys0ytEf8icTp8q\nEdqIWZgesEwVFXhcPOvcZ6MoM7iINeySHm67RcjmFnQKE8mY/4FwsaWzoiTrywqD\nYHn20Udv23rmGbYjAX4gQxgyzl8RlL3Ib5wSQXkCgYEAiQ0+c3RJnO/MgNw5Btjp\nUjkX1YejFLqpt2NzBshfu2sIZmmof5Nf9fJZFp95druyQmgB2MF7hQGAIgUPP5YK\nYpfgx3BzQFCrTIMamIx/4OuBaxhdYKOPYg5ss1ZIGPD33u9NNHqrj04C/c0Ru0Xp\np98orQlzlKKRYmvIZj7BYeECgYEAo9oKC5ENFMh3V9g9j7GEQDwJJk6fAM1OC7qO\nNu4oJ0mb4EVp/gnGx4yhpjrZ61dCiW0Nt99n4Ch/NoC73Fw4cNSVJhA8JKJQ7Ugf\n+e1Lf/pFm9SuvUbEjEJSoc7om8DasHwftKw0ApZJE/E77T2L7/s7Svwjh9zmtGsO\nrEhldakCgYEAhEouHr9Z1SEQoTQaAI6B/5k4micCV90RnfZ1t3PWjBBHgMvHZ14f\nCm8qwGl3GnXv1bH9Pwdd+jow4pKr/9lk2x0On3Y/ntQymklVv/KydLWxgJlWDyXg\n+nsUhg+QTAus4WUAEInEt2Nmvd6XkTYsMI0le7Lwx4q1JnWYqGlm4Tg=\n-----END RSA PRIVATE KEY-----'

# Teks yang telah dienkripsi
encrypted_text = 'lPIokgn5d5kfJSAkUJEHgpeLqV8nkm3bZ9cGwlGp//ZTDysfxoDwBjf6zI1y1pZKe+z7WCMwN5kRj6/K5hCP5EjortMVGHsjT0F9yMY+1j5DbjHs4F2gc89ktelMRcZcKDSdTSxbP5ri4u0vSTAIF4mb+bO2mM97oioQJtSesOEEQQdaQa0LC/UgDQnrgfpBt9H6inZXhRV2V2qCqCxJoJk6vFWeQPl61x3koL7DHtogppH3euc5NAnrSZCz0mnh97XqFX2qPMcqUFFIzkhceK6B9zlwIhsKwnkhbxa6lj1IX1wi6uW36GUs0hzr8HyAhnuvJBgpPqZLKX09DO7F0Q=='

# Melakukan dekripsi teks
decrypted_text = decrypt_text(encrypted_text, private_key)
print("Decrypted Text:", decrypted_text)







# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import base64


# import base64

# # Fungsi untuk membuat pasangan kunci RSA
# def generate_key_pair():
#     key = RSA.generate(2048)
#     private_key = key.export_key()
#     public_key = key.publickey().export_key()
#     return private_key, public_key

# # Fungsi untuk melakukan enkripsi teks menggunakan kunci publik RSA
# def encrypt_text(text, public_key):
#     public_key = RSA.import_key(public_key)
#     cipher = PKCS1_OAEP.new(public_key)
#     encrypted_text = cipher.encrypt(text.encode())
#     return base64.b64encode(encrypted_text).decode()

# # Fungsi untuk melakukan dekripsi teks menggunakan kunci privat RSA
# def decrypt_text(encrypted_text, private_key):
#     private_key = RSA.import_key(private_key)
#     cipher = PKCS1_OAEP.new(private_key)
#     encrypted_text = base64.b64decode(encrypted_text.encode())
#     decrypted_text = cipher.decrypt(encrypted_text).decode()
#     return decrypted_text

# # Membuat pasangan kunci RSA
# private_key, public_key = generate_key_pair()
# print("Private Key:", private_key)
# print("Public Key:", public_key)

# # Teks yang akan dienkripsi
# plaintext = "4321lupa"

# # Melakukan enkripsi teks
# encrypted_text = encrypt_text(plaintext, public_key)
# print("Encrypted Text:", encrypted_text)

# # Melakukan dekripsi teks
# decrypted_text = decrypt_text(encrypted_text, private_key)
# print("Decrypted Text:", decrypted_text)
