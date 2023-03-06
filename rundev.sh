#!/bin/bash
export FLASK_ENV=development
export FLASK_DEBUG=0
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export ACTIVITY_LOGGER_URL=http://0.0.0.0:5001
flask run --host=0.0.0.0 --port=8082
