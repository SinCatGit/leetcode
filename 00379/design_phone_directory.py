

class PhoneDirectory:
    """
    [379. Design Phone Directory](https://leetcode.com/problems/design-phone-directory/)

    Design a Phone Directory which supports the following operations:
    
    1. `get`: Provide a number which is not assigned to anyone.
    2. `check`: Check if a number is available or not.
    3. `release`: Recycle or release a number.
    
    **Example:**
    
    ```
    // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
    PhoneDirectory directory = new PhoneDirectory(3);
    
    // It can return any available phone number. Here we assume it returns 0.
    directory.get();
    
    // Assume it returns 1.
    directory.get();
    
    // The number 2 is available, so return true.
    directory.check(2);
    
    // It returns 2, the only number that is left.
    directory.get();
    
    // The number 2 is no longer available, so return false.
    directory.check(2);
    
    // Release number 2 back to the pool.
    directory.release(2);
    
    // Number 2 is available again, return true.
    directory.check(2);
```
    """
    def __init__(self, maxNumbers):
        self.numbers = [i for i in range(maxNumbers)]
        self.used = [False for _ in range(maxNumbers)]
        self.idx = 0
        self.num_len = maxNumbers

    def get(self):
        if self.idx == self.num_len:
            return -1
        res = self.numbers[self.idx]
        self.idx += 1
        self.used[res] = True
        return res

    def check(self, number):
        return 0 <= number < self.num_len and not self.used[number]

    def release(self, number):
        if self.idx == 0: return
        if number < 0 or number >= self.num_len or not self.used[number]:
            return
        self.idx -= 1
        self.numbers[self.idx] = number
        self.used[number] = False
