from flask import Blueprint,render_template, request, redirect, url_for, g

from todor.auth import login_required

from .models import User
from todor import db
from forms import UserForm


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)  # Carga los datos del usuario en el formulario
    
    if form.validate_on_submit(): 
        id = request.form.get('id')  # Obtén el id enviado desde el formulario
        #if int(id) != user.id:
         #   abort(403)  # Evita modificaciones no autorizadas
        # Actualizar los datos del usuario
        form.populate_obj(user)
        db.session.commit()
      #  flash("Usuario actualizado correctamente.", "success")
        return redirect(url_for('user.edit_user',id=user.id))  # Cambia según tus rutas user=user
    
    return render_template('account/profile.html', form=form, user=user)
