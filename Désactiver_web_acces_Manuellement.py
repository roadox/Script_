from netmiko import ConnectHandler

# Informations de connexion au commutateur Cisco
device = {
    'device_type': 'cisco_ios',
    'ip': 'IP_Address',
    'username': 'Username', 
    'password': 'MotDePasse',
}

# Connexion au commutateur
connection = ConnectHandler(**device)

# Vérification de la configuration actuelle pour l'accès Web
output = connection.send_command("show running-config | include ip http")

# Vérification si les lignes "ip http server" ou "ip http secure-server" sont présentes
if "ip http server" in output or "ip http secure-server" in output:
    print("L'accès Web est activé. Désactivation en cours...")
    
    # Entrer en mode de configuration
    connection.config_mode()

    # Désactivation de l'accès Web
    connection.send_command("no ip http server")
    connection.send_command("no ip http secure-server")

    # Sauvegarde de la configuration
    connection.send_command("write memory")

    print("L'accès Web a été désactivé avec succès.")
else:
    print("L'accès Web n'est pas activé sur ce commutateur.")

# Déconnexion du commutateur
connection.disconnect()