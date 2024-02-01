import time

class File:

    counter = 1
    
    @classmethod
    def show_counter(cls):
        return cls.counter
    
    def __init__(self, file_path : str, method : str) -> None:
        self.__method = method
        self.open_file = open(file_path, self.__method)
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self.open_file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        if File.counter == 1:
            my_method = "w"
        else:
            my_method = "a"
        with open("lesson21/logs.txt", my_method) as add_log:
            add_log.write(
                "Call : " + str(File.show_counter()) + "\nMethod : " + self.__method + "\n" + "Work time : " + str((self.end - self.start) * 1000) + " ms\n"
            )
        File.counter += 1
        self.open_file.close()