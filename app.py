from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security, current_user

from flask import redirect, url_for, request


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# admin panel
from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'text', 'tags']


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'posts']


admin = Admin(app, 'BlogApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)