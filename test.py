import matplotlib.pyplot as plt

x1 = [0, 1, 2, 5, 7, 8, 10]
y1 = [18, 10, 5, 0, 0, 3, 12]
x2 = [-4, -3, -2, 1, 6, 7, 9]
y2 = [18, 10, 5, 0, 0, 3, 12]
a = 1
b = 4 

# Créer une figure avec 1 ligne et 2 colonnes
# plt.figure(figsize=(10, 4)) # Optionnel : définit la taille de la fenêtre

# --- Premier graphique (en haut) ---
plt.subplot(2, 1, 1) 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x1[:4], y1[:4], marker = 'o', linestyle = '-', color = 'red') # Triangle rouge

plt.plot(x1[4:], y1[4:], marker = 'o', linestyle = '-', color = 'blue') # Triangle blue

plt.plot(x1[3:5], y1[3:5], marker = 'o', linestyle = '-', color = 'orange', label = "range from x0 to x1") # Triangle jaune
plt.legend()

# --- Deuxième graphique (en bas) ---
plt.subplot(2, 1, 2)
plt.xlabel('x')
plt.ylabel('x --> min f over [x+1,x+4]')
plt.plot(x2[:4], y2[:4], marker = 'o', linestyle = '-', color = 'red', label = "shift b units to the left") # Triangle rouge

plt.plot(x2[4:], y2[4:], marker = 'o', linestyle = '-', color = 'blue', label = "shift a units to the left") # Triangle blue

plt.plot(x2[3:5], y2[3:5], marker = 'o', linestyle = '-', color = 'orange', label = "range from x0 to x1") # Triangle jaune

plt.legend()
plt.tight_layout() # Ajuste automatiquement les marges pour éviter les chevauchements
plt.show()