import math

def calculoEntropia(dominio):
    probabilidad = [dominio.count(element) / len(dominio) for element in set(dominio)]
    return -sum(p * math.log(p,2) for p in probabilidad if p > 0)

if __name__ == "__main__":
    string = "123456"
    print(f"La entropia de '{string}' se aproxima a: {calculoEntropia(string):.3f} bits")

'''
RESPUESTA: La entropia de '123456' se aproxima a: 2.585 bits
'''