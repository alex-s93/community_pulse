from community_app import create_app
from community_app.routers.questions import questions_bp
from community_app.routers.response import response_bp
from community_app.routers.categories import categories_bp


app = create_app()
app.register_blueprint(questions_bp)
app.register_blueprint(response_bp)
app.register_blueprint(categories_bp)

if __name__ == '__main__':
    app.run()
