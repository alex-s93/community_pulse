from datetime import datetime

from community_app import db


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete="CASCADE"), nullable=False)

    responses = db.relationship('Response', backref='question', lazy=True)

    def __str__(self):
        return f"Question: {self.text}"


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    questions = db.relationship('Question', backref='category', lazy=True)

    def __str__(self):
        return f"Category - {self.name}"


class Statistic(db.Model):
    __tablename__ = 'statistics'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    agree_count = db.Column(db.Integer, nullable=False, default=0)
    disagree_count = db.Column(db.Integer, nullable=False, default=0)

    def __str__(self):  # default= return self -> <__init__.questions.Statistics object at asdnf9823asndf>
        return "Statistic of Question '{}': {} of agree, {} of disagree".format(
            self.question_id, self.agree_count, self.disagree_count
        )
