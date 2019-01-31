# Mixing Python `@abstractmethod`s With Other Decorators

**TL;DR** Support for abstract classes through Python's `ABC` module is a great way to enforce good object-oriented programming practices in your team's codebase. But the nature of its implementation means some care must be taken when mixing `@abstractmethod` with other decorators. This blog post covers how we resolved issues that arose when mixing `@abstractmethod` with the frequently-used `@cachedproperty` decorator, and how these issues can be resolved more generally in a Pythonic way.
