from src.prime import is_prime

def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(1009) is True
    assert is_prime(1011) is False
    assert is_prime(1013) is True
    assert is_prime(1015) is False

def test_is_prime_benchmark(benchmark):
    def benchmark_is_prime():
        is_prime(10000019)

    benchmark(benchmark_is_prime)
