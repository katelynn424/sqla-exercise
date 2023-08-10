from unittest import Testcase

from app import app 
from models import db, Users


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///app_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UsersTestCase(Testcase):
    def test_homepage_redirect(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "http://localhost/users")

    def test_create_new_user_route(self):
        response = self.app.post('/users/new', data={
            'first_name': 'John',
            'last_name': 'Doe',
            'image_url': ''
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create_new_form_route(self):
        response = self.app.get('/users/new')
        self.assertEqual(response.status_code, 200)

    def test_show_user_route(self):
        user = User(first_name='Jane', last_name='Smith', image_url='')
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)