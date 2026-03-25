# snippet: main
if __name__ == '__main__':
    class OnStreamAverage:
        def __init__(self):
            self._current_sum = 0.0
            self._counts = 0

        @property
        def current_average(self) -> float:
            return self._current_sum / self._counts

        def new_value(self, new_value: float):
            self._counts += 1
            self._current_sum += new_value

    on_stream_avg = OnStreamAverage()
    on_stream_avg.new_value(2.0)
    on_stream_avg.new_value(3.0)
    on_stream_avg.new_value(4.0)
    print(on_stream_avg.current_average)
# snippet: /main
