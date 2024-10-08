# system imports

# relative imports
from forum import create_app, socketio

##########################################
# Initialize the Flask app
##########################################

app = create_app()
socketio.init_app(app, cors_allowed_origins="*")