# 介绍
该工具箱可以用来生成多聚焦图像融合的数据集以及差分图，参考文章见：

https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/ipr2.12383

开源的代码中:

mainwindows.py为初始运行窗体，为各个功能提供窗体事件;

scrip/get_diffimage.py为求差分图的python脚本;

scrip/create_dataset.py为生成数据集的python脚本;

scrip/cut_imagetocompare.py为生成论文中展示图像的python脚本。


# 数据集生成流程
![图11](https://user-images.githubusercontent.com/40713736/164642530-d14b700d-be3c-407a-9572-e3951cf377f8.jpg)




如果使用该代码，请引用：

@article{wang2022two,
  title={Two-stage progressive residual learning network for multi-focus image fusion},
  author={Wang, Haoran and Hua, Zhen and Li, Jinjiang},
  journal={IET Image Processing},
  volume={16},
  number={3},
  pages={772--786},
  year={2022},
  publisher={Wiley Online Library}
}
