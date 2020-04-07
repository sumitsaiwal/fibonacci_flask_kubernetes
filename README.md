# fibonacci_flask_kubernetes
A sample python flask app, which returns n'th fibonacci number.
The app also contains a sample for pytest.

Multistage dockerfile is used for the test and build.

Since flask sever is only for development purposes, the app runs on gunicorn.
The application can be deployed in kubernetes with a multicontainer pod including nginx as sidecar.

