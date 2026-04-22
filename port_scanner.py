import socket

# Pobranie celu od użytkownika
target = input("Podaj adres IP lub domenę do skanowania: ")
ports = [21, 22, 80, 443]

print(f"\nSkanowanie celu: {target}...\n") 

for p in ports:
    # 1. Tworzymy socket (IPv4, TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Ustawiamy timeout (pół sekundy), żeby nie czekać w nieskończoność
    s.settimeout(0.5)
    
    # 3. Próbujemy nawiązać połączenie (connect_ex zwraca kod błędu zamiast rzucać wyjątek)
    result = s.connect_ex((target, p))
    
    # 4. Jeśli wynik to 0, port jest otwarty
    if result == 0:
        print(f"Port {p:3}: OTWARTY")
    else:
        print(f"Port {p:3}: ZAMKNIĘTY")
        
    # 5. Zamykamy socket, aby zwolnić zasoby systemowe przed kolejną iteracją
    s.close()

print("\nSkanowanie zakończone.")
