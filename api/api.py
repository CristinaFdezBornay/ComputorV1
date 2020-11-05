import time
from flask import Flask

app = Flas(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}
