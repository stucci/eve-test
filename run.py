# [Quickstart — Eve 1.1.5 documentation](https://docs.python-eve.org/en/stable/quickstart.html)

from eve import Eve
app = Eve()

if __name__ == '__main__':
    app.run()


"""
POST requests:
curl -d '[{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/people

GET requests:
curl http://127.0.0.1:5000/people/obama

POST requests:
curl -d '[{"name": "vscode", "type": ["IDE"]}, {"name": "vim", "type": ["editor"]}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/editors

GET requests:
curl http://127.0.0.1:5000/editors/vim
"""
