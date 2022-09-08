

letras=['A','B','C','D','b','c','d','a']
letrasFinal=['Z','z','X','x','Y','y']

print (letras)

letras.sort(key=str.lower)
print (letras)

letras.append(('E','e'))
print (letras)

letras.pop(4)
print (letras)

letras.extend(letrasFinal)
print (letras)

letras.remove('X')
print (letras)

letras.reverse()
print (letras)

letras.copy()
print (letras)

a=letras.count('a')
print (a)

x=letras.index('x')
print (x)

letras.insert(len(letras),'M')
print (letras)

#index,insert

#print(dir(letras))

