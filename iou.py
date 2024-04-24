import torch
import numpy as np



def single_seg_iou(pred_mask, label, cls):
    '''计算一张图片中cls这个类别的iou'''
    mask = pred_mask == cls
    intersection = np.logical_and(mask, label)
    union = np.logical_or(mask, label)
    if union.sum() == 0:
        return 'nan'
    else:
        iou = intersection.sum() / union.sum()
        return iou


def single_bbox_iou(box1, box2):
    """
    computing IoU
    param box1: (x1min, y1min, x1max, y1max) --> (左上角x, 左上角y, 右下角x,右下角y)
    param box2: (x2min, y2min, x2max, y2max) --> (左上角x, 左上角y, 右下角x,右下角y)
    return : scale value of IoU
    """
    x1min, y1min, x1max, y1max = box1[0], box1[1], box1[2], box1[3]
    x2min, y2min, x2max, y2max = box2[0], box2[1], box2[2], box2[3]
    # 计算两个框的面积
    s1 = (y1max - y1min) * (x1max - x1min)
    s2 = (y2max - y2min) * (x2max - x2min)

    # 计算相交部分的坐标
    xmin = max(x1min, x2min)
    ymin = max(y1min, y2min)
    xmax = min(x1max, x2max)
    ymax = min(y1max, y2max)

    inter_h = max(ymax - ymin, 0)
    inter_w = max(xmax - xmin, 0)

    intersection = inter_h * inter_w
    union = s1 + s2 - intersection

    # 计算iou
    iou = intersection / union
    return iou
def iou(b1,b2):
    x1min, y1min, x1max, y1max = b1[0], b1[1], b1[2], b1[3]
    x2min, y2min, x2max, y2max = b2[0], b2[1], b2[2], b2[3]
    s1 = (x1max-x1min)*(y1max-y1min)
    s2 = (x2max-x2min)*(y2max-y2min)

    xmin = max(x1min,x2min)

    xmax = min(x1max,x2max)

    ymin = max(y1min,y2min)

    ymax = min(y1max,y2max)

    inth=max(xmax-xmin,0)
    intw=max(ymax-ymin,0)

    ious = intw*inth

    inters = s1 + s2 - ious
    iou = ious/inters
    return iou
if __name__ == '__main__':
    # 生成两个mask
    # a = torch.randn(5, 8)  # 均值为0方差为1的正态分布
    # a.gt_(0)  # 二值化：大于0的数替换为1 小于0的数替换为0
    # b = torch.randn(5, 8)
    # b.gt_(0)
    # c = a + b
    #
    # d = torch.randn(5, 8)  # 均值为0方差为1的正态分布
    # d.gt_(0)  # 二值化：大于0的数替换为1 小于0的数替换为0
    # e = torch.randn(5, 8)
    # e.gt_(0)
    # f = d + e
    #
    # seg_iou = single_seg_iou(c, f, 0)
    # print(seg_iou)
    det_iou = iou([1, 1, 4, 4,0.5], [2, 2, 6, 6,0.7])
    print(det_iou)
