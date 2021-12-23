# Django et HTMX

Envoyez des requêtes AJAX sans utiliser `JavaScript` ou `jQuery`.
Pour plus d'informations, veuillez consulter la [documentation officielle](https://htmx.org/docs) de **HTMX** ici.
Pour moi, il n'a jamais été aussi facile et simple de faire des requêtes AJAX qu'avec **HTMX**. Et si l'on y réfléchit longuement et assez  sérieusement, il apparaît qu'il (HTMX) se veut un concurrent sérieux de **React** ou encore **Vue**. Mais après, ça ne reste que mon point de vue.

## Ce repo

Dans ce repo, j'effectue juste deux sortes de requêtes (les deux plus connues) avec HTMX: **POST**, **GET** même si dans le fond, j'ai utilisé **DELETE**.

## Tester ce repo

```bash
pip install -r requirements.txt
```

```bash
python manage.py collectstatic
```

```bash
python manage.py runserver
```
