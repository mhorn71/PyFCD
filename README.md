# pyfcdctrl

Python FCD Interface.

WARNING IN PROCESS OF UPDATING TO COVER FCD Pro+

Implements the full Funcube Dongle Pro api excluding 'Firmware Update and Verify.'

To use:

You need to install cython and cython-hidapi and get the latter from https://github.com/bazuchan

NOTE: cython-hidapi from the raspbian repos causes a segmentation fault on exit whereas the version above doesn't.

NOTE NOTE ::  The RaspberryPi Raspbain USB sometimes locks up, if you call methods concurrently without adding a time delay.

This has been tested on a RaspberryPi B and Pi2 with Raspbian, as well as Debian on the Beaglebone Black Rev C.

Copy pyfcdctrl.py to your programs root folder and import it in your program.

##  Example Program

```python
import pyfcdctrl as fcd

mydevice = fcd.PyFcdCtrl('pro')   # proplus not yet implemented.

try:
    mydevice.defaults() ## sets defaults
except Exception as e:
    print('failed to set defaults!!')

ppm_offset = 0
freq = 140000000

try:
    if mydevice.set_hz(freq, ppm_offset): ## Set the frequency.
        print('set frequency = %s' % str(freq))
except Exception as e:
    print('failed to set frequency')

try:
    freq = mydevice.get_hz()  ## Get the frequency as reported by the FCD Pro.
except Exception as e:
    print('failed to get frequency')
else:
    print('Frequency = %s' % str(freq)
```