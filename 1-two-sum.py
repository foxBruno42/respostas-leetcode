#######################################################################################################
## 1. Two Sum                                                                                        ##
## Diferente do URI, o leetcode cria classes e as executam, nao faço uso dos inputs.                 ##
## Achei algo um pouco disruptivo do que estou acostumado, mas é interessante.                       ##
## Para testar localmente, instancio a classe e chamo o método passando os argumentos de teste.      ##
## O problema consiste em encontrar dois números em uma lista que somados resultem em um valor alvo. ##
## A função deve retornar os índices desses dois números.                                            ##
#######################################################################################################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# --- CÓDIGO PARA TESTAR LOCALMENTE ---
# 1. Instancia a classe
solucao = Solution()
# 2. Chama o método passando os argumentos de teste e exibe a resposta
resultado = solucao.twoSum([2, 7, 11, 15], 9)
print("Resultado:", resultado)  # Saída esperada: [0, 1]