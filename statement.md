# MathCrypt – A Multi-Algorithm Password Encryption System

**## 1. Problem Statement**

Basic mathematical operations such as factors, prime checking, digit manipulation and number-base conversion are usually taught separately, so beginners rarely see how they can work together in one program. Password-related programs, on the other hand, are often either too simple to be interesting or too complex for a beginner to understand.

MathCrypt addresses this by taking a 4-digit numeric password, analysing it with several mathematical operations, and combining the results into a new encrypted password string. It also provides a decryptor that rebuilds the original number from that string and verifies it, so the whole process can be followed and tested step by step.

**## 2. Scope of the Project**

### In scope

- A Python command-line program that accepts a 4-digit whole number (1000 to 9999, or -9999 to -1000) as the password.
- Analysis of the number: factors, prime check, prime factors, sum of digits, reverse, binary form, factorial of each digit, and positive/negative check.
- Generation of an encrypted password in the format b\<binary>r\<reverse>f\<#factors>s\<digit sum>pf\<#prime factors>.
- An optional decryptor, started only when the user asks for it, that recovers the number from the binary part and checks it against the other stored values.
- Input validation, with repeated prompts until a valid entry is given.

### Out of scope

- Real-world password security. MathCrypt is an educational demonstration and does not replace established hashing or encryption methods.
- Recovering the original sign, because the encrypted password stores only the absolute value of the number.
- Text passwords, file or database storage, user accounts, and a graphical interface.

**## 3. Target Users**

- Beginner Python learners who want a practical example that uses loops, conditions, lists, strings and arithmetic together.
- Students of programming, mathematics and cybersecurity who are learning how data can be transformed step by step.
- Teachers and evaluators who need a clear, well-commented program that demonstrates algorithmic thinking.

**## 4. High-Level Features**

- Validated command-line input for a 4-digit positive or negative number.
- Factor listing and prime check.
- Prime factorisation.
- Digit sum and digit reversal.
- Binary conversion.
- Factorial of each digit, with their total.
- Positive/negative sign check.
- A summary of all results in one place.
- Encrypted password generation from the combined results.
- Optional password decryptor with a consistency check of every stored value.
- No external libraries required (Python 3 only).
