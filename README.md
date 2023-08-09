# Raytracing-with-Python

This project was created while studing about [_Ray Tracing in One Weekend_](https://raytracing.github.io/books/RayTracingInOneWeekend.html), where I was interested to implement the whole idea in Python and see how it looks.

Due to CPU limitations the output is noisy, and the multiprocess isn't implemented yet.

**Output**

![raytraced image](./output.png)

## Running the program in local.

### A. With Poetry

* The dependancy management is maintained by [Poetry](https://python-poetry.org/). Make sure you have it installed.
* Clone this repo to you local and cd to the directory.
* `poetry update`
* `poetry run python main.py`

### B. requirements.txt

* Clone this repo to you local and cd to the directory.
* `pip install -r requirements.txt`
* `python main.py`