# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import inspect

from flask import flash


def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)


class ClassDict():
    """Utility class for setting/getting class attributes as a dict."""
    def as_dict(self):
        """Return public class attributes as a dictionary"""
        return {attr: getattr(self, attr) for attr in get_attrs(self)}

    def update(self, *argv, **kwargs):
        """Updates public class attributes

        Examples:
        >>> eg = ClassDict(); eg.a=0; eg.b=0
        >>> eg.update(os.environ())
        >>> eg.update(**os.environ())
        >>> eg.update(a=1, b=2)

        Invalid:
        >>> eg = ClassDict(); eg.a=0; eg.b=0
        >>> eg.update(1)  # positional argument must be a dict
        >>> eg.update(dict(a=1), b=2)  # only positional or kwards supported
        >>> eg.update(1, 2)  # only one position argument allowed
            """
        if argv:
            assert isinstance(argv, dict)
            assert not kwargs
            assert len(argv)==1
            kwargs = argv[0]
        for attr in get_attrs(self):
            cls = self.__annotations__.get(attr, None) or type(getattr(self, attr))
            val = kwargs.get(attr, None)
            if val is not None:
                setattr(self, attr, cls(val))


def get_attrs(class_or_instance):
    result = inspect.getmembers(class_or_instance, lambda a:not(inspect.isroutine(a)))
    result = [val[0] for val in result if not val[0].startswith("__")]
    return result