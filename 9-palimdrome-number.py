class Solution:
    def isPalindrome(self, x: int) -> bool:
        invertido = str(x)[::-1]
        if str(x) == invertido:
            return True
        else:
            return False

# --- CÓDIGO PARA TESTAR LOCALMENTE ---
# 1. Instancia a classe
solucao = Solution()
# 2. Chama o método passando os argumentos de teste e exibe a resposta
resultado = solucao.isPalindrome(1210)
print("Resultado:", resultado)  # Saída esperada: False