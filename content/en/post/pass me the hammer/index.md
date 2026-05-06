---
title: "Pass me the hammer: how people deal with errors in Python"
date: 2026-05-05
description: A collection of stories that illustrate how errors in programming represent communication between programmers far apart in time and space.
draft: false
---

Imagine three people building a house, A, B, and C. A finds and gives tools, C uses the tools, and B makes the logistics of passing things from A to C.

If everything goes perfect, then:

> B to A: Can you please pass me the hammer?
>
> A to B: *gives them the hammer*
>
> A to C: here you go
>
> C: Thanks! *works with the hammer*

```python
class Hammer:
    pass

class Screwdriver:
    pass

class Nail:
    pass

screwdriver = Screwdriver()
nail = Nail()

def A():
    drawers = {"screwdriver": screwdriver, "nail": nail, "hammer": Hammer()}
    thing = drawers["hammer"]
    return thing

def B():
    thing = A() # get something from A
    C(thing) # give it to C
    # C finishes their work, so does A
```

A(), B() and C(thing) are all functions. `Hammer`, `Screwdriver` and `Nail` are stand-ins for real objects with more interesting methods. 
But the world is, as you know, imperfect, so things can break at any point of the chain. 
Here you will find several cases one could possibly encounter in the wild and ask: What is best? More robust? Faster? Convenient?

A just goes through the motions, as they have done many times before, of getting the hammer. Reaches to the right place, grabs whatever it was there, and gives it back to B.
However, for one reason or another, the hammer is not there. There's no immediate solution for that. What to do?

## Muscle memory

> B to A: Can you please pass me the hammer?
>
> A to B: *gives them poop*
>
> B: Great, now I have to deal with this

```python
def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    thing = drawers["hammer"]
    return thing
```

You can immediately tell by reading that this dictionary has no "hammer" key, so this will fail throwing a KeyError exception. This may not be that easy to tell if there were thousands of items in the dictionary.

When the exception is not handled (in a dedicated try block), then A is implicitly re-raising that exception to B. And now B must deal with this. If B does not deal with it, then so will the caller of B, and so on.
When poop is brought up, and no one deals with it, then the whole operation shuts down (the program crashes).

## Empty hands

A is now aware of the fact that they don't have a hammer. They tried, however, nothing came up. They come back to B with a big nothing sandwich…

```python
def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError:
        return None
```

> B to A: Pass me the hammer
>
> A to B: *gives them a ✨nothing✨*
>
> B to C: try this
>
> C: I can't hammer with nothing!

Presumably here, the hammer was really needed, and ✨nothing✨ has none of the properties a hammer is known for. C now can understandably complain, because whatever they got did not meet their expectations. The whole operation is shut down again.

What's worse here is that in python None is always implicitly returned:

```python
def A():
    drawers = {"screwdriver": screwdriver, "nail": nail, "hammer": hammer}
    # (40 lines of code later I forgot to add a "return result"

A() # -> also returns None!
```

You'll get a raised exception coming from C ("I wanted a hammer and you gave me nothing. I can't hammer with nothing!")
But the real error was upstream of C, at the place where None got first into the pipeline. The stack trace is not helpful here.

## Send a note

> B to A: Pass me the hammer
>
> A to B: *gives them a hand written note*
>
> The note: "I don't have a hammer 🙂"

Truth is, anything can be returned that signals an error.

```python
def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError:
        return "I don't have a hammer :)"
```

Is this any better than before?

Well, C can't hammer with ✨nothing✨ and certainly will not be able to hammer with a handwritten note. At least now, maybe C will complain in a way that can lead you a step closer to finding out what went wrong:

C: "I wanted a hammer and you gave me a handwritten note saying 'I don't have a hammer'. I can't hammer with this!"

Another instance where returning a value instead of throwing is when you want to leverage idempotency. Better shown with example:

```python
L = get_list_of_tools()
for tool in L:
    print(f"we have a {tool}")
```

If get_list_of_tools fails to give any actual tool, it is still reasonable to return the empty list. The loop will simply not print anything, and not fail. The code is robust in the sense that, no matter the result from get_list_of_tools, it will run anyway.

The opposite is the risky:

```python
L = get_list_of_tools()
first_tool = L[0] # may fail with index error!
print(f"The first tool is {first_tool}")
```

## CYA operation

The "cover your ass" operation is how you deal with people you don't trust.

> B to A: Pass me the hammer
>
> A to B: *gives them something (or nothing, or perhaps a hammer)*
>
> B: *checks* this isn't a hammer!

```python
def B():
    thing = A() # get something from A
    if not isinstance(thing, Hammer):
        thing = get_hammer_from_store()
    C(thing)
```

Now B is prepared to deal with A's sloppy behaviour. But the problem is that this defense is incomplete, only covering for when A might give you a "not hammer", while failing when A throws an exception as we just saw in [Muscle memory](#muscle-memory).

Essentially there are two different pipelines, the normal pipeline and the error pipeline. The error pipeline bubbles errors whether you like it or not. And you treat both of them with different syntaxes: writing an if...else for the former and a try...except for the latter. 

## Helpful unhelpful

The thing with returning an error instead of throwing is that B might not do their due diligence to cover themselves. So instead…

> B to A: Can you please pass me the hammer?
>
> A to B: *writes note, staples note to some poop, gives them the poop*
>
> B: Great, now I have to deal with this, but thanks for the info

```python
class HammerNotFound(Exception):

def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError:
        raise HammerNotFound("Could not find hammer in any drawers.") from KeyError
```

`KeyError` does not mean anything in the context of making a house. Getting such an exception is unhelpful, because there's no practical way to deal with this without looking at the code from A.

A `HammerNotFound` error is much more informative. There are specific reasons explaining why the drawers dictionary does not contain the right tools. Maybe you have to focus on the places where the drawers get filled up.

The information is not limited to just text. HammerNotFound is a class that, apart from inheriting all the properties of Exception, can contain arbitrary properties and methods. Maybe it can store the full context which produced the exception, like giving a copy of all the items they did have.

In this version, A is unhelpful (it failed) and helpful (gave you a reason and context). And failed in a way that B must deal with.

## Indiscrete

> B to A: Can you please pass me the hammer?
>
> A to B: *running in the streets* HEY EVERYONE! I DON'T HAVE A HAMMER!!!"
>
> People in the streets: shut up!!

```python
def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError as e:
        print(f"Could not find Hammer: {e} ")
        return None # why not while you are at it
```

Printing is not an acceptable way of logging errors. The user might be using stdout streams for their own purposes. Don't complain to everyone about your problems, complain to the right person.

## Union member

> B to A: Pass me the hammer
>
> A: *proceeds to file a complaint to the labour board*

```python
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR, stream=sys.stdout)

def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError as e:
        logger.error(f"Could not find Hammer: {e} ")
        return None
```

This is a fairly standardized way for users to set up debugging logs. Python's standard library logging can be used to set up a log (say, a file, or even stdout) where all the libraries and files used all along the whole project may post their messages with different levels of severity and or detail. It's very useful specially because it's such a strong convention in the python ecosystem.

The result of calling A() from the previous code is:

```
ERROR:__main__:Could not find Hammer: 'hammer'
```

If you setup a plot, and something in matplotlib fails, you will for example see:

```bash
WARNING:matplotlib.font_manager:findfont: Font family 'Arial' not found.
```

Additionally, the logging library can be configured to output a log to a file, which is fairly useful.

## Arson

> B to A: Pass me the hammer
>
> A: *sets the house on fire*

```python
import sys
def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError as e:
        sys.exit(1)
```

Here the program just crashes, no stack trace. You have an indication that there was an error, through the error code (sys.exit(0) signals no error, any non-zero code means error) but no reference to a line of the source code, no stack trace, nothing.

There's an even more nuclear version os._exit(0) stops everything in its tracks and does not clean up. For example a serial connection might remain open, hindering your ability to re-open it later.

## Epilogue

Software is libraries using libraries.. n times ..using libraries finally ending in a user-facing place (in the last step, the users are usually not programmers). Our actors played the part of people sitting in different parts of the stack. C uses results from -> B uses results from -> A.

When importing a library, implicitly or explicitly we believe that it will work, it will be fast enough, it will have no vulnerabilities, etc. The library in turn expects us to use it properly, provide the right type of inputs, provide inputs that make sense and not edge cases, that the classes provided will be used as intended. Unexpected errors shatter this view. 

Library writers can work on the quality of documentation. Indeed, in a modern coding environment, just by hovering on top of a imported function users can read the documentation, "a message from the past". To go with, a carefully designed error interface puts the user and the library-writers in the same room when an error bubbles up. This was A's role. But A is not there when the error happens. It's B the one who had a mission, who wanted to combine A and D, E, F's libraries to make something genuingly new. It's up to library users to cover for errors: their own and of others.

The point of this post is not to recommend any particular strategy, many projects don't need fine level of control, but as it develops, it's good to think critically when is time to _grow out_ of one strategy and go for the next.


> Word count for the word "error": 22 times

--- 

Any corrections or comments? [Leave an issue](https://github.com/acanalis/acanalis.github.io/issues)!

[Link to the snippets in full.](https://github.com/acanalis/acanalis.github.io/tree/master/content/en/post/pass%20me%20the%20hammer/code)
