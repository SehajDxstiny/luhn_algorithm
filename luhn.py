def main(n): 
    y = [(int(i) * (1 + idx % 2)) for idx, i in enumerate(reversed(list(n)))]
    return (sum(i - 9 if i > 9 else i for i in y)) % 10 == 0

'''-------------------testing---------------------'''

def test_luhn_algorithm():
    test_cases = [
        ("79927398713", True),
        ("79927398710", False),
        ("7", False),
        ("18", True), 
        ("19", False),
        ("0", True),
        ("1234567812345670", True),
        ("1234567812345678", False),
        ("4147204642145148", False),
        ("8273123273520569", False)
    ]

    all_pass = True
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = main(test_input)
        if result == expected:
            print(f"Test Case {i}: Pass - Input: {test_input}, Expected: {expected}, Got: {result}")
        else:
            print(f"Test Case {i}: Fail - Input: {test_input}, Expected: {expected}, Got: {result}")
            all_pass = False

    if all_pass:
        print("All tests passed")
    else:
        print("Some tests failed")

test_luhn_algorithm()




