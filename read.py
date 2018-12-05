
data = []
#with open('not_00.o1307847','r') as f:
with open('../baseline/pytorch_resnet_cifar10/not_00_4.o1313080','r') as f:
#with open('not_00.o1307847','r') as f:
    for line in f:
        #print(line)
        if line.startswith(' * Prec@1'):
            words = line.split()
            data.append(float( words[-1] ))

#print(data)
print(max(data))
