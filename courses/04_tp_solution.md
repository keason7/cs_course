# TP Qui suis-je ?

## Solution

```python
def main():
    print("Bonjour")

    # recupere les informations utilisateur
    prenom = input("Quel est votre prénom ?\n")
    nom = input("Quel est votre nom ?\n")
    age = input("Quel est votre age ?\n")
    metier = input("Quel est votre métier ?\n")
    hobbie = input("Quel est votre hobbie ?\n")
    orientation_politique = input("Quel est votre orientation politique ?\n")

    # affiche les informations utilisateur
    print("\nMerci pour ces informations. Si je bien compris:")
    print(f"Vous vous appelez {prenom} {nom}")
    print(f"Vous avez {age} ans")
    print(f"Mais je vous aurais donné {int(age) - 4}")
    print(f"Vous travaillez en tant que {metier}")
    print(f"Vous aimez le hobbie suivant: {hobbie}")
    print(f"Vous avez l'orientation politique suivante: {orientation_politique}")

    print("Bonne journée")

if __name__ == "__main__":
    main()
```
