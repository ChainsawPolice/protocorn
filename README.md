![Protocorn](protocorn_logo.png)

Protocorn allows you to test Unicorn HAT projects on your Windows, Mac, or Linux computer without needing a Raspberry Pi *or* a Unicorn HAT on hand.

This project was written when I was but a wee lass and Pimoroni had only created the original 8x8 Unicorn HAT. This was before the HAT Mini, the pHAT, and the HAT HD. Keep in mind that it's probably not going to work with a lot of the examples Pimoroni currently have in their GitHub repos and that some major tweaks will need to be done to Protocorn in order to get it back to being a drop-in replacement for the official `unicornhat` module. I might pick it back up when I have spare time. Who knows?

The rest of the below is verbatim from when I originally started this project back in 2015.

===============================

## Usage
Protocorn is intended as a drop-in replacement for the `unicornhat` module — just drop protocorn.py into your project folder, and wherever you have `import unicornhat` in your code, simply replace it with `import protocorn as unicornhat` and run your script.

## Dependencies
You will need to have PyGame installed for your OS. It's fairly easy on Windows and Linux, but OS X requires some major fiddling and tweaking.  
I wish I could tell you how I got it working on my Mac, but I'd be lying if I said I knew how I did it.

## Coverage
Currently, Protocorn covers the following functions from the official `unicornhat` module:

 * `set_pixel()`
 * `get_pixel()`
 * `show()`
 * `clear()`
 * `off()`

~~Other modules are not supported as of yet. However most, if not all, functions will be implemented in the future.~~

## To do
* Create PyPi package
* Optimise `show()`; get rid of any unecessary `for`s
* Implement other functions
