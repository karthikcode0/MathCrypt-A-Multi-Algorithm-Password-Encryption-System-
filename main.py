# =====================================================================
# ========================password encryptor================================
# first analyzes the password number and then encrypts it into a new password
# it uses factors, prime check, prime factors, digit sum, reverse,
# binary, factorial of digits, sign check, 
# and encrypts the password into a new password using all of the above
# Runs top to bottom; every step uses the number entered in step 1.
# Steps are numbered so each output can be matched to the code producing it.
# The decryptor (step 12) only runs if the user asks for it.
# =====================================================================

# --- 1. Input: keep asking until the user enters a valid 4-digit password ---
# Both positive (1000 to 9999) and negative (-9999 to -1000) are accepted,
# so that the positive/negative check in step 9 is meaningful.
while True:
    try:
        # input() always returns text, so int() converts it to a number
        num = int(input("Enter a 4 digit password: "))
    except ValueError:                       # input was not a number
        print("Please enter a valid password.")
        continue                               # go back to the top of the loop
    if 1000 <= abs(num) <= 9999:            # abs() ignores the minus sign
        break                               # valid input, leave the loop
    print("The password must be exactly 4 digits (1000 - 9999 or negative).")

# All calculations below use the absolute value, because factors, digits
# and binary conversion are defined for positive whole numbers.
n = abs(num)

# --- 2. Factors: numbers that divide n with remainder 0 ---
# Results are stored in a list so they can be printed now and counted later.
factors = []
for i in range(1, n + 1):                   # every integer from 1 to n
    if n % i == 0:                          # remainder 0 means exact division
        factors.append(i)
print("\nThe factors of the number are:", *factors)

# --- 3. Prime check: a prime has exactly two factors (1 and itself) ---
# The factor list from step 2 is reused, so no extra looping is needed.
if len(factors) == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

# --- 4. Prime factors: divide out the smallest divisor repeatedly ---
prime_factors = []
temp = n                    # work on a copy so n stays unchanged
i = 2                       # 2 is the smallest prime
while i * i <= temp:        # a leftover factor is never above sqrt(temp)
    while temp % i == 0:    # i divides temp, so i is a prime factor
        prime_factors.append(i)
        temp //= i          # divide it out and check the same i again
    i += 1                  # move on to the next integer
if temp > 1:                # remainder with no smaller factor is prime
    prime_factors.append(temp)
print("\nThe prime factors of the number are:", *prime_factors)

# --- 5. Sum of digits: % 10 takes last digit, // 10 removes it ---
# Example: 1234 % 10 = 4 and 1234 // 10 = 123, so the loop peels off
# one digit per pass until nothing is left.
temp = n
digit_sum = 0               # running total
digits = []                 # saved for the factorial step later
while temp > 0:
    digit = temp % 10       # last digit of temp
    digits.append(digit)
    digit_sum += digit
    temp //= 10             # drop the last digit
digits.reverse()            # digits were collected last-to-first, so flip
print("\nThe sum of the digits of the number is:", digit_sum)

# --- 6. Reverse: shift result left (x10) and add the last digit ---
# Multiplying by 10 makes room on the right for the next digit.
temp = n
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print("\nThe reverse of the number is:", reverse)

# --- 7. Binary: divide by 2, remainders read last-to-first ---
# Binary is base 2, so every digit is either 0 or 1.
temp = n
binary = ""                 # string keeps the 0s and 1s as text
while temp > 0:
    binary = str(temp % 2) + binary         # add in front to fix the order
    temp //= 2
print("\nThe binary equivalent of the number is:", binary)

# --- 8. Factorial of each digit ---
# factorial(d) = 1 x 2 x ... x d, and factorial(0) is defined as 1.
# The multiplication loop below naturally gives 1 when d is 0.
digit_factorials = []
print("\nThe factorial of each digit is:")
for d in digits:
    fact = 1                                # start of the product
    for k in range(2, d + 1):               # multiply 2 up to d
        fact *= k
    digit_factorials.append(fact)
    print(f"  {d}! = {fact}")
factorial_sum = sum(digit_factorials)       # total of all digit factorials
print("The sum of the factorials of the digits is:", factorial_sum)

# --- 9. Positive or negative check ---
# Numbers above 0 are positive; the input range guarantees it is never 0.
# Uses the original input `num`, before abs() removed the sign.
if num > 0:
    sign = "positive"
else:
    sign = "negative"
print(f"\nThe number {num} is {sign}.")

# --- 10. Summary of all results ---
# Storing (label, value) pairs lets one loop print every result.
summary = [
    ("sign", sign),
    ("factors", factors),
    ("prime_factors", prime_factors),
    ("sum_of_digits", digit_sum),
    ("reverse", reverse),
    ("binary", binary),
    ("digit_factorials", digit_factorials),
    ("factorial_sum", factorial_sum),
]
print("\nSummary:")
for label, value in summary:
    print(f"{label}: {value}")          # e.g. "sign: positive"

# --- 11. Password: b<binary> r<reverse> f<#factors> s<sum> pf<#prime factors> ---
# Only the counts of factors are used, not the full lists.
# f-strings insert each value into the text, joining all parts in order.
encrypted_password = (
    f"b{binary}"
    f"r{reverse}"
    f"f{len(factors)}"
    f"s{digit_sum}"
    f"pf{len(prime_factors)}"
)
print("\nThe encrypted password is:", encrypted_password)


# =====================================================================
# --- 12. Ask whether the user wants the password decoded ---
# The decryptor below only starts if the answer is yes.
# Keep asking until the answer is a clear yes or no.
# =====================================================================
while True:
    choice = input("\nDo you want to decode the encrypted password? (yes/no): ").strip().lower()
    if choice in ("yes", "y", "no", "n"):
        break                                # valid answer, leave the loop
    print("Please type yes or no.")

if choice in ("no", "n"):
    print("Decryption skipped. Your encrypted password is:", encrypted_password)
else:
    # =================================================================
    # --- 13. Password decryptor ---
    # Format being decoded: b<binary>r<reverse>f<#factors>s<digit sum>pf<#prime factors>
    # Plan: split the password into its parts, rebuild the number from the
    # binary part, then re-run the analysis on it and compare with the
    # values stored in the password.
    # =================================================================
    import re                                # regular expressions split the text

    print("\n--- Password Decryptor ---")

    # Decrypt the password just made in step 11. To decode a different one,
    # replace this line with:  password_to_decode = input("Enter password: ")
    password_to_decode = encrypted_password

    # --- 13a. Split the password into its five parts ---
    # b([01]+)  -> binary: only 0s and 1s
    # r(\d+)    -> reverse of the number
    # f(\d+)    -> count of factors
    # s(\d+)    -> sum of digits
    # pf(\d+)   -> count of prime factors
    match = re.fullmatch(r"b([01]+)r(\d+)f(\d+)s(\d+)pf(\d+)", password_to_decode)

    if match is None:
        print("Invalid password format - cannot decrypt.")
    else:
        d_binary = match.group(1)
        d_reverse = int(match.group(2))
        d_factor_count = int(match.group(3))
        d_digit_sum = int(match.group(4))
        d_pf_count = int(match.group(5))

        # --- 13b. Binary -> number: each digit doubles the total and adds itself ---
        # Example: "101" -> 0*2+1=1 -> 1*2+0=2 -> 2*2+1=5
        d_num = 0
        for bit in d_binary:
            d_num = d_num * 2 + int(bit)
        print("The decrypted number is:", d_num)

        # --- 13c. Re-analyse the recovered number ---
        # Factor count
        check_factors = 0
        for i in range(1, d_num + 1):
            if d_num % i == 0:
                check_factors += 1

        # Prime factor count (same method as step 4)
        check_pf = 0
        temp = d_num
        i = 2
        while i * i <= temp:
            while temp % i == 0:
                check_pf += 1
                temp //= i
            i += 1
        if temp > 1:
            check_pf += 1

        # Digit sum and reverse (same method as steps 5 and 6)
        check_sum = 0
        check_rev = 0
        temp = d_num
        while temp > 0:
            check_sum += temp % 10
            check_rev = check_rev * 10 + temp % 10
            temp //= 10

        # --- 13d. Compare every recomputed value with the one in the password ---
        checks = [
            ("reverse", check_rev, d_reverse),
            ("factor count", check_factors, d_factor_count),
            ("digit sum", check_sum, d_digit_sum),
            ("prime factor count", check_pf, d_pf_count),
        ]
        all_ok = True
        for label, computed, stored in checks:
            ok = computed == stored
            all_ok = all_ok and ok
            print(f"  {label}: computed {computed}, stored {stored} -> "
                  f"{'OK' if ok else 'MISMATCH'}")

        if all_ok:
            print("Password is valid and decrypted successfully.")
        else:
            print("Warning: password does not match its number (it may be corrupted).")

        # The password stores no sign (step 11 uses n = abs(num)), so the
        # original sign cannot be recovered from the password alone.
        print("Note: the sign (positive/negative) is not stored in the password.")

# --- End of program ---