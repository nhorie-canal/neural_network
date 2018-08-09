# cording: UTF-8
import math
import matplotlib.pyplot as plt

#シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

#ニューロン
class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp
    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output
    def reset(self):
        self.input_sum = 0
        self.output = 0

#ニューラルネットワーク
class NeuralNetwork:
    #重み
    w_im = [[0.496, 0.512],[-0.501, 0.998], [0.498, -0.502]]
    w_mo = [0.121, -0.4996, 0.200]

    #各層の宣言
    input_layer = [0.0, 0.0, 1.0]
    middle_layer = [Neuron(), Neuron(), 1.0]
    output_layer = Neuron()
    


    #実行
    def commit(self, input_data):
        self.neuron.reset()

        bias = 1.0

        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        self.neuron.setInput(bias * self.w[2])
        return self.neuron.getOutput()



#基準点
refer_point_0 = 34.5
refer_point_1 = 137.5

trial_data = []
trial_data_file = open("trial_data", "r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0, float(line[1]) - refer_point_1])
trial_data_file.close()

neural_network = NeuralNetwork()

position_tokyo = [[],[]]
position_kanagawa = [[],[]]

for data in trial_data:
    if neural_network.commit(data) < 0.5:
        position_tokyo[0].append(data[1] + refer_point_1)
        position_tokyo[1].append(data[0] + refer_point_0)
    else:
        position_kanagawa[0].append(data[1] + refer_point_1)
        position_kanagawa[1].append(data[0] + refer_point_0)



plt.scatter(position_tokyo[0], position_tokyo[1], c="red", label="tokyo", marker="+")
plt.scatter(position_kanagawa[0], position_kanagawa[1], c="blue", label="kanagawa", marker="+")

plt.legend()
plt.show()
