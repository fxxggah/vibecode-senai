populacao = float(input("Digite a população atual do município: "))
taxa = 0.0089

print("\n--- Previsão do Crescimento Populacional ---")

for ano in range(1, 26):
    populacao = populacao * (1 + taxa)
    
    print(f"Ano {ano:02d}: {int(populacao)} habitantes")