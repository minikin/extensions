# Benchmark of Swift extensions vs methods

- Swift version: 5.1.2
- Updated: 12.11.2019

[![Results](results.png?raw=true "Benchmark of Swift extensions vs methods")](http://minikin.me/extensions/)

## Run tests

To run tests set `USE_EXTENSIONS` to `true` or `false` in Rakefile.

```bash
rake benchmark
```

Cleanup tests results:

```bash
rake clean
```

## Results

To get more details you can [read blog](https://medium.com/@minikin/benchmark-of-swift-extensions-vs-methods-swift-4-1-may-2018-2df3229f76fe) and check [interactive charts](http://minikin.me/extensions/).

_[Results for Swift 4.1](https://github.com/minikin/extensions/tree/swift-4.1)_

If you have any questions, please feel free to contact me: [@minikin](https://twitter.com/minikin)

## Testing Machine

Mac Pro (Late 2013)

3 GHz 8-Core Intel Xeon E5

64 GB 1866 MHz DDR3

AMD FirePro D500 3 GB

macOS 10.15.1

## Plots

To generate `index.html` run:

```python
python3 main.py
```

or

```python
python main.py
```