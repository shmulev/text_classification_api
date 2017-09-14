# -- Load library --
import os
from __init__ import app

# from __init__ import db

port = int(os.getenv("PORT", 5000))

# -- Main --
if __name__ == '__main__':
    ###############################################################################
    # Main - App Start here
    ###############################################################################
    # db.create_all()
    app.run(host='0.0.0.0', port=port, threaded=True)
# -- // Main --
