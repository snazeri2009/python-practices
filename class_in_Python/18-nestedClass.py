# this is a nested class example
class OuterClass:  # this is outer Class
    class _InternalClass:  # this is internal class
        def __init__(self, value):
            self.value = value

        def internal_method(self):
            print(f"Internal class method called with value: {self.value}")

    def __init__(self, value):  # this init is for outer classes
        self.internal = self._InternalClass(value)

    # this method is for outer classes and call internal method
    def call_internal_method(self):
        self.internal.internal_method()


# called by outer class and set value to "Hello" ,  __init__(self, value):
outer = OuterClass("Hello")
outer.call_internal_method()  # Output: Internal class method called with value: Hello
