def hi():
    return "hi, caoqi"

def doSomeThingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


if __name__ == "__main__":
    doSomeThingBeforeHi(hi)