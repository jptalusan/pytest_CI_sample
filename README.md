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

# Git commands
Since we already have this boilerplate, might as well set up some boilerplate for branching and feature development.

## Branching for feature development
Assuming you just cloned the repo and want to create a new feature or have updated your local code with the changes you intended to commit and push:
```
  git checkout -b <branch name> 
  git branch
```
After you are done, you can either do a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) if you are not able to edit main, or you can merge your branch and its changes to main.
```
  git checkout main
  git merge <branch name>
```
If there are conflicts due to your branch being outdated with other newer changes in main then you can update it first. Which is essentially the reverse of the previous command.
```
  git checkout <branch name>
  git merge main
```
Try to do this after you add a function and the corresponding test case for it.

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
* Extra useful information: https://www.varonis.com/blog/git-branching#:~:text=To%20merge%20branches%20locally%2C%20use,branch%20into%20the%20main%20branch.
  * **Merging Branches in a Local Repository**: To merge branches locally, use git checkoutto switch to the branch you want to merge into. This branch is typically the main branch. Next, use git mergeand specify the name of the other branch to bring into this branch. This example **merges the jeff/feature1 branch into the main branch**. Note that this is a fast-forward merge.
  ```
    git checkout main
    git merge jeff/feature1
  ```

  * **Merging Main into a Branch**: While you are working on your branch, other developers may update the main branch with their branch. This action means your branch is now out of date of the main branch and missing content. You can **merge the main branch into your branch** by checking out your branch and using the same git merge command.
  ```
    git checkout <branch name>
    git merge main
  ```