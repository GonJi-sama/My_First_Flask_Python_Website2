class mainfunc:
    def myfunc(a, b):
        result = ""
        for i in range(b):
            for j in range(b):
                if i < j:
                    result += "  "
                else:
                    result += a + " "
            result += "\n"
        return result
