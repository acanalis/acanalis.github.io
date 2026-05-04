---
title: "Pass me the hammer"
date: 2026-03-19T20:00:00
draft: true  
---

## Recap 

In the [previous post]({{}}) I listed the main ways Python deals with errors and how programmers deal with well, python. 


The fact that in python there are two pipelines complicates everything. Let’s take a look at how Go treats error, see if the grass is greener on the other side.

Let's begin with the happy path where everything goes as it should:

```go
main go

func A(){
    drawers = {"screwdriver": 1, "nail": 2, "hammer": 3}
    thing = drawers["hammer"]
    return thing
}

func B(){
    thing = A() # get something from B
    C(thing) # give it to C
    # C finishes their work, so does A
}

func C(a:)

func main() {
    B()
    // Pass
}

```

## Panic! at the disco

To be completely fair, Go also has an error pipeline. It looks like this: 

```go
main go


```

STo add insult to injury, there is no type checking step where A is guaranteed to even be qualified to give hammers in the first place.

# parked this one

None is not a reasonable way to represent nothing because anything can be nothing. What are you going to check? That you stand on the floor? That you can touch your table? Did you meet Morpheous or something?

#### Ideal scenario

A function does its job properly if:
executes unreliable functions in a try block
Tries its best not to fail by recovering from expected errors
Raises a wrapped exception upwards if something is truly unrecoverable. The wrapping provides context on how and where to solve the issue
Raise a CLOSED LIST of exceptions. 
Returning successfully means that whoever is calling the function will not be surprised by what they got.

Problem is, expectations need to be synchronised across library borders.

Honorable mention to returning nans. Any mathematical operation with a NaN results in a NaN, like:
NaN + 1 = NaN
NaN*1 = NaN

Which means that as soon as nan gets in the chain, more and more nans will pop up in the results. The job will just continue running and not complain. Whether this is acceptable depends on context.
