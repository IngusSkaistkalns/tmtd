# tmtd

"Tell me the digit" python flask example using trained keras model

## Dependencies

- Python 3 (`python3 --version`)
- PIP (`pip --version`)
- Flask (`flask --version`)
- dotenv files

## Digit number model

~~Downloaded from https://github.com/YakkaluruSathvik/Handwritten_Digit_Recognition/blob/main/model.h5~~

Replace model with trained from [model_mnist_0.keras](https://huggingface.co/wisetown/cnn-digit-recognizer/tree/main)

## Setup (MAC)

See https://flask.palletsprojects.com/en/stable/installation/

### Init virtual environment

```bash
$ python3 -m venv .venv
```

### Activate virtual environment

```bash
. .venv/bin/activate
```

### Install flask

```bash
$ pip install Flask
```

### Install dotenv support

```bash
$ pip install python-dotenv
```

### Install image recognition libraries

```bash
$ pip install tensorflow
$ pip install opencv-python
$ pip install numpy
$ pip install Pillow
```

## Start up

```bash
$ flask --app tmtd run --port=5001 --host=0.0.0.0 --debug
```
