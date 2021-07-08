from threading import Timer


def hello():
    print("hello, world")


t = Timer(2.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
