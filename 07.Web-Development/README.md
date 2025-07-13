# Fast API
- FastAPI is a python web-framework for building modern APIs
  - Fast (Performance)
  - Fast (Development)
- Key Notes
  - Few bugs: all data validation embedded
  - Quick & easy to use and learn
  - Robust
  - Standards: follows open api standards and json schema
- key facts
  - Built on top of Starlette for the web parts and Pydantic for the data parts
  - Asynchronous support: built-in support for async and await
  - Automatic interactive API documentation: Swagger UI and ReDoc
  - Dependency injection: built-in support for dependency injection

> Official Documentation:
> https://fastapi.tiangolo.com/


- Where does fast api fit within an application architecture?
  - web pages uses rest APIs to talk to the backend
  - the backend service you can write with fastapi which handles buisiness logics
  - with additional tools you can write full stack application


## Concepts
- Hello World
- Get
  - path parameters
  - query parameters
- 