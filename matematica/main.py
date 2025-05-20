backend = ("Python", "Java", "C#", "Ruby")
frontend = ("JavaScript", "TypeScript", "Python", "HTML", "CSS")

# União: todas as liguagens
todas = backend | frontend 
print("Todas as linguagens:", todas)

# Inserção: linguagens usadas no front-end e no back-end
comum = backend & frontend 
print("Linguagens usadas nos dois:", comum)

# Diferença: Linguagens exclusivas do backend
exclusivo_backend = backend - frontend 
print("linguagens apenas do backend:", exclusivo_backend)