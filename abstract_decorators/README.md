# Safely Mixing Python Decorators

**TL;DR** Decorators are a super useful Python feature that unfortunately run into limitations when used in combination. This blog post and the accompanying notebook delve into why these issues happen and how you can make sure your decorators don't have these problems!

## Why Use Decorators?

Python decorators are a fantastic way to add reusable components to a function's implementation. From a technical perspective, decorators are merely syntactic sugar for a function call, so that

```
from boltons.cacheutils import cached

@cached(cache={})
def fib(n):
    if n == 0 or n == 1:
    	return 1

    return fib(n-1) + fib(n-2)
```

is equivalent to

```
from boltons.cacheutils import cached

def fib(n):
    if n == 0 or n == 1:
    	return 1

    return fib(n-1) + fib(n-2)

fib = cached(cache={})(fib)
```

But in practice, they've become a widespread way to extend functionality of a function in a very readable way. The super-popular [Flask service framework](http://flask.pocoo.org/docs/1.0/quickstart/) uses them to route endpoints to Python functions

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## Mixing Decorators

Despite how useful they are, decorators are a little bit notorious for being hard to combine. This is particularly problematic when one of the decorators sets and reads attributes defined on the function object itself. If you paid close attention in the `fib` example above, you'll notice that the original `fib` function gets overridden by a new definition that doesn't necessarily maintain the attributes of the original function. The attached Jupyter notebook goes into this issue in more depth for one particular pair of decorators, which I was able to resolve and contribute a fix back to the `boltons` library.
