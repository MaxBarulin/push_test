def log(filename=None):
    """Декоратор для логирования вызовов функции и её результатов."""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if filename is None:
                try:
                    func(*args, **kwargs)
                    print(f"{func.__name__} ok")
                except Exception as e:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")

            else:
                if type(filename) is str:
                    try:
                        func(*args, **kwargs)
                        # print("ok")
                        with open(f"../logs/{filename}", "a") as file:
                            file.write(f"{func.__name__} ok")
                            file.write("\n")

                    except Exception as e:
                        with open(f"../logs/{filename}", "a") as file:
                            file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                            file.write("\n")
                else:
                    filename_str = f"{str(filename)}.txt"
                    try:
                        func(*args, **kwargs)
                        # print("ok")
                        with open(f"../logs/{filename_str}", "a") as file:
                            file.write(f"{func.__name__} ok")
                            file.write("\n")

                    except Exception as e:
                        with open(f"../logs/{filename_str}", "a") as file:
                            file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                            file.write("\n")

        return wrapper

    return my_decorator


@log()
def my_function(x, y):
    return x / y


@log("mylog.txt")
def my_function_file(x, y):
    return x / y


if __name__ == "__main__":
    my_function_file(10, 20)
