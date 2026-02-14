import csv

class OrcamentoImobiliaria:
    def __init__(self):
        self.taxa_contrato_total = 2000.00
        self.parcelas_contrato = 5
        self.valor_parcela_contrato = self.taxa_contrato_total / self.parcelas_contrato

    def calcular_aluguel(self, tipo, quartos, tem_garagem, tem_criancas, extras_estudio=0):
        valor_base = 0
        
        if tipo == "Apartamento":
            valor_base = 700.00
            if quartos == 2:
                valor_base += 200.00
            if tem_garagem:
                valor_base += 300.00
            if not tem_criancas:
                valor_base *= 0.95
                
        elif tipo == "Casa":
            valor_base = 900.00
            if quartos == 2:
                valor_base += 250.00
            if tem_garagem:
                valor_base += 300.00
                
        elif tipo == "Estudio":
            valor_base = 1200.00
            if extras_estudio == 2:
                valor_base += 250.00
            elif extras_estudio > 2:
                valor_base += 250.00 + ((extras_estudio - 2) * 60.00)
        
        return valor_base

    def gerar_csv(self, valor_mensal):
        # Defini o nome fixo aqui: orcamento_final.csv
        nome_arquivo = 'orcamento_final.csv'
        with open(nome_arquivo, mode='w', newline='') as ficheiro:
            writer = csv.writer(ficheiro, delimiter=';') # Mudei para ; para abrir fácil no Excel
            writer.writerow(['Parcela', 'Valor Aluguel', 'Parcela Contrato', 'Total Mensal'])
            
            for i in range(1, 13):
                p_contrato = self.valor_parcela_contrato if i <= 5 else 0.0
                total = valor_mensal + p_contrato
                writer.writerow([f"Mes {i}", f"{valor_mensal:.2f}", f"{p_contrato:.2f}", f"{total:.2f}"])
        return nome_arquivo

def executar():
    sistema = OrcamentoImobiliaria()
    
    print("--- Sistema de Orcamento R.M ---")
    print("1. Apartamento\n2. Casa\n3. Estudio")
    opcao = input("Tipo: ")
    
    tipo_imovel = "Apartamento" if opcao == "1" else "Casa" if opcao == "2" else "Estudio"
    
    quartos = 1
    garagem = False
    criancas = True
    vagas_estudio = 0
    
    if tipo_imovel in ["Apartamento", "Casa"]:
        quartos = int(input("Quantidade de quartos (1 ou 2): "))
        garagem = input("Deseja garagem? (s/n): ").lower() == 's'
        if tipo_imovel == "Apartamento":
            criancas = input("Possui criancas? (s/n): ").lower() == 's'
    else:
        vagas_estudio = int(input("Quantidade de vagas para o Estudio: "))

    mensalidade = sistema.calcular_aluguel(tipo_imovel, quartos, garagem, criancas, vagas_estudio)
    
    print(f"\nValor do Aluguel Mensal: R$ {mensalidade:.2f}")
    print(f"Taxa de Contrato: 5x de R$ {sistema.valor_parcela_contrato:.2f}")
    
    nome_gerado = sistema.gerar_csv(mensalidade)
    print(f"\nArquivo '{nome_gerado}' gerado com sucesso!")

if __name__ == "__main__":
    executar()
