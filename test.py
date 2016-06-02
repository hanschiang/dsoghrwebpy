# virtualenv python 2.7.9
# web.py
# db: sqlite3

import web

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/add', 'add'
)

db = web.database(dbn='sqlite', db='testdb')

class index:
    def GET(self):
        todos = db.select('todo2', order="created DESC")
        stafflists = db.select('stafflist')
        tant = [todos, stafflists]
        return render.index(tant)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo2', title = i.title)
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()