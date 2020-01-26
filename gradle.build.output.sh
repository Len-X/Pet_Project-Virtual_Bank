~/D/U/A/P/P/Python_Code [master]× » gradle build -PpyDistType="bdist_wheel --universal"                                              17:50:04
> Task :assemble UP-TO-DATE
> Task :check UP-TO-DATE

> Task :pythonRuntime
Installing virtualenv
Collecting virtualenv
  Using cached https://files.pythonhosted.org/packages/05/f1/2e07e8ca50e047b9cc9ad56cf4291f4e041fa73207d000a095fe478abf84/virtualenv-16.7.9-py2.py3-none-any.whl
Installing collected packages: virtualenv
Successfully installed virtualenv-16.7.9
Creating a virtual environment
Using base prefix '/Users/LenX/anaconda3'
New python executable in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/bin/python
Installing setuptools, pip, wheel...
done.

> Task :pythonDependencies
Installing dependencies in requirements.txt true
Requirement already satisfied: tabulate==0.8.6 in ./build/virtualenv/lib/python3.7/site-packages (from -r requirements.txt (line 1)) (0.8.6)
Requirement already satisfied: console-menu==0.6.0 in ./build/virtualenv/lib/python3.7/site-packages (from -r requirements.txt (line 2)) (0.6.0)
Requirement already satisfied: peewee==3.11.2 in ./build/virtualenv/lib/python3.7/site-packages (from -r requirements.txt (line 3)) (3.11.2)
Requirement already satisfied: pymysql==0.9.3 in ./build/virtualenv/lib/python3.7/site-packages (from -r requirements.txt (line 4)) (0.9.3)
Requirement already satisfied: six in ./build/virtualenv/lib/python3.7/site-packages (from console-menu==0.6.0->-r requirements.txt (line 2)) (1.13.0)
Downloading dependencies to /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/libs
Processing /Users/LenX/Library/Caches/pip/wheels/9c/9b/f4/eb243fdb89676ec00588e8c54bb54360724c06e7fafe95278e/tabulate-0.8.6-cp37-none-any.whl
Collecting console-menu==0.6.0
  Using cached https://files.pythonhosted.org/packages/db/00/b15db89f70b722d962ce3e3ab77b7135fa7493ae3189683272595980c865/console_menu-0.6.0-py2.py3-none-any.whl
Processing /Users/LenX/Library/Caches/pip/wheels/79/7e/1a/6c138b5e531b85670078781d92a14aefb7f3e7f81e56026118/peewee-3.11.2-cp37-cp37m-macosx_10_7_x86_64.whl
Collecting pymysql==0.9.3
  Using cached https://files.pythonhosted.org/packages/ed/39/15045ae46f2a123019aa968dfcba0396c161c20f855f11dea6796bcaae95/PyMySQL-0.9.3-py2.py3-none-any.whl
Collecting six
  Using cached https://files.pythonhosted.org/packages/65/26/32b8464df2a97e6dd1b656ed26b2c194606c16fe163c695a992b36c11cdf/six-1.13.0-py2.py3-none-any.whl
Installing collected packages: tabulate, six, console-menu, peewee, pymysql
  WARNING: The script tabulate is installed in '/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/libs/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed console-menu-0.6.0 peewee-3.11.2 pymysql-0.9.3 six-1.13.0 tabulate-0.8.6

> Task :pythonTest
Unit testing (pytest only)
Requirement already satisfied: pytest in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (5.3.2)
Requirement already satisfied: pytest-cov in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (2.8.1)
Requirement already satisfied: importlib-metadata>=0.12; python_version < "3.8" in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (1.3.0)
Requirement already satisfied: packaging in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (19.2)
Requirement already satisfied: more-itertools>=4.0.0 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (8.0.2)
Requirement already satisfied: attrs>=17.4.0 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (19.3.0)
Requirement already satisfied: pluggy<1.0,>=0.12 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (0.13.1)
Requirement already satisfied: wcwidth in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (0.1.8)
Requirement already satisfied: py>=1.5.0 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest) (1.8.1)
Requirement already satisfied: coverage>=4.4 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from pytest-cov) (5.0.1)
Requirement already satisfied: zipp>=0.5 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from importlib-metadata>=0.12; python_version < "3.8"->pytest) (0.6.0)
Requirement already satisfied: pyparsing>=2.0.2 in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from packaging->pytest) (2.4.6)
Requirement already satisfied: six in /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages (from packaging->pytest) (1.13.0)
============================= test session starts ==============================
platform darwin -- Python 3.7.3, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
rootdir: /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code
plugins: cov-2.8.1
collected 17 items

../../test/test_bank.py .................                                [100%]

=============================== warnings summary ===============================
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/_pytest/junitxml.py:436
  /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/_pytest/junitxml.py:436: PytestDeprecationWarning: The 'junit_family' default value will change to 'xunit2' in pytest 6.0.
  Add 'junit_family=legacy' to your pytest.ini file to silence this warning and make your suite compatible.
    _issue_warning_captured(deprecated.JUNIT_XML_DEFAULT_FAMILY, config.hook, 2)

/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
  /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236: DeprecationWarning: "PrimaryKeyField" has been renamed to "AutoField". Please update your code accordingly as this will be completely removed in a subsequent release.
    warnings.warn(s, DeprecationWarning)

/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236
  /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/virtualenv/lib/python3.7/site-packages/peewee.py:236: DeprecationWarning: "related_name" has been deprecated in favor of "backref" for Field objects.
    warnings.warn(s, DeprecationWarning)

-- Docs: https://docs.pytest.org/en/latest/warnings.html
- generated xml file: /Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/testReports/junit-output.xml -

---------- coverage: platform darwin, python 3.7.3-final-0 -----------
Name                                                                                                                Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------------------------------------------------------------------------
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/src/__init__.py       0      0   100%
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/src/bank.py          95      0   100%
/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/src/models.py        95     46    52%   61-63, 67-72, 77-82, 86, 90, 95-98, 102-109, 113-116, 120-125, 132-133, 137-142, 146-149
-------------------------------------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                                                 190     46    76%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml

======================== 17 passed, 8 warnings in 1.27s ========================

> Task :test

> Task :pythonBuild
Building package based on setup.py
Requirement already satisfied: wheel in ./build/virtualenv/lib/python3.7/site-packages (0.33.6)
running bdist_wheel
running build
running build_py
installing to build/bdist.macosx-10.7-x86_64/wheel
running install
running install_lib
creating build/bdist.macosx-10.7-x86_64/wheel
creating build/bdist.macosx-10.7-x86_64/wheel/test
copying build/lib/test/test_bank.py -> build/bdist.macosx-10.7-x86_64/wheel/test
copying build/lib/test/__init__.py -> build/bdist.macosx-10.7-x86_64/wheel/test
creating build/bdist.macosx-10.7-x86_64/wheel/src
copying build/lib/src/models.py -> build/bdist.macosx-10.7-x86_64/wheel/src
copying build/lib/src/__init__.py -> build/bdist.macosx-10.7-x86_64/wheel/src
copying build/lib/src/bank.py -> build/bdist.macosx-10.7-x86_64/wheel/src
running install_egg_info
running egg_info
writing Lena_s_Bank.egg-info/PKG-INFO
writing dependency_links to Lena_s_Bank.egg-info/dependency_links.txt
writing top-level names to Lena_s_Bank.egg-info/top_level.txt
reading manifest file 'Lena_s_Bank.egg-info/SOURCES.txt'
writing manifest file 'Lena_s_Bank.egg-info/SOURCES.txt'
Copying Lena_s_Bank.egg-info to build/bdist.macosx-10.7-x86_64/wheel/Lena_s_Bank-1.0-py3.7.egg-info
running install_scripts
creating build/bdist.macosx-10.7-x86_64/wheel/Lena_s_Bank-1.0.dist-info/WHEEL
creating '/Users/LenX/Desktop/University/Advanced_SE/Pet_Project/Pet_Project-Virtual_Bank/Python_Code/build/python-build/Lena_s_Bank-1.0-py2.py3-none-any.whl' and adding 'build/bdist.macosx-10.7-x86_64/wheel' to it
adding 'src/__init__.py'
adding 'src/bank.py'
adding 'src/models.py'
adding 'test/__init__.py'
adding 'test/test_bank.py'
adding 'Lena_s_Bank-1.0.dist-info/METADATA'
adding 'Lena_s_Bank-1.0.dist-info/WHEEL'
adding 'Lena_s_Bank-1.0.dist-info/top_level.txt'
adding 'Lena_s_Bank-1.0.dist-info/RECORD'
removing build/bdist.macosx-10.7-x86_64/wheel

> Task :build

Deprecated Gradle features were used in this build, making it incompatible with Gradle 7.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/6.0.1/userguide/command_line_interface.html#sec:command_line_warnings

BUILD SUCCESSFUL in 20s
4 actionable tasks: 4 executed