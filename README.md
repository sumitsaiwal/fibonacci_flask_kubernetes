# fibonacci_flask_kubernetes
A sample python flask api, which returns n'th fibonacci number.

This is a tutorial project, which demonstrates lifecycle of a microservice in terms of DevOps.

##Topics Covered in the project
  - sample api : flask
  - unit test : pytest
  - integration test : pytest
  - api test : tavern, pytest
  - build : docker
  - continuous integration : github action, docker-compose
  - Deployment : kubernetes

Multistage dockerfile is used to run the test and build.

Since flask sever is recomended only for development purposes, the app runs on gunicorn.
This application can be deployed in kubernetes as a multicontainer pod (nginx as sidecar) with the following command:
```bash
kubectl create -f fibonacci-k8s.yaml
```

references: 
- https://www.nayuki.io/page/fast-fibonacci-algorithms
- https://funloop.org/post/2017-04-14-computing-fibonacci-numbers.html#the-doubling-method
- https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code
- https://realpython.com/python-testing/#writing-integration-tests
- https://flask.palletsprojects.com/en/1.1.x/testing/#testing-flask-applications
- https://tavern.readthedocs.io/en/latest/
- https://github.com/docker/compose/issues/2791


ToDo:
- swagger api docs
- authorization
- logger >> stdout
- openapi specification 