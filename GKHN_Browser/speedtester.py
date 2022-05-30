import speedtest


def get_speed():
    s = speedtest.Speedtest()
    s.download()
    result: int = s.results.download
    result /= 8  # bit --> byte
    result /= 1024  # byte --> kb
    result /= 1024  # kb --> mb
    return result
