import os

from flask_failsafe import failsafe


@failsafe
def create_app():
    # note that the import is *inside* this function so that we can catch
    # errors that happen at import time
    from buddle_core import app
    return app


if __name__ == "__main__":
    # Watch the templates folder for changes too
    extra_dirs = [
        os.path.abspath(os.path.dirname(__file__)) + "/buddle_core/templates",
    ]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)

    app = create_app()
    app.templates_auto_reload = True

    app.run(host="0.0.0.0", debug=True, extra_files=extra_files, port=os.environ.get('PORT'))