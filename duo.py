import turtle
 
# 创建海龟对象
t = turtle.Turtle()
 
# 设置初始位置和朝向
t.penup()
t.goto(-100, -50)
t.pendown()
 
# 开始绘制图形
for _ in range(4):
    # 前进200像素并右转90度
    t.forward(200)
    t.right(90)
    
# 关闭海龟窗口
turtle.done()
