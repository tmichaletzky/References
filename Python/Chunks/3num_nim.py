def nim_game(a, b, c, N = 30):
    s = ''
    s = s.join('n' for _ in range( max(a, b, c)))
    for _ in range(N):
            if s[-a] == s[-b] == s[-c] == 'n':
                    s = s + 'p'
            else:
                    s = s + 'n'

    print(s[ max(a, b, c):])
