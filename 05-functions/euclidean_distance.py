def distance(dx, dy):
    return (dx*dx + dy*dy) ** 0.5

def is_point(point):
    parts = point.split()
    if len(parts) != 2:
        return False
    try:
        float(parts[0])
        float(parts[1])
        return True
    except ValueError:
        return False

def get_point(prompt="enter point"):
    while True:
        point = input(prompt)
        if is_point(point):
            return point
        print("Invalid input! Please enter two numbers separated by space.")

def main():
    point1 = get_point("Enter first point (x1 y1): ").split()
    point2 = get_point("Enter second point (x2 y2): ").split()

    x1, y1 = float(point1[0]), float(point1[1])
    x2, y2 = float(point2[0]), float(point2[1])

    dx = x2 - x1
    dy = y2 - y1
    dist = distance(dx, dy)
    print(f"Distance: {dist}")
    
if __name__ == "__main__":
    main()