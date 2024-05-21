from community_app import create_app
from community_app.models.questions import Question, Statistic
from community_app.models.response import Response


if __name__ == '__main__':
    app = create_app()
    app.run()
