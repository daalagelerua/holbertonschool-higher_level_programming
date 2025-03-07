# ORM (Object Relationnal Mapping)

## Injection SQL

Les injections SQL sont un type de vulnérabilité de sécurité dans les applications web et les bases de données. Elles se produisent lorsque des attaquants parviennent à insérer (ou « injecter ») du code SQL malveillant dans une requête SQL, ce qui peut leur permettre de manipuler la base de données de manière non autorisée. L'attaque se produit généralement lorsque des entrées utilisateur ne sont pas correctement validées ou échappées avant d'être insérées dans une requête SQL.

### Comment cela fonctionne-t-il ?

Lorsqu'une application web ou une API interagit avec une base de données, elle construit souvent des requêtes SQL en utilisant des informations fournies par l'utilisateur, comme les paramètres dans une URL ou un formulaire. Si ces informations sont insérées directement dans la requête sans être correctement validées, un attaquant peut introduire du code SQL malicieux.

*Voici un exemple simple d'injection SQL* :

**Exemple vulnérable** :
Imaginons qu'une application cherche un utilisateur en fonction de son username et password :

```python
username = input("Username: ")
password = input("Password: ")

query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
```

*Si un utilisateur entre les valeurs suivantes* :

- username: admin
- password: ' OR '1'='1

**La requête devient** :

```sql
SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'
```

Dans ce cas, la condition OR '1'='1' est toujours vraie, ce qui permet à l'attaquant de se connecter à l'application sans connaître le mot de passe réel. Cela peut donner accès à des données sensibles ou permettre d'exécuter d'autres commandes malveillantes.

### Pourquoi cela fonctionne-t-il ?

L'injection SQL fonctionne parce que le code malicieux est inséré dans la requête SQL de manière telle que le système de gestion de base de données (SGBD) l'exécute sans distinction. Voici pourquoi cela se produit :

Construction de la requête sans validation : Si l'entrée de l'utilisateur est insérée directement dans une requête SQL sans être correctement vérifiée ou échappée, le système peut interpréter cette entrée comme du code SQL légitime.

Manipulation des chaînes SQL : Le code malicieux injecté peut modifier la logique de la requête SQL, comme nous l'avons vu avec OR '1'='1'. Cela peut faire en sorte que la requête retourne des résultats inattendus, ce qui permet à l'attaquant de contourner les restrictions d'accès.

### Pourquoi c'est un problème ?

Les injections SQL peuvent entraîner plusieurs conséquences graves, telles que :

- **Accès non autorisé aux données** :

L'attaquant peut accéder, modifier ou supprimer des données sensibles dans la base de données.

- **Exécution de commandes arbitraires** :

Un attaquant peut potentiellement exécuter n'importe quelle commande SQL, y compris des commandes pour supprimer des tables ou injecter des scripts malveillants.
- **Exposition des informations système** :

L'attaquant peut obtenir des informations sur la structure de la base de données (par exemple, les noms de tables et de colonnes), ce qui peut faciliter des attaques ultérieures.

- **Escalade de privilèges** :

Si l'attaquant parvient à exécuter des requêtes SQL dans le contexte d'un utilisateur ayant des privilèges élevés (comme un administrateur), il peut compromettre le système dans son ensemble.

### Comment prévenir les injections SQL ?

Pour protéger les applications contre les injections SQL, il existe plusieurs bonnes pratiques essentielles :

*Utilisation de requêtes paramétrées (ou préparées)* :

Les requêtes paramétrées empêchent l'injection SQL en séparant les données des instructions SQL. Les données sont envoyées séparément, de manière à ce qu'elles ne puissent pas être interprétées comme du code SQL.
Exemple avec MySQLdb :

```python
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
```

Ici, %s est un espace réservé pour les valeurs et elles sont transmises séparément, ce qui empêche toute manipulation malicieuse.

*Échapper les caractères spéciaux* :

Si tu dois absolument insérer des données directement dans une requête SQL (ce qui n'est pas recommandé), il faut échapper les caractères spéciaux comme ', ;, ou --, afin qu'ils ne soient pas interprétés comme des commandes SQL.

**Exemple** :

```python
query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(escape(username), escape(password))
```

*Vérification et validation des entrées* :

Toujours valider les données saisies par l'utilisateur pour s'assurer qu'elles sont dans le format attendu. Par exemple, pour un champ de type email, il faut vérifier que la donnée correspond à un format d'email valide.

*Privilèges minimaux* :

Limiter les privilèges de l'utilisateur de la base de données. Si l'application a seulement besoin de lire les données, n'accorde pas de privilèges d'écriture ou de suppression. Cela limite les dégâts en cas d'injection SQL réussie.

*Utilisation de ORM (Object-Relational Mapping)* :

Les ORM comme SQLAlchemy ou Django ORM génèrent automatiquement des requêtes SQL paramétrées et échappent les données, ce qui réduit le risque d'injection SQL.

### Conclusion

L'injection SQL est un vecteur d'attaque puissant, mais heureusement, il est relativement simple à prévenir en suivant les bonnes pratiques de sécurité. En utilisant des requêtes paramétrées, en validant les entrées et en réduisant les privilèges des utilisateurs, tu peux protéger efficacement ton application contre ce type de vulnérabilité