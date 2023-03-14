# challenge-response-auth
Client/Serveur authentication based on challenge-response

## Description

Dans le langage de votre choix et par groupe de deux, implémentez un client et un serveur d'authentification basé sur un challenge-response.

## Questions

**quel hachage cryptographique utilisez-vous et pourquoi ?**

**quelles précautions pour le générateur aléatoire ?**

**quelles précautions pour la construction garantissant l'unicité du nonce ?**

**quelles précautions pour la durée de validité du nonce ?**

**le système garantit l'authentification du client mais ne protège pas**

**d'attaques MitM (relais), ni n'assure l'authentification du serveur, que pourrait-on faire? (idées à proposer)**

Indications

la partie réseau n'est pas nécessaire: des appels de fonctions simples sont autorisés.

Voir https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication
Tenir compte des recommandations hash, crypto, PRNG
