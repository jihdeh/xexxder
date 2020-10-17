## Sennder Task

#### Getting Started

  - clone project locally
  - Make sure to have docker and docker-compose installed
  - RUN `make` or RUN `docker-compose up` in project root
  - A `.env` is auto-generated on project build just to avoid you manually creating an env file yourself for "this test"
  - When project is done building head over to http://localhost:8000/movies/

### Running Tests, Lints and Type Checks
  In order to run other commands, to check test, lint and type, it is required to run the command `make setup_venv` to set the environment and setup venv. After running that command, the below can be run in no particular order.

  - make setup_venv  - important first step
  - make test
  - make type
  - make lint

#### Test
  - RUN `make test` this also shows coverage report
  - To view coverage report in html RUN `coverage html` this would add a `htmlcov` folder to the root project, head over to the index.html and open that in browser

#### Lint Check
  - RUN `make lint` , coding style guide -PEP8, black for formatting

#### Type Check
  - RUN `make type` , mypy type checker in use

## Notes

  #### Optimization

    - On first page load, response takes about 10secs
    - Redis handles caching on second page load
    - Code space/time complexity is O(n)T, O(n)S

  ### Can improve

    - One first page load, should display the page then add a loader instead of nothing showing up first
    - Other helpful feature would have been pagination.
    - Polling can be used to check and update data(if any) on the view at intervals

### Debug

  This project runs on python3 and pip3, if by chance you're using a different version and you run `make setup_env` you might encounter an error like the one below.

```
  make: pip3: no such file or directory

```

You can just go to the makefile and change `pip3` in `make setup_env` to `pip`, and that should fix it for you.