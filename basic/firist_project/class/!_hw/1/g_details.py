n, k, m = map(int, input().split(' '))

if n < k or k < m:
    print(0)
else:
    m_num = 0
    k_num = 0

    m_num_per_k = k // m
    m_left_per_k = k % m

    while n >= k:
        k_num = n // k
        m_num += (k // m) * k_num
        n = n - k_num * k + m_left_per_k * k_num
    print(m_num)