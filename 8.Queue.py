from collections import deque

bank=deque(["Rimon","Yasir","Yousuf"])
print(bank)

bank.popleft()
print("Now member is",bank)

bank.popleft()
print("Now member is",bank)

bank.popleft()
print("Now member is",bank)

if not bank:
    print("No person")