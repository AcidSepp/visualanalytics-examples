# snippet: main
if __name__ == '__main__':
    class OnStreamSum:
        def __init__(self):
            self.current_sum = 0.0

        def new_value(self, new_value: float):
            self.current_sum += new_value

    on_stream_sum = OnStreamSum()
    on_stream_sum.new_value(2.0)
    on_stream_sum.new_value(3.0)
    on_stream_sum.new_value(4.0)
    print(on_stream_sum.current_sum)
# snippet: /main
