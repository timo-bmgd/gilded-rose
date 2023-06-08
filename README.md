
# Gilded Rose Kata in Python
[For Informatics 3 @ Media Informatics HTW Berlin](https://home.htw-berlin.de/~kleinen/info3)

This version of the Guilded Rose Kata is an excerpt compiled from [Emily Bache's repo,](https://github.com/emilybache/GildedRose-Refactoring-Kata)
prepared for usage within [Info3](https://home.htw-berlin.de/~kleinen/info3) in the [International Media Informatics](https://imi-bachelor.htw-berlin.de/) Bachelor at [HTW Berlin](https://www.htw-berlin.de/).

If you look for the Gilded Rose Kata in general, go to the [version published by Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata) or [Kata-Log](https://kata-log.rocks/gilded-rose-kata) for a more general version.

# Introduction: Code Katas

The Term 'Kata' is a Metaphor taken from Martial Arts for a Pattern of Movements to Practice and Perfect those same Movements ([Wikipedia:Kata](https://en.wikipedia.org/wiki/Kata)). According to ([Wikipedia:Kata](https://en.wikipedia.org/wiki/Kata)), it was introduced as a practice to Software Craftsmanship by [Dave Thomas in his blog](http://codekata.com/), to practice Practices of Software Craftsmanship like TDD, Refactoring or the SOLID principles. There are several Code Kata Collections; see [Kata-Log](https://kata-log.rocks/gilded-rose-kata) for an example that can be browsed by topic and constraint.

# Instructions for the Kata

You will use this Kata to Practice Work on Legacy Code by 
1. Implementing Characterization Tests

and then  and then implement the new feature using 

2. Refactor to make the hard change easy and
3. Implement the Easy Change

## Step by Step

1. Implement Characterization Tests

    a. Read the [Requirements](GuildedRoseRequirements.txt)
    
    b. Have a look at the current source code
    
    c. Create Closed Box Tests based on the [Requirements](GuildedRoseRequirements.txt) (the specification)
   - if you find behaviour not compliant with the specification, 
     mark the tests with xfail as in the example.

    d. Ensure that you've written 'enough' tests by checking the test coverage

2. Refactor to make the hard change easy
    
    Now that you have a full test suite, you can confidently refactor the source code. Take a moment to consider which new design would make the change easy. Remember that there is a restriction though: You may not alter the Item class. 
    Which GoF-Patterns would be useful?


3. Implement the Easy Change

    This should be easy now! 

    Did your new design allow for adding the new requirement by just adding new code, without changing existing code?
    (Open-Closed Principle) 
    

## Requirements

Read through the [Requirements](GuildedRoseRequirements.txt)





