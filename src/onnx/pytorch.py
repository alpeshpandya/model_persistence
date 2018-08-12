from torch.autograd import Variable
import torch.onnx
import torchvision
from resources.onnx.config import *
dummy_input = Variable(torch.randn(10, 3, 224, 224)).cuda()
model = torchvision.models.alexnet(pretrained=True).cuda()

# Providing input and output names sets the display names for values
# within the model's graph. Setting these does not change the semantics
# of the graph; it is only for readability.
#
# The inputs to the network consist of the flat list of inputs (i.e.
# the values you would pass to the forward() method) followed by the
# flat list of parameters. You can partially specify names, i.e. provide
# a list here shorter than the number of inputs to the model, and we will
# only set that subset of names, starting from the beginning.
input_names = [ 'actual_input_1' ] + [ 'learned_%d' % i for i in range(16) ]
output_names = [ 'output1' ]

torch.onnx.export(model, dummy_input, PYTORCH_ONNX, verbose=True, input_names=input_names, output_names=output_names)