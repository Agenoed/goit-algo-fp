import turtle

def draw_tree(branch_len, angle, level):
  if level > 0:
    turtle.forward(branch_len)
    turtle.left(angle)
    draw_tree(branch_len * 0.7, angle, level - 1)
    turtle.right(2 * angle)
    draw_tree(branch_len * 0.7, angle, level - 1)
    turtle.left(angle)
    turtle.backward(branch_len)

def main():

  level = int(input("Введіть рівень рекурсії: "))
  turtle.speed(0)  
  turtle.left(90)  
  turtle.penup()
  turtle.backward(100) 
  turtle.pendown()
  draw_tree(100, 45, level)  
  turtle.done()  

if __name__ == "__main__":
  main()