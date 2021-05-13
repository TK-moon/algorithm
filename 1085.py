x, y, w, h = map(int, input().split())


left = 0 - x;
right = (w) - x;
bottom = 0 - y;
top = (h) - y;

left, right, bottom, top = map(abs, [left, right, bottom, top])

print(min(left, right, bottom, top));