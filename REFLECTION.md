# Reflection: ITCS386 TDD Lab

## 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?
8 tests and 38 lines of production code, so about 1 test per 5 lines.

## 2. When was your bar red for the longest time, and what made it last so long?
A7 mixed addition. It stayed red over several changes because `Sum.reduce` ignored units and gave 201 g instead of 228 g.

## 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
- Fake It: A1 `times` returned 600. Right, it proved the test worked.
- Triangulate: A2 the x2 test forced the real formula. Right, it worked.
- Obvious: A3 `return Quantity(...)`. Right, it was a one-line fix.

## 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
`(200 g + 1 oz) x 2` is next. `__hash__` is speculation, so delete it.

## 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
No. It only appeared because `Converter` needed to treat `Quantity` and `Sum` the same way.

## 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
Part 0 tests only checked existing code and found boundary bugs. In Part A the tests shaped the design. `Sum` and `Converter`.
