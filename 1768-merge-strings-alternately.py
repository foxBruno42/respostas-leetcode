class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1
        return ''.join(merged)

# --- CÓDIGO PARA TESTAR LOCALMENTE ---
# 1. Instancia a classe
solucao = Solution()
# 2. Chama o método passando os argumentos de teste e exibe a resposta
resultado = solucao.mergeAlternately('quota','wordi')
print("Resultado:", resultado)  # Saída esperada: [0, 1]