class Example:
    a = 5  # public
    _b = 6  # protected
    __c = 7  # private

ex = Example()
print(ex.a)
print(ex._b)
print(ex._Example__c)
