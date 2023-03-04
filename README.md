# 百度网盘AI大赛-表格检测进阶：表格的结构化赛第10名方案
百度网盘AI大赛-表格检测进阶：表格的结构化赛第10名方案
> 是前十中速度最快的
![排名信息](./img/%E6%8E%92%E5%90%8D%E4%BF%A1%E6%81%AF.png)

# 算法流程
详细看main.ipynb

# 提交时使用的checkpoint
链接: https://pan.baidu.com/s/114UVouzjzBBLtx0SycYb8g?pwd=grit 提取码: grit 

# 特点: 自己生成数据, 二次训练调优

我们结合了 https://github.com/Belval/TextRecognitionDataGenerator 和 https://github.com/WenmuZhou/TableGeneration 这两个项目, 并开源到了 https://github.com/moyueheng/TableGeneration 进行数据生成, 获得了模糊, 倾斜的数据

# 还可优化点:
1. 目前只生成了模糊, 倾斜的数据, 还可以生成有遮挡物的数据
2. 换成更大的模型