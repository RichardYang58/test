import matplotlib.pyplot as plt
# import numpy as np
import matplotlib
import matplotlib.gridspec as gridspec

# print(matplotlib.__file__)

# a=np.arange(10)
# plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5)
# plt.show()

# a=np.arange(10)
# plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')
# plt.show()

# matplotlib.rcParams['font.family']='Kaiti'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus']=False
# plt.plot([3,1,4,5,2])
# plt.ylabel("縱軸(值)")
# plt.savefig('test',dpi=600)
# plt.show()

# a=np.arange(0.0,5.0,0.02)
# plt.plot(a,np.cos(2**np.pi*a),'r--')
# plt.xlabel('橫軸:時間',fontproperties='SimSun',fontsize=15,color='green')
# plt.ylabel('縱軸:震幅',fontproperties='SimSun',fontsize=15)
# plt.title(r'正玄波 $y=cos(2\pi x)$',fontproperties='SimSun',fontsize=25)
# # plt.text(2,1,r'$\mu=100$',fontsize=15)
# plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
# plt.axis([-1,6,-2,2])
# plt.grid(True)
# plt.show()

gs=gridspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,:-1])
ax3=plt.subplot(gs[1:,-1])
ax4=plt.subplot(gs[2:0])
ax5=plt.subplot(gs[2:1])
plt.show()


