# virtualenv python 2.7.9
# web.py
# db: sqlite3

import web
from web import form

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/add', 'add',
    '/staff_list/', 'staff_list'
)

db = web.database(dbn='sqlite', db='dsoghrdb')

staff_register_form = form.Form(
    form.Textbox('staff_number'),
    form.Textbox('staff_name'),
)

class index:
    def GET(self):
        punch_ins = db.select('punch_in', order="created DESC")
        stafflists = db.select('stafflist')
        hr_items = [punch_ins, stafflists]
        return render.index(hr_items)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('punch_in', punch = i.punch)
        raise web.seeother('/')

class staff_list:
    def GET(self):
        staff_new = staff_register_form()
        return render.staff_list(staff_new)

    def POST(self):
        staff_new = staff_register_form()
        if staff_new.validates():
            db.insert('stafflist', **staff_new.d)
            raise web.seeother('/')
        else:
            return "Problems?"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
