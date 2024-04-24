import torch
from matplotlib import pyplot as plt

def farthest_point_sample(xyz,npoint):
    '''
    最远点采样,返回采样点的索引
    xyz: Batch*N*(x,y,z),Tensor
    npoint: 采样点个数,int
    '''
    B,N,C=xyz.shape     # Batch,N,3
    # 1*512,用于记录选取的512个点的索引
    centroids=torch.zeros(B,npoint,dtype=torch.long)
    # 1*1024,用于记录1024个全部数据点与已采样点的距离
    distance=torch.ones(B,N)*1e10
    # [6],第一个点从0~N中随机选取,如点6;
    farthest=torch.randint(0,N,(B,),dtype=torch.long)
    # 一批点云数据的标号,[0]
    batch_indices=torch.arange(B,dtype=torch.long)
    for i in range(npoint):
        # 第一个点随机选取
        centroids[:,i]=farthest
        # 获取当前采样点的坐标,(x,y,z)
        centroid=xyz[batch_indices,farthest,:].view(B,1,3)
        # 计算1024个全部采样点与当前采样点的欧式距离
        dist=torch.sum((xyz-centroid)**2,-1)
        # 为更新每个点到已采样点的距离做标记
        mask=dist<distance
        # 更新每个点到已采样点的距离
        distance[mask]=dist[mask]
        # 选取到已采样点距离最大的点作为下一个采样点
        farthest=torch.max(distance,-1)[1]
    return centroids
def index_points(points,idx):
    '''
    根据采样点的索引,取出采样点
    points:Batch*1024*(x,y,z),Tensor
    idx:Batch*512,Tensor
    '''
    B=points.shape[0]   # batch=1
    view_shape=list(idx.shape)
    view_shape[1:]=[1]*(len(view_shape)-1)
    repeat_shape=list(idx.shape)
    repeat_shape[0]=1
    batch_indices=torch.arange(B,dtype=torch.long).view(view_shape).repeat(repeat_shape)
    # 根据索引取出采样点
    new_points=points[batch_indices,idx,:]
    return new_points   # Batch*512*(x,y,z)


path="./modelnet40_normal_resampled/airplane/airplane_0001.txt"
data=open(path,"r")
x,y,z=[],[],[]
for line in data:
    tx,ty,tz,nx,ny,nz=line.split(",")
    x.append(eval(tx))
    y.append(eval(ty))
    z.append(eval(tz))

batches=[]
points=[]
for i in range(len(x)):
    point=[x[i],y[i],z[i]]
    points.append(point)
batches.append(points)
batches=torch.tensor(batches)
print(batches.shape)

idx=farthest_point_sample(batches,1024)
batches=index_points(batches,idx)
print(idx.shape)
print(batches.shape)


x,y,z=[],[],[]
for batch in range(batches.shape[0]):
    for i in range(batches.shape[1]):
        tx,ty,tz=batches[batch][i]
        x.append(tx)
        y.append(ty)
        z.append(tz)
    break
print(len(x))

# 3D散点图
fig=plt.figure()
ax=plt.axes(projection="3d")
ax.scatter3D(x,y,z,c="b",s=10,alpha=0.8,marker=".")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.pause(50)