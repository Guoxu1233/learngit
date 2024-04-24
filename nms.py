import numpy as np
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

def nms(detections, threshold=0.5):
    # detections: 待筛选的检测框列表，每个元素为(x1, y1, x2, y2, score)
    # threshold: 阈值，设定IoU值小于阈值的框为非极大值框

    if len(detections) == 0:
        return []

    # 按照置信度分数从高到低排序
    detections = sorted(detections, key=lambda x: x[4], reverse=True)

    # 用于保存最终保留下来的检测框
    keep = []

    while len(detections) > 0:
        # 取分数最高的框作为起始框
        A = detections[0]
        keep.append(A)

        # 计算该起始框和剩余框的IoU值
        B = detections[1:]
        overlaps = [iou(A, b) for b in B]

        # 将IoU值大于阈值的框删除
        indices = [i + 1 for i, overlap in enumerate(overlaps) if overlap > threshold]
        detections = [b for i, b in enumerate(detections) if i not in indices]

    return keep


if __name__ =="__main__":
    b1 = [1,2,3,4,0.2]
    b2 = [1,2,3,5,0.7]
    dect= [b1,b2]
    nms(dect,0.5)
    print(nms)
# 首先，我们来看最后两行代码的目的是什么：

# 确定与起始框（A）有较大重叠的检测框的索引。
# 根据这些索引从detections列表中删除相应的检测框。
# 现在，让我们逐行解释：
#
# indices = [i + 1 for i, overlap in enumerate(overlaps) if overlap > threshold]
# 这行代码的目的是生成一个索引列表，这些索引对应的检测框与起始框A的IoU值大于给定的阈值threshold。
#
# enumerate(overlaps): 这部分代码对overlaps列表中的每个元素overlap进行编号，返回一个元组，其中第一个元素是索引，第二个元素是IoU值。
# [i + 1 for i, overlap in enumerate(overlaps) if
#  overlap > threshold]: 这部分代码对每个元组进行迭代，如果IoU值大于阈值，则将索引加1（因为Python的索引是从0开始的）添加到新的列表中。
# detections = [b for i, b in enumerate(detections) if i not in indices]
# 这行代码的目的是根据上面生成的索引列表indices，从detections列表中删除相应的检测框。
#
# enumerate(detections): 对detections列表中的每个元素进行编号。
# [b for i, b in enumerate(detections) if
#  i not in indices]: 这是列表推导式的核心部分。它遍历detections列表中的每个元素，如果某个元素的索引不在indices列表中，那么这个元素就会被保留在新的列表中。换句话说，如果某个检测框的索引在indices中（意味着它与起始框有较大重叠），那么它就不会出现在新的detections列表中。
# 总结：这段代码首先找出与起始框有较大重叠的所有检测框的索引，然后根据这些索引从总检测框列表中删除这些重叠的检测框。这是非极大值抑制（NMS）的一个关键步骤，用于去除冗余或重叠的检测框，从而得到更精确的检测结果。