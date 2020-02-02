"""
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
"""

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in resultado:
    print(i)


