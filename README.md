pandoc-d2-filter
================

Pandoc filter to convert d2 code blocks to images.

````
```{.d2 pad=20}
x -> y
```
````

## Usage

Install it with pip:

```
pip install pandoc-d2-filter
```

And use it like any other pandoc filter:

```
pandoc tests/testdata/default.md -o default.pdf --filter pandoc-d2
```

The d2 binary is either part of the `$PATH`
or can be configured via `D2_BIN` environment variable.
If you use other output formats than svg,
you should `d2 init-playwright` before the first use.

## Configuration

TODO check `tests/testdata` for now.

## Inspiration

This filter is heavily inspired by the
[JavaScript d2-filter](https://github.com/ram02z/d2-filter)
and the [pandoc-plantuml-filter](https://github.com/timofurrer/pandoc-plantuml-filter).

Thanks [Omar](https://github.com/ram02z) & [Timo](https://github.com/timofurrer)
