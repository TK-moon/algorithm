def calc(sh, sm, ss, fh, fm, fs):
  starttime = (sh * 60 * 60) + (sm * 60) + ss
  finishtime = (fh * 60 * 60) + (fm * 60) + fs
  time = finishtime - starttime
  h = time // 60 // 60
  m = (time % (60 * 60)) // 60
  s = (time % (60 * 60)) % 60
  print(h, m, s)

  

a = list(map(int, input().split()))
calc(*a)
b = list(map(int, input().split()))
calc(*b)
c = list(map(int, input().split()))
calc(*c)