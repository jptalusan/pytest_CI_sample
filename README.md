# pytest_CI_sample
Learning about how pytest and CI for python

# PyTest and Coverage
You can run pytests using:
```
      - name: Test with pytest  
        run: |  
          coverage run -m pytest  -v -s
```
Or
```
      - name: Test with pytest
        run: |
          pip install pytest pytest-cov
          pytest -v -s --doctest-modules --junitxml=junit/test-results-${{ matrix.python-version }}.xml --cov=. --cov-report=xml --cov-report=html
```
Then coverage can be reported using:
```
      - name: Generate Coverage Report  
        run: |  
          coverage report -m
```

# References
* https://pytest-with-eric.com/integrations/pytest-github-actions/
* https://bas.codes/posts/python-pytest-introduction
* https://stackoverflow.com/questions/75036841/unittest-directory-structure-cannot-import-src-code
    * Using `__init__.py` is not suggested, instead use `pytest.ini` in root to update PYTHONPATH.
* https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#introduction
* https://stackoverflow.com/questions/60776736/warning-failed-to-generate-report-no-data-to-report-error-in-python-using-pyte
    * Running pytest on a directory
    * Or you can just use coverage instead of pytest-cov since it just calls coverage in the background:
        Instead of this:
        ```
        - name: Test with pytest
        run: |
          pip install pytest pytest-cov
          pytest --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html
        ```

        Use this:
        ```
      - name: Test with pytest  
        run: |  
          coverage run -m pytest  -v -s  
      - name: Generate Coverage Report  
        run: |  
          coverage report -m
        ```