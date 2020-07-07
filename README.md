# fibonacci_flask_kubernetes
A sample python flask app, which returns n'th fibonacci number.
The app also contains a sample for pytest.

Multistage dockerfile is used for the test and build.

Since flask sever is only for development purposes, the app runs on gunicorn.
The application can be deployed in kubernetes with a multicontainer pod including nginx as sidecar.

references: 
- https://www.nayuki.io/page/fast-fibonacci-algorithms
- https://funloop.org/post/2017-04-14-computing-fibonacci-numbers.html#the-doubling-method
- https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code
- https://realpython.com/python-testing/#writing-integration-tests
- https://flask.palletsprojects.com/en/1.1.x/testing/#testing-flask-applications
- https://github.com/aviskase/testproject-api-example


ToDo:
- Add swagger api docs
- acceptance test run with docker-compose
- Authorization
- Add logs stdout
- openapi specification 