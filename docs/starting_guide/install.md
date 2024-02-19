# Installation `aPlot`

You can install the `aplot` library using either pip or by pulling the repository directly from GitHub.

## Option 1: Install via Pip

Open your terminal and run the following command

```sh
pip install aplot
```

## Option 2: Install from GitHub

You can also install `aplot` directly from its GitHub repository. This option is useful if you want to work with the latest development version or if you need to customize the library. Here's how to do it:

1. Clone the `aplot` repository from GitHub using the following command:

```sh
git clone https://github.com/kyrylo-gr/aplot.git
```

2. Enter the directory and install the package.

```sh
cd aplot
pip install -e .
```

`-e` allows you to link the library to the directory that you created, therefore allows you to change the code inside this directory.
Instead `pip install -e .` you can run `python setup.py develop` if you prefer.

## That's it!

You've successfully installed the `aplot` library. You can now start incorporating `aplot` into your Python projects.

For further insight, please refer to the [First Steps guide](first_steps.md).
