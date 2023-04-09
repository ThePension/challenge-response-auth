# challenge-response-auth
Client/Serveur authentication based on challenge-response

## Étudiants :

* Aubert Nicolas, ISC3il-b
* Comi Alessio, ISC3il-b

## Liste des packages nécessaires

- `hashlib` : Hachage
- `secrets` stantard library : Génération d'un `nonce` avec unicité forte (*for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.*)
    * https://docs.python.org/3/library/secrets.html

## Description

Dans le langage de votre choix et par groupe de deux, implémentez un client et un serveur d'authentification basé sur un challenge-response.

* Langage : Python 3.7

## Questions

**quel hachage cryptographique utilisez-vous et pourquoi ?**

* SHA-256, rapide, sécurisé, et utilisé dans la plupart des systèmes d'authentification.
* 256 bits de longueur, difficile à casser.

**quelles précautions pour le générateur aléatoire ?**
* Doit être cryptographiquement fort, et ne pas être prédictible (RNG)
    * Chaque challenge-response doit être unique afin de se protéger contre les "replay attacks"
* Il peut être intéressant de se baser sur le temps (date, heure, etc.) pour générer le nonce, afin d'éviter les attaques par messages retardés (*delayed message attacks*)
* Ici, on utilise `secrets` qui est une bibliothèque standard de python, qui utilise `os.urandom()` pour générer des nombres aléatoires

**quelles précautions pour la construction garantissant l'unicité du nonce ?**

* RNG de qualité cryptographique
* Utilisation de la date et de l'heure pour générer le nonce
* Stockage des challenges dans une base de données, afin de vérifier que le nonce n'a pas déjà été utilisé

**quelles précautions pour la durée de validité du nonce ?**

* Doit être valide pendant une courte durée
    * Réduire les attaques par messages retardés (*delayed message attacks*) et les attaques par messages répétés (*replay attacks*)

**le système garantit l'authentification du client mais ne protège pas d'attaques MitM (relais), ni n'assure l'authentification du serveur, que pourrait-on faire? (idées à proposer)**

* Certificats numériques
* Protocoles sécurisés (SSL/TLS, SSH, etc.)
* Authentification mutuelle
    * S'assurer aussi que le serveur est bien celui qu'il prétend être : https://en.wikipedia.org/wiki/Mutual_authentication
* Utiliser l'algorithme SCRAM pour éviter de stocker les mots de passe en clair : https://en.wikipedia.org/wiki/Salted_Challenge_Response_Authentication_Mechanism
