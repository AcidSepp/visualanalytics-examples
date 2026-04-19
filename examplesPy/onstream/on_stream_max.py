# snippet: class
class OnStreamMax:
    def __init__(self):
        self.current_max = float('-inf')

    def new_value(self, new_value: float):
        if new_value > self.current_max:
            self.current_max = new_value
# snippet: /class

# snippet: main
if __name__ == '__main__':
    on_stream_max = OnStreamMax()
    on_stream_max.new_value(2.0)
    on_stream_max.new_value(3.0)
    on_stream_max.new_value(4.0)
    print(on_stream_max.current_max)
# snippet: /main
