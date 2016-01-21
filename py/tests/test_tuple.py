from erlpack import pack


def test_small_tuple():
    assert pack((1, 2, 3)) == '\x83h\x03a\x01a\x02a\x03'


def test_large_tuple():
    t = tuple(range(257))
    assert pack(t) == '\x83i\x00\x00\x01\x01a\x00a\x01a\x02a\x03a\x04a\x05a\x06a\x07a\x08a\ta\na\x0ba\x0ca\ra\x0ea' \
                      '\x0fa\x10a\x11a\x12a\x13a\x14a\x15a\x16a\x17a\x18a\x19a\x1aa\x1ba\x1ca\x1da\x1ea\x1fa a!a"a' \
                      '#a$a%a&a\'a(a)a*a+a,a-a.a/a0a1a2a3a4a5a6a7a8a9a:a;a<a=a>a?a@aAaBaCaDaEaFaGaHaIaJaKaLaMaNaOa' \
                      'PaQaRaSaTaUaVaWaXaYaZa[a\\a]a^a_a`aaabacadaeafagahaiajakalamanaoapaqarasatauavawaxayaza{a|a' \
                      '}a~a\x7fa\x80a\x81a\x82a\x83a\x84a\x85a\x86a\x87a\x88a\x89a\x8aa\x8ba\x8ca\x8da\x8ea\x8fa' \
                      '\x90a\x91a\x92a\x93a\x94a\x95a\x96a\x97a\x98a\x99a\x9aa\x9ba\x9ca\x9da\x9ea\x9fa\xa0a\xa1' \
                      'a\xa2a\xa3a\xa4a\xa5a\xa6a\xa7a\xa8a\xa9a\xaaa\xaba\xaca\xada\xaea\xafa\xb0a\xb1a\xb2a\xb3' \
                      'a\xb4a\xb5a\xb6a\xb7a\xb8a\xb9a\xbaa\xbba\xbca\xbda\xbea\xbfa\xc0a\xc1a\xc2a\xc3a\xc4a\xc5' \
                      'a\xc6a\xc7a\xc8a\xc9a\xcaa\xcba\xcca\xcda\xcea\xcfa\xd0a\xd1a\xd2a\xd3a\xd4a\xd5a\xd6a\xd7' \
                      'a\xd8a\xd9a\xdaa\xdba\xdca\xdda\xdea\xdfa\xe0a\xe1a\xe2a\xe3a\xe4a\xe5a\xe6a\xe7a\xe8a\xe9' \
                      'a\xeaa\xeba\xeca\xeda\xeea\xefa\xf0a\xf1a\xf2a\xf3a\xf4a\xf5a\xf6a\xf7a\xf8a\xf9a\xfaa\xfb' \
                      'a\xfca\xfda\xfea\xffb\x00\x00\x01\x00'