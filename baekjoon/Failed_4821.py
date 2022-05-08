while True:
  total = int(input())
  if total == 0: break
  pages = [0] * total
  print_pages = input().split(',')
  for page_range in print_pages:
    page_range = list(map(int, page_range.split('-')))
    if len(page_range) < 2 and page_range[0] >= 0:
      index = int(page_range[0]) - 1
      if index >= 0: pages[index] = 1
    elif page_range[0] <= page_range[1]:
      for index in range(page_range[0], page_range[1] + 1):
        index -= 1
        if index < total and index >= 0: pages[index] = 1
        else: break
  
  print(pages.count(1))