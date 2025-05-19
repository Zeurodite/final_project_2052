from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Article
from app.forms import ArticleForm
from datetime import datetime

article_bp = Blueprint('article', __name__)

@article_bp.route('/articles')
@login_required
def articles():
    if current_user.role.name == "Admin":
        articles = Article.query.all()
    else:
        articles = Article.query.filter_by(author_id=current_user.id).all()
    return render_template('article/articles.html', articles=articles)

@article_bp.route('/articles/create', methods=['GET', 'POST'])
@login_required
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            publication_date=datetime.now(),
            status=form.status.data,
            author_id=current_user.id
        )
        db.session.add(new_article)
        db.session.commit()
        flash('Artículo creado exitosamente.')
        return redirect(url_for('article.articles'))
    return render_template('article/article_form.html', form=form)

@article_bp.route('/articles/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author_id != current_user.id and current_user.role.name != "Admin":
        flash("No tienes permiso para editar este artículo.")
        return redirect(url_for('article.articles'))
    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.content.data
        article.category = form.category.data
        article.status = form.status.data
        db.session.commit()
        flash('Artículo actualizado correctamente.')
        return redirect(url_for('article.articles'))
    return render_template('article/article_form.html', form=form)

@article_bp.route('/articles/delete/<int:article_id>')
@login_required
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author_id != current_user.id and current_user.role.name != "Admin":
        flash("No tienes permiso para eliminar este artículo.")
        return redirect(url_for('article.articles'))
    db.session.delete(article)
    db.session.commit()
    flash('Artículo eliminado correctamente.')
    return redirect(url_for('article.articles'))