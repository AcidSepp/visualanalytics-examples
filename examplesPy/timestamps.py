import pendulum

# snippet: main
if __name__ == '__main__':
    birth_time = pendulum.datetime(1995, 11, 6, 9, 11, 0, tz="Europe/Paris")
    print(birth_time.in_tz("UTC").to_iso8601_string())
# snippet: /main
