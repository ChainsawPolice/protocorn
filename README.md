# Protocorn

Protocorn allows you to test Unicorn HAT projects on your Windows, Mac, or Linux computer without needing a Raspberry Pi *or* a Unicorn HAT on hand. Perfect for sneaky lunch-break dev sessions or the poor few without a diffuser over their HAT.

## Usage
Protocorn is intended as a drop-in replacement for the `unicornhat` module — just drop protocorn.py into your project folder, and wherever you have `import unicornhat` in your code, simply replace it with `import protocorn as unicornhat` and run your script.

## Dependencies
You will need to have PyGame installed for your OS. It's farirly easy on Windows and Linux, but OS X requires some major fiddling and tweaking. I wish I could tell you how I got it working on my Mac, but I'd be lying if I said I knew how I did it.

## Coverage
Currently Protocorn covers the `set_pixel()` and `show()` functions from the official `unicornhat` module. Other modules are not supported as of yet. However most, if not all, functions will be implemented.

## To do
* Create PyPi package
* Optimise `show()`; get rid of any unecessary `for`s
* Implement other functions