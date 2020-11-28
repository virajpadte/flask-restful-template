# Flask-restful-template
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

I have used flask for a lot of projects now and I realized very soon thaat having a consistent and structure to the flask app is needed as the flask routes increase. While flask documentation does not clearly mention a lot in this regard, based on some articles I read, I have come up with a good structure for using flask to develop containerized python APIs.


**Project Structure:**<br />

```
api/
    __init__.py       # contains all routes
    resources/        # contains all API resource and HTTP method implementations
        __init__.py
    common/           #common utilities
        __init__.py
config
    __init__.py       # loads config based on env variables
    settings.py       # contains all various environment based configurations
app.py                # instantiation of app based on current config
wsgi.py               # needed to allow gunicorn to connect to Flask application
```

**Setup Development environment:**<br />
```
cd flask-restful-template
virtualenv -p {your-current-python3-version} env
source env/bin/activate
pip3 install -r requirements.txt
```

**Using the Makefile:**<br />

***Running Locally:***<br />
make run-local

***Running in docker:***<br />
make run - will serve the API inside a docker container exposed on port 5001<br />
make up - will build and then serve the API inside a docker container exposed on port 5001<br />

***Stop and Cleanup:***<br />
make stop - will stop and remove the container<br />
make clean - will delete container image<br />

***Todos:***<br />
1. Add some debugging probe for local as well as in-container execution if possible
1. Add structure for tasks
2. Add structure for DB layer
3. Add structure for unit tests
4. Add structure for performance tests using k6 testing suite
4. Add structure for generating project documentation via code
5. Add support for swagger documentation
6. Extend support for running local and dockerized tests using make commands


### License Summary
This sample code is made available under the Apache License Version 2.0. See the LICENSE file.

### Keep contributing to Open Source
लोकाः समस्ताः सुखिनोभवंतु
