## Decorators

A decorator in Python is a function that takes another function or class as input, extends or modifies its behavior, and returns it — usually without changing its actual source code.

Think of it as a “wrapper” that adds functionality around another function/class.

### Types of decorators

> This is based on what they are decorating

| Type | Notes/Observations | Examples |
|------|--------------------|----------|
| Function Decorators | Most commonly used | `@staticmethod`, `@classmethod`, `@property`, `@lru_cache` | 
| Class Decorators | These modify behaviour of whole class | Add `__repr__` method to class |
| Builtin Decorators | Included in the python implementation itself | `@staticmethod`, `@classmethod`, `@property` |
| Custom Decorators | Created by you as per the use case | Validator, Authentication, Timing |
| Parameterized Decorators | Decorators that accept parameters | `@repeat(3)` |
| Chained Decorators | When multiple decorators are stacked on a function | |