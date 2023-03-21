import flask
import chating
import asyncio
from functools import wraps

def async_action(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapped

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('./index.html')

@app.route('/recording',methods=['GET'])
@async_action
async def record():
    user = await chating.recoding()
    print(user)
    result = await chating.chat(user)
    fin = list(result.split('\n'))
    print(fin)

    return flask.render_template('./index.html',user=user,bot=fin)

if __name__ == '__main__':
    app.run(debug=True)